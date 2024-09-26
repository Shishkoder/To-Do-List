from typing import NoReturn, Optional

from todo_list import ToDoList
from config import TaskConstant
from file_worker import FileWorker


def only_read(todo_list: ToDoList, file_worker: FileWorker) -> NoReturn:
    tasks_tuple: tuple[Optional[list[str]], ...] = file_worker.read_file()
    for task in tasks_tuple:
        todo_list.add_task(task[FileWorker.TASK_NAME_INDEX])

    print(file_worker.read_file())


def only_write(todo_list: ToDoList, file_worker: FileWorker) -> NoReturn:
    todo_list.add_task("Помыть полы")
    todo_list.add_task("Посмотреть фильм")
    todo_list.add_task("Задача для удаления")
    todo_list.add_task("Лечь спать")

    todo_list.update_status(1, TaskConstant.DONE)
    todo_list.update_status(2, TaskConstant.PROCESSING)

    todo_list.remove_task(3)
    tasks_tuple: tuple[Optional[list[str]], ...] = todo_list.view_tasks()

    file_worker.write_file(tasks_tuple)


def main() -> NoReturn:
    todo_list: ToDoList = ToDoList()
    file_worker: FileWorker = FileWorker()

    is_write: bool = True
    if is_write:
        only_write(todo_list, file_worker)
    else:
        only_read(todo_list, file_worker)


if __name__ == '__main__':
    main()
