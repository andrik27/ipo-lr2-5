import math
class_1 = int(input("Введите кол-во учащихся в 1 классе: "))
class_2 = int(input("Введите кол-во учащихся во 2 классе: "))
class_3 = int(input("Введите кол-во учащихся в 3 классе: "))
d1 = math.ceil(class_1 / 2)
d2 = math.ceil(class_2 / 2)
d3 = math.ceil(class_3 / 2)
d = d1 + d2 + d3
print("Нужно купить",d,"парт.")
