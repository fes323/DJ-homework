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
    if recipe == 'omlet':
        servings = int(request.GET.get('servings', 1))
        context = {
            'recipe': {
                'яйца, шт': 2 * servings,
                'молоко, л': 0.1 * servings,
                'соль, ч.л.': 0.5 * servings,
            },
        }
    if recipe == 'pasta':
        context = {
            'recipe': {
                'макароны, г': 0.3 * servings,
                'сыр, г': 0.05 * servings,
            },
        }
    if recipe == 'buter':
        servings = int(request.GET.get('servings', 1))
        context = {
            'recipe': {
                'хлеб, ломтик': 1 * servings,
                'колбаса, ломтик': 1 * servings,
                'сыр, ломтик': 1 * servings,
                'помидор, ломтик': 1 * servings,
            },
        }
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
