from json_structure.entity_value import EntityValue


class Entity:
    entity: str = None
    values: list[EntityValue] = []
    fuzzy_match: bool = True
