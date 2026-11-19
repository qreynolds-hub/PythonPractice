class Pet:
    """Superclass for all pets."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")
