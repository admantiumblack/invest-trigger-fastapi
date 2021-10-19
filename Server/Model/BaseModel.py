from pydantic import BaseModel
from pydantic.fields import Field

class BaseModelDTO(BaseModel):
    Parameter1:str = Field(alias='Parameter1')
    Parameter2:str = Field(alias='Parameter2')
    Parameter3:int = Field(alias='Parameter3')
    Parameter4:int = Field(alias='Parameter4')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "Parameter1":"something2",
                "Parameter2":"something2",
                "Parameter3":123,
                "Parameter4":234
            }
        }