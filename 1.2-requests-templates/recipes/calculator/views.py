from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe_book(request, recipe):
    servings = int(request.GET.get('servings', 1))

    data_recipe = DATA.get(recipe)  # находим нужный словарь внутри словаря

    new_list = []
    for i in data_recipe.values():  # умножаем список значений на количество персон, добавляем в новый список
        data = servings * i
        new_list.append(data)

    key_list = []
    for i in data_recipe:  # создаем список значений
        key_list.append(i)

    data_context = dict(zip(key_list, new_list))  # создаем временный словарь с новыми значениями

    context = {
        'recipe': data_context
    }
    return render(request, 'calculator/index.html', context)
