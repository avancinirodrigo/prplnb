class SortService:
    def __init__(self, sortKeys: list, dicts: dict):
        self._sortKeys = sortKeys
        self._dicts = dicts

    def exec(self):
        for k in self._sortKeys:
            self._dicts[k].sort()
        return self._dicts
