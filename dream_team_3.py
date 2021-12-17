
# # 1 1-балл
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.
#
# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.
#
# class Soldier:
#
#     soldier = 'Ryan'
#
# class Guns(Soldier):
#
#     def __init__(self):
#         self.weopon = 'AK 47'
#         self.s_weopon = 'pistol'
#         self.ammo_1 = 30
#         self.ammo_2 = 7
#
# class Act_of_Shooting(Guns):
#
#     def shoot_AK47(self):
#         times = int(input('Сколько раз выстрельнуть из АК 47?'))
#         for bullet in range(times):
#             print('тиги-тигитиш')
#             self.ammo_1 -= 1
#             while self.ammo_1 == 0:
#                 print('Нету патронов, нужно перезаридить АК 47!')
#                 self.reload_AK47()
#
#     def shoot_pistol(self):
#         times = int(input('Сколько раз выстрельнуть из пистолета?'))
#         for bullet in range(times):
#             print('тиги-тигитиш')
#             self.ammo_2 -= 1
#             while self.ammo_2 == 0:
#                 print('Нету патронов, нужно перезаридить пистолет!')
#                 self.reload_pistol()
#
#     def reload_AK47(self):
#         print('Перезарижаю АК47!!!')
#         self.ammo_1 = 30
#
#     def reload_pistol(self):
#         print('Перезарижаю пистолет!!!')
#         self.ammo_2 = 7
#
# trial = Act_of_Shooting()
# trial.shoot_AK47()
# trial.shoot_pistol()

# # 2
# #Furniture:
# #Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# #Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# #Добавьте в дом три вышеупомянутых предмета мебели.
# #При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.
# class Furniture:
#     def __init__(self,home,area_home):
#         self.home = home
#         self.area_home = area_home
#         self.bedroom = 0
#         self.wardrobe = 0
#         self.table = 0
#     def add_fornutures(self):
#         self.bedroom = 4
#         self.wardrobe = 2
#         self.table = 1.5
#     def output(self):
#         total_area_fornute = self.bedroom + self.wardrobe + self.table
#         left_area = self.area_home - total_area_fornute
#         return self.home, self.area_home, left_area, ['bedroom', 'waedrobe', 'table']
# far1 = Furniture('частный дом',20)
# far1.add_fornutures()
# print(far1.output())
#######################################



# 3
# Students room:
# Реализуйте студенческую комнату с помощью ООП:
#
# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>
#
# class Student:
#     def __init__(self,name,age,language):
#         self.name = name
#         self.age = age
#         self.language = language
#
#     def __str__(self):
#         return f'<name: {self.name}, age: {self.age}, major: {self.language}>'
# student1 = Student('Гарик Харламов',23,'English')
# student2 = Student('Грегорий Лепс',21,'Biology')
# student3 = Student('Иван Ахлабыстин',24,'Physics')
# print(student2)
# print(student1)
# print(student3)

#problem4
# from moneyfmt import Moneyfmt
# alo = Moneyfmt(1234.43456)
# print(alo)
# alo.update(100000.123)
# print(alo)
# repr(alo)

