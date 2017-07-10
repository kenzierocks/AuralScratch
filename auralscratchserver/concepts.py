from abc import ABC
from pathlib import Path
from typing import List, TypeVar
from uuid import UUID, uuid4

D = TypeVar('D')


class Identifiable:
    def __init__(self, uuid: UUID = None):
        self.uuid = uuid or uuid4()

    def with_uuid(self: D, uuid: UUID) -> D:
        self.uuid = uuid
        return self


class Naming(ABC):
    def get_name(self) -> str:
        if hasattr(self, 'name'):
            return getattr(self, 'name')
        raise ValueError("No name field on self, override get_name!")

    def __str__(self):
        return self.get_name()


class TagCategory(Identifiable, Naming):
    def __init__(self, name: str):
        super().__init__()
        self.name = name


class Tag(Identifiable, Naming):
    def __init__(self, category: TagCategory, value: str):
        super().__init__()
        self.category = category
        self.value = value

    def get_name(self):
        return str(self.category) + ': ' + self.value


class Song(Identifiable, Naming):
    def __init__(self, name: str, file: Path = None, tags: List = None):
        super().__init__()
        self.name = name
        self.file = file
        self.tags = tags or []  # type: List


class PlaylistBase(Identifiable, Naming):
    def __init__(self, name: str, songs: List[Song] = None):
        super().__init__()
        self.name = name
        self._songs = songs or []  # type: List

    @property
    def songs(self):
        """
        :return: the songs in this playlist. Retrieving this may incur a performance hit while smart playlists update.
        """
        return tuple(self._songs)


class Playlist(PlaylistBase):
    def add_song(self, song: Song):
        """
        Simply appends a song.

        :param song: the song to add to this playlist
        """
        self._songs.append(song)

    def get_songs_list(self):
        """
        Exposes the actual list of songs, for free modification by other mechanisms.
        :return: the list of songs
        """
        return self._songs


# TODO SmartPlaylist
class SmartPlaylist(PlaylistBase):
    def __init__(self, name: str):
        super().__init__(name)
        raise NotImplementedError("Smart playlists are a TODO item.")
