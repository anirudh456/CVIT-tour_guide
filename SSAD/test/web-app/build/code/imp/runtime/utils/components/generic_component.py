
from runtime.exceptions.app.exception import AppException

class GenericComponent:
    def __init__(self):
        self.method_map = {}

    def add_cmd_handler(self, cmd, handler):
        self.method_map[cmd] = handler

    def do(self, spec):
        cmd=spec['cmd']
        if cmd not in self.method_map.keys():
            raise AppException(op=cmd, msg="Unimplemented command")

        m = self.method_map[cmd]
        return m(self, spec)
