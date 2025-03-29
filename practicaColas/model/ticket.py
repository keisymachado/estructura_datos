from pydantic import BaseModel

class Ticket(BaseModel):
    name: str # name of the person
    type: str # type of consultation
    identity: str # identity card
    case_description: str # description of the case
    age: int # age of the person
    priority_attention: bool = None  # Will be calculated automatically

def __init__(self, **data):
        # Si priority_attention no se proporciona, se asigna basado en la edad
    if "priority_attention" not in data or data["priority_attention"] is None:
        data["priority_attention"] = data["age"] >= 60
    super().__init__(**data)

