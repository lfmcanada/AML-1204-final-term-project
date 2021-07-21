from step import Step
from condition import Condition
from action_variable import ActionVariable
class Action:
    steps : list[Step] = []
    title : str = None
    action : str = None
    handlers: list[str] = []
    condition : Condition = Condition()
    variables: list[ActionVariable] = []
    next_action: str = None
    disambiguation_opt_out:bool = False


