from typing import Any, Callable, Dict, Mapping, TypeVar, Generic, Iterable

LazySourceDict = Dict[Any, Callable[[str], Any]]

K = TypeVar('K')
V = TypeVar('V')


class LazyDictionary(Generic[K, V], Mapping[K, V]):
    def __init__(self, source: LazySourceDict):
        self._source = source
        self._loaded = dict()

    def __getitem__(self, key: K) -> V:
        if key not in self._loaded:
            if key not in self._source:
                raise KeyError(key)
            self._loaded[key] = self._source[key](key)

        return self._loaded[key]

    def __iter__(self) -> Iterable[K]:
        yield from self._source.keys()

    def __len__(self) -> int:
        return len(self._source)
