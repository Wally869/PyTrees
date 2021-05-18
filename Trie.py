from typing import List, Tuple, Union, Dict


from BaseTree import BaseTree

class Trie(BaseTree):
    def __init__(self):
        self.Map: Dict[Trie] = {}
        self.Value: Union[None, int] = None
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
    def delete(self, item: str) -> bool:
        if len(item) == 0:
            raise KeyError("Trie delete - Invalid item of len 0")
        else:
            if self.__getitem__(item) is None:
                return False
            else:
                if len(item) == 1:
                    self.Map[item] = None
                else:
                    self.Map[item[0]].delete(item[1:])
                return True
    def __ensure_not_none(self, key: str):
        if key not in self.Map.keys():
            self.Map[key] = Trie()

