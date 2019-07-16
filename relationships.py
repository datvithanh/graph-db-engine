from neomodel import StructuredRel, FloatProperty, StringProperty

class FoodContainsNutrition(StructuredRel):
    amount = FloatProperty()   
    # g mg pound
    metric = StringProperty()

class FoodHasEffect(StructuredRel):
    description = StringProperty()

class FoodAffectCondition(StructuredRel):
    description = StringProperty()

class FoodAffectConsumerGroup(StructuredRel):
    description = StringProperty()