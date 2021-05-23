from dataclasses import dataclass


@dataclass(frozen=True)
class PlanningMessages:
    write_planning_message: str = 'Напишите задачу'
    is_result: str = 'Есть исчисляемое значение для задачи (например, прочесть 100 страниц в книге)?'
    result: str = 'Укажите значения для требуемого резульата (напишите тольео цифру).'
    deadline_result: str = 'До какого числа нужно выполнить задачу? (Внесите только цифры формата 10-01-2021)'
    task_in_database: str = 'Задача внесена в базу данных. Теперь вы можете получить информацию об этой задаче через ' \
                            'кнопку "Получить список запланированных задач".'


planning_msg = PlanningMessages()
