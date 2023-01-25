"""
Pete likes to bake some cakes. He has some recipes and ingredients.
Unfortunately he is not good in maths. Can you help him to find out,
how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the
available ingredients (also an object) and returns the maximum
number of cakes Pete can bake (integer). For simplicity there are
no units for the amounts (e.g. 1 lb of flour or 200 g of sugar
are simply 1 or 200). Ingredients that are not present in the objects
, can be considered as 0.

Examples:
# must return 2
cakes(
    {flour: 500, sugar: 200, eggs: 1},
    {flour: 1200, sugar: 1200, eggs: 5, milk: 200}
    )
# must return 0
cakes(
    {apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100},
    {sugar: 500, flour: 2000, milk: 2000}
    )
"""

# MY CODE ARE BOILERPALET EVERYWERE
# def cakes(recipe: dict, available: dict):
#     try:
#         for key in recipe:
#             assert isinstance(key, str)
#             assert isinstance(recipe[key], (int, float))
#         for key in available:
#             assert isinstance(key, str)
#             assert isinstance(available[key], (int, float))
#         if not recipe or not available:
#             return 0
#         if len(recipe) > len(available):
#             return 0
#     except AssertionError:
#         return 0

#     recipe_numbers_list = [*recipe.values()]
#     available_numbers_list = []
#     for items in recipe:
#         available_numbers_list.append(available.get(items))
#     if available_numbers_list == recipe_numbers_list:
#         return 1
#     for ingredient, amount in recipe.items():
#         if ingredient not in available or available[ingredient] < amount:
#             return 0
#     cakes = 0
#     while True:
#         for i in range(len(recipe)):
#             available_numbers_list[i] = available_numbers_list[i] - \
#                 recipe_numbers_list[i]
#             if available_numbers_list[i] < 0:
#                 return cakes
#         cakes += 1


def cakes(recipe, available):
    output = []
    for i in recipe:
        if i not in available:
            return 0
        output.append(available.get(i) // recipe.get(i))
    return min(output)


recipe = {
    "cream": 200,
    "flour": 300,
    "sugar": 150,
    "milk": 100,
    "oil": 100,
}
available = {
    "sugar": 1700,
    "flour": 20000,
    "milk": 20000,
    "oil": 30000,
    "cream": 5000,
    'cream': 1000,
    'oil': 1000,
    'milk': 1000
}
print(cakes(recipe, available))
