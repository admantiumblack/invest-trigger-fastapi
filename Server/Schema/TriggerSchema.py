from Server.Schema.BaseSchema import BaseSchemaDTO
from pydantic.fields import Field
from typing import Optional

class TriggerSchemaDTO(BaseSchemaDTO):
    period:str = Field(alias='comparator')
    pair:str = Field(alias='pair')
    indicator1: Optional[str] = Field(alias='indicator1')
    indicatorVar1: Optional[int] = Field(alias='indicatorVar1')
    comparator:str = Field(alias='comparator')
    indicator2: Optional[str] = Field(alias='indicator2')
    indicatorVar2: Optional[int] = Field(alias='indicatorVar2')