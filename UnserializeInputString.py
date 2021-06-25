from SelectType import SelectType
from phpserialize import *


class UnserializeInputString(SelectType):
    def input_serialization_array(self, string_array: str) -> dict:
        return unserialize(string_array.encode('utf-8'), decode_strings=True)
