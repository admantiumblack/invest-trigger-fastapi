from Server.Schema.BaseSchema import BaseSchemaDTO
from pydantic.fields import Field
from typing import Optional

class UserSchemaDTO(BaseSchemaDTO):
    userId: Optional[int] = Field(alias='userId')
    fullName: Optional[str] = Field(alias='fullName')
    username: Optional[str] = Field(alias='username')
    email: Optional[str] = Field(alias='email')
    password: Optional[str] = Field(alias='password')

class UserRegisterSchemaDTO(BaseSchemaDTO):
    fullName: str = Field(alias='fullName')
    username: str = Field(alias='username')
    email: str = Field(alias='email')
    password: str = Field(alias='password')