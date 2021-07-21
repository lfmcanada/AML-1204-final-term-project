from json_structure.workspace import Workspace


class DialogSettings:
    actions: bool = True


class Skill:
    name: str = None
    type: str = 'dialog'
    status: str = 'Available'
    created: str = 'YYYY-MM-DDTHH:MM:SS.MMMZ'
    updated: str = 'YYYY-MM-DDTHH:MM:SS.MMMZ'
    language: str = 'en'
    skill_id: str = None
    workspace: Workspace
    description: str = None
    workspace_id: str = None
    dialog_settings: DialogSettings = DialogSettings()
