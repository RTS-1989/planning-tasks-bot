import logging
from typing import Optional

from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext

from bot.service import MAIN_KB
from planning.dialogs import planning_msg
from conversation.states.planning_states import PlanningTasks
from conversation.constants import REMOVE_INLINE_KEYBOARD_REPLY
from planning.keyboard import planning_is_countable_keyboard
from clients.planning_service.service import PlanningService
from clients.planning_service.response import PlanCreateSuccessResponse
from clients.planning_service.models import Plan


def init_planning_tasks(dp: Dispatcher, planning_service: PlanningService):

    def _get_bot_user_id(message: types.Message) -> Optional[int]:
        bot_user_id = getattr(message, "bot_user_id", None)
        return int(bot_user_id) if bot_user_id else None

    @dp.callback_query_handler(lambda c: c.data.startswith('planning_kb'))
    async def choose_planning_service(callback_query: types.CallbackQuery = None):
        planning_service_id = 0
        if callback_query:
            planning_service_id = callback_query.data.split('#')[-1]
            logging.info(f'Номер выбранного сервиса - {planning_service_id}')

        if planning_service_id == '1':
            await callback_query.message.answer(planning_msg.write_planning_message)
            await PlanningTasks.task_name.set()

        elif planning_service_id == '2':
            pass
        elif planning_service_id == '3':
            pass

    @dp.message_handler(state=PlanningTasks.task_name)
    async def get_task_name(message: types.Message, state: FSMContext):
        logging.info('get_task_name')
        await state.update_data(task_name=message.text)
        await message.answer(planning_msg.is_result,
                             reply_markup=planning_is_countable_keyboard())

    @dp.callback_query_handler(state=PlanningTasks.task_name)
    async def get_countable_info_yes_answer(callback: types.CallbackQuery):
        logging.info('set_countable_value')
        if callback.data == 'yes':
            logging.info('answer_yes')
            await PlanningTasks.next()
            await callback.message.answer(planning_msg.result)
            await PlanningTasks.countable_value.set()
        elif callback.data == 'no':
            logging.info('answer_no')
            await PlanningTasks.next()
            await callback.message.answer(planning_msg.deadline_result)
            await PlanningTasks.deadline.set()

    @dp.message_handler(state=PlanningTasks.countable_value)
    async def set_countable_info_value(message: types.Message, state: FSMContext):
        logging.info('set_countable_value')
        await state.update_data(countable_value=int(message.text))
        await PlanningTasks.next()
        await message.answer(planning_msg.deadline_result)
        await PlanningTasks.deadline.set()

    @dp.message_handler(state=PlanningTasks.deadline)
    async def set_deadline_info(message: types.Message, state: FSMContext):
        logging.info('set_deadline')
        await state.update_data(deadline=message.text)
        data = await state.get_data()
        await state.finish()
        bot_user_id = _get_bot_user_id(message)
        await message.answer(f'{data.get("task_name")} - {data.get("countable_value")} - {data.get("deadline")}')
        response = await planning_service.send_planning_task(bot_user_id=bot_user_id,
                                                             task_name=data.get("task_name"),
                                                             countable_value=data.get('countable_value'),
                                                             deadline=data.get('deadline')
                                                             )

        if isinstance(response, PlanCreateSuccessResponse):
            planning_task: Plan = response.item
            await message.edit_reply_markup(reply_markup=REMOVE_INLINE_KEYBOARD_REPLY)
            await message.answer(f'Задача {planning_task.id} внесена в базу', reply_markup=MAIN_KB)
