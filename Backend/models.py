from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    
class IMDBInfo(Base):
    __tablename__ = "IMDBInfo"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    titleType: Mapped[str] = mapped_column(String(20), nullable=False)
    primaryTitle: Mapped[str] = mapped_column(String(50), nullable=False)
    originalTitle: Mapped[str] = mapped_column(String(50), nullable=False)
    isAdult: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    startYear: Mapped[int] = mapped_column(Integer, nullable=False)
    endYear: Mapped[int] = mapped_column(Integer, nullable=True)
    runtimeMinutes: Mapped[int] = mapped_column(Integer, nullable=True)
    genres: Mapped[str] = mapped_column(String(50), nullable=False)
    
    #1-to-1 Relationship to Ratings table
    rating: Mapped["IMDBRating"] = relationship(back_populates="info")

class IMDBRating(Base):
    __tablename__ = "IMDBRatings"
    
    id: Mapped[int] = mapped_column(ForeignKey("IMDBInfo.id"), primary_key=True)
    averageRating: Mapped[float] = mapped_column(Float, nullable=False)
    numVotes: Mapped[int] = mapped_column()
    
    #1-to-1 Relationship to Basics table
    info: Mapped["IMDBInfo"] = relationship(back_populates="rating")