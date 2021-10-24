from pydantic import BaseModel

class BaseSchemaDTO(BaseModel):
    class Config:
        allow_population_by_field_name = True