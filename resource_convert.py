class ResourceConverter():
    """Generiek resource converter maakt van een json een python instance aan zoals die staan in /models/"""

    @staticmethod
    def from_json(resource_name, json_val):
        module_name = resource_name.lower()
        module = __import__('models.' + module_name)
        module = getattr(module, module_name)
        cls = getattr(module, module_name.capitalize())

        import json

        if isinstance(json_val, str):
            json_val =json_val.replace("'", '"')
            json_val = json.loads(json_val)

        resource = cls(json_val)
        return resource
