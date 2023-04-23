from sqlalchemy import Column, ForeignKey, String, Text, Integer
from sqlalchemy.orm import relationship

from src.database.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


class Ingredient(Base):
    __tablename__ = "ingredient"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    recipe_id = Column(Integer, ForeignKey("recipe.id"))

    recipe_ingr = relationship("Recipe", back_populates="ingredient")


class Cook_Step(Base):
    __tablename__ = "cook_step"

    id = Column(Integer, primary_key=True)
    step = Column(Integer)
    time = Column(Integer)
    description = Column(Text)
    url = Column(String)

    recipe_id = Column(Integer, ForeignKey("recipe.id"))
    recipe_cook = relationship("Recipe", back_populates="cook_step")


class Recipe(Base):
    __tablename__ = "recipe"

    id =  Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    url = Column(String)

    ingredient = relationship("Ingredient", back_populates="recipe_ingr")
    cook_step = relationship("Cook_Step", back_populates="recipe_cook")
    ratings = relationship("Rate", back_populates="recipes", cascade="all, delete")

class Rate(Base):
    __tablename__ = "rate"

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    recipe_id = Column(Integer, ForeignKey("recipe.id", ondelete='CASCADE'))
    recipes = relationship("Recipe", back_populates="ratings", cascade="all, delete")
