from enum import StrEnum
from typing import Literal, Type, Final


# Статусы задач
class TaskConstant(StrEnum):
    NOT_STARTED: Final[str] = "NOT_STARTED"
    PROCESSING: Final[str] = "PROCESSING"
    DONE: Final[str] = "DONE"


TASK_CONSTANTS_LITERAL: Type[TaskConstant] = Literal[
    TaskConstant.NOT_STARTED,
    TaskConstant.PROCESSING,
    TaskConstant.DONE
]
