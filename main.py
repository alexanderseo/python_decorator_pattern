from SelectType import SelectType
from UnserializeInputString import UnserializeInputString
from StaticAttributes import StaticAttributes
from VariableAttributes import VariableAttributes
from DynamicDict import DynamicDict


class MainApp:
    def __init__(self):
        self.data = []
        self.string_data = 'a:12:{s:16:"pa_overall-width";a:6:{s:4:"name";s:16:"pa_overall-width";s:5:"value";s:0:"";s:8:"position";i:0;s:10:"is_visible";i:0;s:12:"is_variation";i:1;s:11:"is_taxonomy";i:1;}s:20:"pa_folding-mechanism";a:6:{s:4:"name";s:20:"pa_folding-mechanism";s:5:"value";s:0:"";s:8:"position";i:1;s:10:"is_visible";i:1;s:12:"is_variation";i:0;s:11:"is_taxonomy";i:1;}s:14:"pa_seat-height";a:6:{s:4:"name";s:14:"pa_seat-height";s:5:"value";s:0:"";s:8:"position";i:2;s:10:"is_visible";i:0;s:12:"is_variation";i:0;s:11:"is_taxonomy";i:1;}s:13:"pa_seat-depth";a:6:{s:4:"name";s:13:"pa_seat-depth";s:5:"value";s:0:"";s:8:"position";i:3;s:10:"is_visible";i:1;s:12:"is_variation";i:0;s:11:"is_taxonomy";i:1;}s:16:"pa_armrest-width";a:6:{s:4:"name";s:16:"pa_armrest-width";s:5:"value";s:0:"";s:8:"position";i:4;s:10:"is_visible";i:1;s:12:"is_variation";i:0;s:11:"is_taxonomy";i:1;}s:14:"pa_legs-height";a:6:{s:4:"name";s:14:"pa_legs-height";s:5:"value";s:0:"";s:8:"position";i:5;s:10:"is_visible";i:0;s:12:"is_variation";i:1;s:11:"is_taxonomy";i:1;}s:16:"pa_legs-material";a:6:{s:4:"name";s:16:"pa_legs-material";s:5:"value";s:0:"";s:8:"position";i:6;s:10:"is_visible";i:1;s:12:"is_variation";i:0;s:11:"is_taxonomy";i:1;}s:17:"pa_frame-material";a:6:{s:4:"name";s:17:"pa_frame-material";s:5:"value";s:0:"";s:8:"position";i:7;s:10:"is_visible";i:1;s:12:"is_variation";i:0;s:11:"is_taxonomy";i:1;}s:11:"pa_softness";a:6:{s:4:"name";s:11:"pa_softness";s:5:"value";s:0:"";s:8:"position";i:8;s:10:"is_visible";i:1;s:12:"is_variation";i:0;s:11:"is_taxonomy";i:1;}s:15:"pa_manufacturer";a:6:{s:4:"name";s:15:"pa_manufacturer";s:5:"value";s:0:"";s:8:"position";i:9;s:10:"is_visible";i:1;s:12:"is_variation";i:0;s:11:"is_taxonomy";i:1;}s:9:"pa_fabric";a:6:{s:4:"name";s:9:"pa_fabric";s:5:"value";s:0:"";s:8:"position";i:10;s:10:"is_visible";i:0;s:12:"is_variation";i:1;s:11:"is_taxonomy";i:1;}s:11:"pa_benefits";a:6:{s:4:"name";s:11:"pa_benefits";s:5:"value";s:0:"";s:8:"position";i:11;s:10:"is_visible";i:0;s:12:"is_variation";i:0;s:11:"is_taxonomy";i:1;}}'
        self.unserialize_input_string = UnserializeInputString()
        self.static_attributes = StaticAttributes(self.unserialize_input_string)
        self.variable_attributes = VariableAttributes(self.unserialize_input_string)
        self._inn = DynamicDict()

    def get(self):
        self.set_attributes(self.static_attributes, self.string_data)
        self.set_attributes(self.variable_attributes, self.string_data)

        return self.data

    def set_attributes(self, select_type: SelectType, string_data: str) -> None:
        self.data.append(select_type.input_serialization_array(string_data))


if __name__ == "__main__":
    x = MainApp()
    print(x.get())
