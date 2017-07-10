"""
Filesystem-based implementation of AuralScratchDB
"""
import pickle
from typing import TypeVar, Generic, Mapping

from .api import AuralScratchDB, DBField
from ..concepts import *
from ..lazydict import LazyDictionary

N = TypeVar('N', bound=Naming)


# DBFields store their info under $base_dir/$name/
class FileSystemDBField(Generic[N], DBField[N]):
    def __init__(self, db: 'FileSystemDB', name: str):
        self.name = name
        self.parent = db

    @property
    def _base_dir(self) -> Path:
        return self.parent.base_dir / self.name

    def get(self, name: str) -> N:
        p = self._base_dir / name
        if not p.exists():
            raise KeyError(name)
        with p.open('rb') as fp:
            return pickle.load(fp)

    def get_map(self) -> Mapping[str, N]:
        p = self._base_dir
        if not p.exists():
            return dict()
        return LazyDictionary({f.name: self.get for f in p.iterdir()})

    def put(self, obj: N):
        d = self._base_dir
        d.mkdir(parents=True, exist_ok=True)
        p = d / obj.get_name()
        with p.open('wb') as fp:
            pickle.dump(obj, fp, protocol=3)


class FileSystemDB(AuralScratchDB):
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self._tags = FileSystemDBField(self, 'tags')  # type: FileSystemDBField[Tag]
        self._playlists = FileSystemDBField(self, 'playlists')  # type: FileSystemDBField[PlaylistBase]
        self._tag_categories = FileSystemDBField(self, 'tag_categories')  # type: FileSystemDBField[TagCategory]
        self._songs = FileSystemDBField(self, 'songs')  # type: FileSystemDBField[Song]

    @property
    def tags(self) -> DBField[Tag]:
        return self._tags

    @property
    def playlists(self) -> DBField[PlaylistBase]:
        return self._playlists

    @property
    def tag_categories(self) -> DBField[TagCategory]:
        return self._tag_categories

    @property
    def songs(self) -> DBField[Song]:
        return self._songs
