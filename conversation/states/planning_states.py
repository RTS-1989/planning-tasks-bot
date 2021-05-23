from aiogram.dispatcher.filters.state import StatesGroup, State


class PlanningTasks(StatesGroup):
    task_name = State()
    countable_value = State()
    deadline = State()
