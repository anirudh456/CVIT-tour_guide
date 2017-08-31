
class ArityException(Exception):
    lm = None

    def __init__(self, **litmap):
        self.lm = {'type': 'ArityException', 'data': litmap}

    def __str__(self):
        return repr(self.lm)

    # to_client : ArityException -> Litmap
    def to_client(self):
        return self.lm
