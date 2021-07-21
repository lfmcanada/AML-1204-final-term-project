from output_value import OutputValue
from option import Option

class GenericOutput:
    values: list[OutputValue] = []
    option : list[Option] = []
    esponse_type: str = None
    selection_policy:str = 'sequential'
    repeat_on_reprompt: bool = True