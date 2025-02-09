from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    """Абстрактный строитель, определяющий шаги для ремонтных работ"""

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def preparation_floor(self) -> None:
        """Подготовить пол перед укладкой плитки"""
        pass

    @abstractmethod
    def lay_the_tiles(self) -> None:
        """Уложить плитку"""
        pass

    @abstractmethod
    def apply_putty(self) -> None:
        """Нанести шпаклевку"""
        pass

    @abstractmethod
    def plaster_the_walls(self) -> None:
        """Оштукатурить стены"""
        pass

    @abstractmethod
    def prime_the_walls(self) -> None:
        """Загрунтовать стены"""
        pass

    @abstractmethod
    def paint_the_walls(self) -> None:
        """Покрасить стены"""
        pass


class TileSetter(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Renovation()

    @property
    def product(self) -> Renovation:
        product = self._product
        self.reset()
        return product

    def preparation_floor(self) -> None:
        """Подготовка пола для укладки плитки"""
        self._product.add("Подготовка пола")

    def lay_the_tiles(self) -> None:
        """Укладка плитки"""
        self._product.add("Укладка плитки")


class Finisher(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Renovation()

    @property
    def product(self) -> Renovation:
        product = self._product
        self.reset()
        return product

    def apply_putty(self) -> None:
        """Нанести шпаклевку на стены"""
        self._product.add("Наносим шпаклевку")

    def plaster_the_walls(self) -> None:
        """Оштукатурить стены"""
        self._product.add("Оштукатуриваем стены")


class Painter(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Renovation()

    @property
    def product(self) -> Renovation:
        product = self._product
        self.reset()
        return product

    def prime_the_walls(self) -> None:
        """Загрунтовать стены"""
        self._product.add("Грунтуем стену")

    def paint_the_walls(self) -> None:
        """Покрасить стены"""
        self._product.add("Красим стену")