from datetime import datetime, timezone

from jsonpath_ng import parse


class Container:

    def __new__(cls, data):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            cls.data = data
            return cls.instance
        else:
            return cls.instance(data)

    def __call__(self, data):
        self.data = data
        return self

    def _get_data(self, path):
        result = parse("$." + path).find(self.data)
        return None if not result else result[0].value

    def get_name(self):
        return self._get_data("name")

    def get_creation(self):
        return self._get_data("created_at")

    def get_status(self):
        return self._get_data("state.status")

    def get_cpu(self):
        return self._get_data("state.cpu.usage")

    def get_memory(self):
        return self._get_data("state.memory.usage")

