from typing import NoReturn, ClassVar, Optional
from dataclasses import dataclass, field

from utils import Singleton
from config import TaskConstant, TASK_CONSTANTS_LITERAL


class ToDoList(metaclass=Singleton):
    def __init__(self):
        self.__tasks_dict: dict[int, Task] = {}

    def add_task(self, description: str):
        self.__tasks_dict[Task.COUNT_ID] = Task(description)

    def remove_task(self, task_id: int) -> NoReturn:
        self.__tasks_dict.pop(task_id)

    def update_status(self, task_id: int, status: TASK_CONSTANTS_LITERAL) -> NoReturn:
        self.__tasks_dict[task_id].status = status

    def view_tasks(self) -> tuple[Optional[list[str]], ...]:
        return tuple([task.description, task.status] for task in self.__tasks_dict.values())


@dataclass
class Task:
    __COUNT_ID: ClassVar[int] = 0

    __description: str

    __id: int = field(init=False)
    __status: str = field(init=False, default=TaskConstant.NOT_STARTED)

    def __post_init__(self) -> NoReturn:
        Task.__COUNT_ID += 1
        self.__id = Task.__COUNT_ID

    @classmethod
    @property
    def COUNT_ID(cls) -> int:
        return cls.__COUNT_ID

    @property
    def description(self) -> str:
        return self.__description

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: TASK_CONSTANTS_LITERAL) -> NoReturn:
        self.__status = status
