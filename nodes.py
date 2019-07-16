from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config
from relationships import *

"""
neomodel documentation https://neomodel.readthedocs.io/en/latest/index.html
"""

config.DATABASE_URL = 'bolt://neo4j:123456@localhost:7687'

class Food(StructuredNode):
    name_en = StringProperty(unique_index=True)
    name_vi = StringProperty(unique_index=False)
    nutritions = RelationshipTo('Nutrition', 'CONTAIN', model=FoodContainsNutrition)
    effects = RelationshipTo('Effect', 'HAS', model=FoodHasEffect)


class Nutrition(StructuredNode):
    name = StringProperty(unique_index=False)
    foods = RelationshipFrom('Food', 'CONTAIN', model=FoodContainsNutrition)

# class Condition(StructuredNode):
#     name = StringProperty(unique_index=True)


class Effect(StructuredNode):
    name = StringProperty(unique_index=True)
    # type = {advantages, disadvantages}
    type = StringProperty()
    description = StringProperty()
    foods = RelationshipFrom('Food', 'HAS', model=FoodHasEffect)    

# harry_potter = Book(title='Harry potter and the..').save()
# rowling =  Author(name='J. K. Rowling').save()
# harry_potter.author.connect(rowling)