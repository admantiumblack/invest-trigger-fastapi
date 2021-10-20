from pydantic import BaseModel
from pydantic.fields import Field

class BaseModelDTO(BaseModel):
    class Config:
        allow_population_by_field_name = True
        }
