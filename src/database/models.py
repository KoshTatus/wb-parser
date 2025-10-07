from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'goods'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    rating: Mapped[float] = mapped_column()
    review_count: Mapped[int] = mapped_column()
    remaining_count: Mapped[int] = mapped_column()