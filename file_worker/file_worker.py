from pathlib import Path
from typing import Optional, ClassVar, NoReturn
import csv

from utils import Singleton


class FileWorker(metaclass=Singleton):
    __ENCODING: ClassVar[str] = 'UTF-8-SIG'
    __DELIMITER: ClassVar[str] = ';'
    __NEW_LINE: ClassVar[str] = ''

    __TASK_NAME_INDEX: ClassVar[int] = 0
    __TASK_STATUS_INDEX: ClassVar[int] = 1

    __DATA_PATH: ClassVar[Path] = Path('resources', 'tasks.csv')

    @staticmethod
    def __validate_file(file_func):
        @classmethod
        def check_has_file(cls, *args, **kwargs) -> None:
            if not cls.__DATA_PATH.parent.is_dir():
                cls.__DATA_PATH.parent.mkdir()

            if not cls.__DATA_PATH.is_file():
                cls.__create_file()

            return file_func(cls, *args, **kwargs)

        return check_has_file

    @classmethod
    @__validate_file
    def read_file(cls) -> tuple[Optional[list[str]], ...]:
        with open(cls.__DATA_PATH, newline=cls.__NEW_LINE, encoding=cls.__ENCODING) as file:
            csv_text: csv.reader = csv.reader(file, delimiter=cls.__DELIMITER)

            return tuple(row for row in csv_text)

    @classmethod
    @__validate_file
    def write_file(cls, tasks_tuple: Optional[tuple[list[str], ...]] = None) -> NoReturn:
        if not tasks_tuple:
            cls.__create_file()
        else:
            with open(cls.__DATA_PATH, 'w', newline=cls.__NEW_LINE, encoding=cls.__ENCODING) as file:
                csv_writer: csv.writer = csv.writer(file, delimiter=cls.__DELIMITER)

                for row in tasks_tuple:
                    csv_writer.writerow(row)

    @classmethod
    def __create_file(cls) -> None:
        with open(cls.__DATA_PATH, 'w', newline=cls.__NEW_LINE, encoding=cls.__ENCODING):
            pass

    @classmethod
    @property
    def TASK_NAME_INDEX(cls) -> int:
        return cls.__TASK_NAME_INDEX

    @classmethod
    @property
    def TASK_STATUS_INDEX(cls) -> int:
        return cls.__TASK_STATUS_INDEX
