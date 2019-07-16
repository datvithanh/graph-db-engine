from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config
from relationships import FoodAffectCondition, FoodAffectConsumerGroup, FoodContainsNutrition, FoodHasEffect

"""
neomodel documentation https://neomodel.readthedocs.io/en/latest/index.html
"""

config.DATABASE_URL = 'bolt://neo4j:123456@localhost:7687'

class Food(StructuredNode):
    name_en = StringProperty(unique_index=True)
    name_vi = StringProperty(unique_index=False)
    nutritions = RelationshipTo('Nutrition', 'CONTAIN', model=FoodContainsNutrition)
    effects = RelationshipTo('Effect', 'HAS', model=FoodHasEffect)
    conditions = RelationshipTo('Condition', 'AFFECT', model=FoodAffectCondition)

class Nutrition(StructuredNode):
    name = StringProperty(unique_index=False)
    foods = RelationshipFrom('Food', 'CONTAIN', model=FoodContainsNutrition)

class Condition(StructuredNode):
    name = StringProperty(unique_index=True)
    foods = RelationshipFrom('Food', 'AFFECT', model=FoodAffectCondition)

class Effect(StructuredNode):
    name = StringProperty(unique_index=True)
    # type = {advantages, disadvantages}
    type = StringProperty()
    foods = RelationshipFrom('Food', 'HAS', model=FoodHasEffect)    

# pregnant and breastfeeding women
# babies and young children
# kids and teens
# adults
# older adults.
class ConsumerGroup(StructuredNode):
    name = StringProperty(unique_index=True)
    name_vi = StringProperty()
    foods = RelationshipFrom('Food', 'AFFECT', model=FoodAffectConsumerGroup)