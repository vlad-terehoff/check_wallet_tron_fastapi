from src.base.base_models.db_models import Base, str_256
from sqlalchemy.orm import Mapped, mapped_column


class CheckRequestModel(Base):
    __tablename__ = 'check_request'

    wallet: Mapped[str_256] = mapped_column(nullable=False)

    def __str__(self) -> str:
        return self.wallet



