from utils import *


class Chain:
    def __init__(self) -> None:
        self._llm = get_llm()
        
    def get_llm(self):
        return self._llm
    def get_data(self):
        return self._data

    def load_data(self,code:str)->None:
        self._data = code

    def get_result(self)->str:
        if not hasattr(self,"_data"):
            raise Exception()
        return get_roast(self._data, self._llm)