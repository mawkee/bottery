class Pattern:
    def __init__(self, pattern, view):
        self.pattern = pattern
        self.view = view

    def check(self, message):
        if message.text == self.pattern:
            return self.view
        return False


class DefaultPattern:
    def __init__(self, view):
        self.view = view

    def check(self, message):
        return self.view
