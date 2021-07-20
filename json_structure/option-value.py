class OptionValueInput:
    text = None


class OptionValue:
    input = OptionValueInput()

    def __init__(self, text):
        self.input.text = text
