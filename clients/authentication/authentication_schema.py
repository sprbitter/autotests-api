from pydantic import BaseModel


class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """
    tokenType: str
    accessToken: str
    refreshToken: str