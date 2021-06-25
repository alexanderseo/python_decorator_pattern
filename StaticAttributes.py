from ProductAttributes import ProductAttributes
from DynamicDict import DynamicDict


class StaticAttributes(ProductAttributes):
    def input_serialization_array(self, string_array: str) -> list:
        attributes = super().input_serialization_array(string_array)
        data = []
        static_attributes = DynamicDict()

        for key, item in attributes.items():
            if str(item['is_visible']) == '1':
                static_attributes['static'][item['name']] = item['name']

        data.append(static_attributes)

        return data
