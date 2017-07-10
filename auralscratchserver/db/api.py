from abc import ABC, abstractmethod
from ..concepts import *
from typing import TypeVar, Generic, Mapping

N = TypeVar('N', bound=Naming)


class DBField(Generic[N], ABC):
    @abstractmethod
    def put(self, obj: N):
        pass

    def get(self, name: str) -> N:
        pass

    @abstractmethod
    def get_map(self) -> Mapping[str, N]:
        pass


class AuralScratchDB(ABC):
    @property
    @abstractmethod
    def songs(self) -> DBField[Song]:
        pass

    @property
    @abstractmethod
    def tag_categories(self) -> DBField[TagCategory]:
        pass

    @property
    @abstractmethod
    def tags(self) -> DBField[Tag]:
        pass

    @property
    @abstractmethod
    def playlists(self) -> DBField[PlaylistBase]:
        pass
