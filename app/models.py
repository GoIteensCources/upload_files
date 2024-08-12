from typing import List

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import db


class UploadModel(db.Model):
    __tablename__ = "file_save"

    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column(sa.String(125))
    data_file: Mapped[bytes] = mapped_column(sa.LargeBinary)

    imgname: Mapped[str] = mapped_column(sa.String(255))
    data_img: Mapped[bytes] = mapped_column(sa.LargeBinary)
