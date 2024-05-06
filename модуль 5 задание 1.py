class StringVar:
    text: str

    def __init__(self, text: str):
        self.set(text)

    def get(self) -> str:
        return self.text

    def set(self, text: str):
        assert isinstance(text, str), "Use str type only!"
        self.text = text