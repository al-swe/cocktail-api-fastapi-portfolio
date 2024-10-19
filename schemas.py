from enum import Enum
from pydantic import BaseModel

class AlcoholType(Enum):
    vodka = "vodka"
    gin = "gin"
    rum = "rum"
    tequila = "tequila"
    whiskey = "whiskey"
    brandy = "brandy"
    liqueur = "liqueur"
    wine = "wine"
    beer = "beer"
    other = "other"

class Cocktail(BaseModel):
    id: int
    name: str
    description: str
    ingredients: list[str]
    instructions: list[str]
    glass: str
    category: str
    alcoholic: str
    image: str
    tags: list[str]