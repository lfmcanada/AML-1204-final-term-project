from step_output import StepOutput
class StepResolver:
    type: str = None
class Step:
    step : str = None
    output : StepOutput
    handlers : list[str] = []
    resolver: StepResolver = StepResolver()
    variable : str = None