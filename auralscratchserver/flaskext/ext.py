from flask import Flask
from abc import ABC, abstractmethod


class FlaskExtension(ABC):
    @abstractmethod
    def extend(self, app: Flask):
        pass
