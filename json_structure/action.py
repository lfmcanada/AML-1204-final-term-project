from json_structure.action_variable import ActionVariable
from json_structure.condition import Condition
from json_structure.step import Step


class Action:
    steps: list[Step] = []
    title: str = None
    action: str = None
    handlers: list[str] = []
    condition: Condition = Condition()
    variables: list[ActionVariable] = []
    next_action: str = None
    disambiguation_opt_out: bool = False
