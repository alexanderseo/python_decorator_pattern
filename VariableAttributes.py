from ProductAttributes import ProductAttributes
from DynamicDict import DynamicDict


class VariableAttributes(ProductAttributes):
    def input_serialization_array(self, string_array: str) -> list:
        attributes = super().input_serialization_array(string_array)
        data = []
        variable_attributes = DynamicDict()

        for key, item in attributes.items():
            if str(item['is_variation']) == '1':
                variable_attributes['variable'][item['name']] = item['name']

        data.append(variable_attributes)

        return data
