# Задача №1


from pprint import pprint

file_name = 'list_recepts.txt'


def cooking(file_name: str) -> dict:
    with open(file_name, encoding='utf-8') as file_obj:
        main_name = ['ingredient_name', 'quantity', 'measure']
        result = {}
        for line in file_obj:
            dish = line.strip()
            foods = []
            amount_ingredients = file_obj.readline()
            for item in range(int(amount_ingredients)):
                food_primary = file_obj.readline()
                food = food_primary.split(" | ")
                ingredient = dict(zip(main_name, food))
                foods.append(ingredient)
            result[dish] = foods
            file_obj.readline()

        return result


cook_book = cooking(file_name)
pprint(cook_book)



# Задача №2


# from pprint import pprint
#
#
# file_name = 'list_recepts.txt'
#
#
# def cooking(file_name: str) -> dict:
#     with open(file_name, encoding='utf-8') as file_obj:
#         main_name = ['ingredient_name', 'quantity', 'measure']
#         result = {}
#         for line in file_obj:
#             dish = line.strip()
#             foods = []
#             amount_ingredients = file_obj.readline()
#             for item in range(int(amount_ingredients)):
#                 food_primary = file_obj.readline()
#                 food = food_primary.split(" | ")
#                 ingredient = dict(zip(main_name, food))
#                 foods.append(ingredient)
#             result[dish] = foods
#             file_obj.readline()
#
#         return result
#
#
# cook_book = cooking(file_name)
#
#
# def get_shop_list_by_dishes(dishes, person_count):
#     order_dishes = []
#     list_of_dishes = []
#     for dish in cook_book:
#         list_of_dishes.append(dish)
#
#
#     for check in list_of_dishes:
#         number = 0
#         count = dishes.count(check)
#         number = +1
#         if count > 0:
#             add = {check : count}
#             order_dishes.append(add)
#
#
#     list_ingrediends = []
#     for dish in order_dishes:
#         for dish_1, amount in dish.items():
#             for current_dish in cook_book:
#                 if current_dish == dish_1:
#                     for ingredient in cook_book[current_dish]:
#                         ingredients_on_dish = {ingredient['ingredient_name']:{'measure' : ingredient['measure'],
#                         'quantity' : int(ingredient['quantity'])* int(amount) *person_count}}
#                         list_ingrediends.append(ingredients_on_dish)
#     pprint(list_ingrediends)
#
#
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# get_shop_list_by_dishes(['Омлет'], 2)
# get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель', 'Запеченный картофель', 'Омлет'], 2)



# Задача №3


# import  os
#
# BASE_PATH = os.getcwd()
#
#
# file_name_1 = '1.txt'
# file_name_2 = '2.txt'
# file_name_3 = '3.txt'
#
#
# file_name = [file_name_1, file_name_2, file_name_3]
#
# list_1 = {}
# all_text = []
#
#
# def files(file_name: str) -> dict:
#     for file in file_name:
#         with open(file, encoding='utf-8') as file_obj:
#             full_path = os.path.join(BASE_PATH, file)
#             name = os.path.basename(full_path)
#             lines = 0
#             for line in file_obj:
#                 lines+=1
#             list_1[lines] = name
#     list_2 = dict(sorted(list_1.items()))
#
#
#     def record_file(file_name):
#         with open(file_name, encoding='utf-8') as file_obj:
#             current_file = file_obj.read()
#             all_text.append(name_of_file)
#             all_text.append(string)
#             all_text.append(current_file)
#
#
#     for string, name_of_file in list_2.items():
#         record_file(name_of_file)
#
#
# files(file_name)
#
#
# file = open(all_text[0], 'w', encoding='utf-8')
# file.close()
# file = open(all_text[0], 'a', encoding='utf-8')
#
# for i in all_text:
#     file.write(str(i) + '\n')



