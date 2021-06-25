from SelectType import SelectType


class ProductAttributes(SelectType):
    _select_type: SelectType = None

    def __init__(self, select_type: SelectType) -> None:
        self._select_type = select_type

    @property
    def select_type(self):
        return self._select_type

    def input_serialization_array(self, string_array: str) -> dict:
        return self._select_type.input_serialization_array(string_array)
