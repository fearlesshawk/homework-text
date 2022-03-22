def read_cookbook():

    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingridients = {}
                ingridients = f.readline().strip()
                ingridients['ingredient_name'], ingridients['quantity'], ingridients['measure'] = ingridients.split('|')
                ingridients['quantity'] = int(ingridients['quantity'])
                ing_list.append(ingridients)
            f.readline()
            cook_book[dish_name] = ing_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ing_list = dict()

    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in cook_book:
            for ingridients in cook_book[dish_name]:  # итерируем ингридиенты в блюде
                meas_quan_list = dict()
                if ingridients['ingredient_name'] not in ing_list:
                    meas_quan_list['measure'] = ingridients['measure']
                    meas_quan_list['quantity'] = ingridients['quantity'] * person_count
                    ing_list[ingridients['ingredient_name']] = meas_quan_list
                else:
                    ing_list[ingridients['ingredient_name']]['quantity'] = ing_list[ingridients['ingredient_name']]['quantity'] + ingridients['quantity'] * person_count

    return ing_list


#print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 8))