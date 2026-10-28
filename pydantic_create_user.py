from pydantic import BaseModel


class UserSchema(BaseModel):
    """Модель данных пользователя"""

class CreateUserRequestSchema(UserSchema):
