# ДЗ 3-4 работа со словарями
# Создайте список словарей, которые содеражат поля имя, возраст, пол.
# При помощи переменной persons найдите и сохраните в переменных следующую информацию:
# - Колличество всех людей
# - Сколько мужчин, а сколько женщин
# - Посчитайте сколько совершеннолетних персон
# - Список всех имён
# - Отсортированный список всех возрастов без повторений
# - 3 самых встречающихся имён.
# - Вывести все имена мужчин старше 35, имя которых начинается с F

persons = [ {"name": "Marat",   "age" : 10, "gender" : "male"},
            {"name" : "Zlata",  "age" : 30, "gender" : "female"},
            {"name" : "Jon",    "age" : 25, "gender" : "male"},
            {"name" : "Fodor",  "age" : 33, "gender" : "male"},
            {"name" : "Anna",   "age" : 28, "gender" : "female"},
            {"name" : "Andrew", "age" : 35, "gender" : "male"},
            {"name" : "Natali", "age" : 22, "gender" : "female"},
            {"name" : "Ruslan", "age" : 29, "gender" : "male"},
            {"name" : "Anna",   "age" : 21, "gender" : "female"}, 
            {"name" : "Natali", "age" : 26, "gender" : "female"},
            {"name" : "Feofania", "age" : 29, "gender" : "female"},
            {"name" : "Lilia", "age" : 22, "gender" : "female"},
            {"name" : "Feffy",  "age" : 36, "gender" : "male"},
            {"name" : "Fakisima",  "age" : 41, "gender" : "male"},
]

print(persons)
# берём длину списка (количество всех людей)
num_peope = len(persons)
num_male = 0
num_female = 0
num_adult = 0
list_name = []
list_age = []
list_man_35 = []

# пройдёмся по всему списку, вычислим все остальное
for i in range(num_peope):
    print(i,persons[i])
    if persons[i].get("gender") == "male":
        num_male += 1
    else:
        num_female +=1
    if int(persons[i].get("age")) >= 18:
        num_adult += 1
    list_name.append(persons[i].get("name"))
    # TODO: для уникальности возраста нужно проверить если ли элемент уже в списке
    # если его нет - добавлять
    list_age.append(persons[i].get("age"))
    if int(persons[i].get("age")) >= 35 and persons[i].get("gender") == "male":
        str_1 = persons[i].get("name")
        if (str_1[0]=="F" or str_1[0]=="f"):
            list_man_35.append(persons[i].get("name"))


print ("Male:", num_male)
print ("Female:", num_female)
print ("Adult:", num_adult)
print ("List of names:", list_name)
list_age.sort()
print ("List of age:", list_age)
print ("List mane:", list_man_35)