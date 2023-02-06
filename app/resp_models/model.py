from pydantic import BaseModel, Field, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str = Field(default = None)


class User(BaseModel):
    id : int = Field(default = None)
    username: str = Field(default = None)
    email: EmailStr = Field(default = None)
    full_name: str = Field(default = None)
    disabled: bool = Field(default = None)


class UserInDB(User):
    hashed_password: str