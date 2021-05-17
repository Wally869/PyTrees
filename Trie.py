from typing import List, Tuple, Union


from BaseTree import BaseTree

class Trie(BaseTree):
    def __init__(self):
        self.Map = {}
        self.Value = None
    def __setitem__(self, item: str, value: int) -> None:
        if len(item) == 0:
            raise KeyError("Trie __setitem__ - Invalid item of len 0")
        else:
            self.__ensure_not_none(item[0])
            if len(item) == 1:
                self.Map[item].Value = value
            else:
                self.Map[item[0]][item[1:]] = value
    def __getitem__(self, item: str) -> Union[None, int]:
        if len(item) == 0:
            raise KeyError("Trie __getitem__ - Invalid item of len 0")
        else:
            self.__ensure_not_none(item[0])
            if len(item) == 1:
                return self.Map[item].Value
            else:
                return self.Map[item[0]][item[1:]]
    def __ensure_not_none(self, key: str):
        if key not in self.Map.keys():
            self.Map[key] = Trie()

