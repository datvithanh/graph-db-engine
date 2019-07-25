from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom
from relationships import FoodAffectHealthIssue, FoodAffectConsumerGroup, FoodContainsNutrition, FoodHasEffect

"""
neomodel documentation https://neomodel.readthedocs.io/en/latest/index.html
"""

class Food(StructuredNode):
    name_en = StringProperty(unique_index=True)
    name_vi = StringProperty(unique_index=False)
    nutritions = RelationshipTo('Nutrition', 'CONTAIN', model=FoodContainsNutrition)
    effects = RelationshipTo('Effect', 'HAS', model=FoodHasEffect)
    health_issues = RelationshipTo('HealthIssue', 'AFFECT', model=FoodAffectHealthIssue)
    consumer_groups = RelationshipTo('ConsumerGroup', 'AFFECT', model=FoodAffectConsumerGroup)

class Nutrition(StructuredNode):
    name = StringProperty(unique_index=True)
    foods = RelationshipFrom('Food', 'CONTAIN', model=FoodContainsNutrition)

class HealthIssue(StructuredNode):
    name_en = StringProperty(unique_index=True)
    name_vi = StringProperty()
    foods = RelationshipFrom('Food', 'AFFECT', model=FoodAffectHealthIssue)

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
    name_en = StringProperty(unique_index=True)
    name_vi = StringProperty()
    foods = RelationshipFrom('Food', 'AFFECT', model=FoodAffectConsumerGroup)