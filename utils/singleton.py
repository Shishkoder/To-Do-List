from abc import ABCMeta
from typing import Optional


class Singleton(ABCMeta):
    """Класс, описывающий Синглтон

    :cls:
    :__INSTANCES: Ссылка на экземпляр.

    """
    __INSTANCES: Optional[type] = None

    def __call__(cls, *args, **kwargs) -> type:
        # Проверка на существования уже готового экземпляра
        if cls.__INSTANCES is None:
            cls.__INSTANCES = super().__call__(*args, **kwargs)
        return cls.__INSTANCES
