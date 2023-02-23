from pprint import pprint
with open('recipes.txt', encoding='utf-8') as file:
    recipes = {}
    for line in file:
        dish_name = line.strip()
        ingridient_count = int(file.readline())
        dish = []
        for ing in range(ingridient_count):
            ingridient = file.readline().strip()
            ingridient_name, quantity, measure = ingridient.split(' | ')
            dish.append({
                'ingridient_name': ingridient_name,
                'quantity': quantity,
                'measure': measure
            })
        recipes[dish_name] = dish
        file.readline()

print('Список рецептов:')
pprint(recipes, width=100)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    ingridient_list = []
    buffer = 0
    for dish in dishes:
        if dish in recipes:
            for ingridient in recipes[dish]:
                ingridient_list.append(ingridient['ingridient_name'])
                shop_list[ingridient['ingridient_name']] = \
                    {'measure': ingridient['measure'], 'quantity':
                        int(ingridient['quantity']) * person_count}
                buffer = int(ingridient['quantity'])
                if ingridient_list.count(ingridient['ingridient_name']) > 1:
                    shop_list[ingridient['ingridient_name']]['quantity'] = int(ingridient['quantity']) * person_count \
                                                                           + buffer * person_count
    return shop_list


print('\n')
print('Выведем список продуктов:')
pprint(get_shop_list_by_dishes(["Фахитос", "Омлет"], 10))
