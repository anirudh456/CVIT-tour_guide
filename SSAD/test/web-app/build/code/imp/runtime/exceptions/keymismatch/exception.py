
class KeyMismatchException(Exception):
    lm = None

    def __init__(self, **litmap):
        self.lm = {'type': 'KeyMismatchException', 'data': litmap}

    def __str__(self):
        return repr(self.lm)

    # to_client : KeyMismatchException -> Litmap
    def to_client(self):
        return self.lm
