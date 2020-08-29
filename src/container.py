from datetime import datetime, timezone
from jsonpath_ng import parse


class Container:

    def __init__(self, data):
        self.data = data

    def _get_object(self, path):
        result = parse("$." + path).find(self.data)
        return None if not result else result[0].value

    def get_name(self):
        return self._get_object("name")

    def get_creation(self):
        date = datetime.strptime(self._get_object("created_at"), '%Y-%m-%dT%H:%M:%S%z')
        return date.replace(tzinfo=timezone.utc).timestamp()

    def get_status(self):
        return self._get_object("state.status")

    def get_cpu(self):
        return self._get_object("state.cpu.usage")

    def get_memory(self):
        return self._get_object("state.memory.usage")

