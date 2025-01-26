from pydantic import BaseModel, ConfigDict


class BaseDto(BaseModel):
    """Базовая схема Pydantic"""

    model_config = ConfigDict(
        from_attributes = True
    )

