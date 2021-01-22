# Определить длины сторон треугольника по заданным целочисленным координатам вершин
# Найти биссектрису, проведенную из наибольшего угла треугольника
# Определить является ли треугольник остроугольным
# Далее ввести координаты 1 точки и определить находится ли она внутри треугольника
# Если находится, то найти расстояние от этой точки до наиболее удаленной стороны или ее продолжения

# Татаринова ИУ7-14Б

from math import sqrt

eps = 1e-7

# Ввод координат вершин
x1, y1 = map (int, input("Введите координаты A: ").split())  # точка А
x2, y2 = map (int, input("Введите координаты B: ").split())  # точка B
x3, y3 = map (int, input("Введите координаты C: ").split())  # точка С


# Уравнения прямых
A1 = y1 - y2                 # для прямой АB
B1 = x2 - x1
C1 = x1 * y2 - x2 * y1
A2 = y2 - y3                 # для прямой BC
B2 = x3 - x2
C2 = x2 * y3 - x3 * y2  
A3 = y3 - y1                 # для прямой CA
B3 = x1 - x3
C3 = x3*y1 - x1*y3


while A1*x3 + B1*y3 + C1 == 0:
      print("Точки лежат на одной прямой")
      x1, y1 = map (int, input("Введите координаты A: ").split())  # точка А
      x2, y2 = map (int, input("Введите координаты B: ").split())  # точка B
      x3, y3 = map (int, input("Введите координаты C: ").split())  # точка С


# Рассчет длин сторон
AB = sqrt((x2 - x1)**2 + (y2 - y1)**2)
BC = sqrt((x3 - x2)**2 + (y3 - y2)**2)
CA = sqrt((x3 - x1)**2 + (y3 - y1)**2)


# Вывод длин сторон
print ("AB = {:3.3g}".format(AB))
print ("BC = {:3.3g}".format(BC))
print ("CA = {:3.3g}".format(CA))


# Поиск максимальной стороны
if (AB > BC or abs(AB - BC) < eps) and (AB > CA or abs(AB - CA) < eps):
      max_side, side2, side3  = AB, BC, CA
elif (BC > AB or abs(BC - AB) < eps) and (BC > CA or abs(BC - CA) < eps):
      max_side, side2, side3 = BC, AB, CA
else:
      max_side, side2, side3 = CA, AB, BC


# Нахождение биссектрисы из наибольшего угла треугольника
P = AB + BC + CA    # периметр треугольника
l = sqrt(side2 * side3 * P *  (P - 2 * max_side)) / (side2 + side3)
print ("Длина биссектрисы к наибольшей стороне =", "{:5.3g}".format(l))


# Является ли треугольник остроугольным
if side2**2 + side3**2 > max_side**2:
      print ("Треугольник остроугольный")
else:
      print ("Треугольник неостроугольный")


# Ввод координат точки D
x0, y0 = map (int, input("Введите координаты D: ").split())

a = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
b = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
c = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)


# Находится ли точка D внутри треугольника
if (a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0):
      print ("Точка внутри треугольника")
      # Поиск  расстояния от точки D до наиболее удаленной стороны или ее продолжения
      r1 = (abs(A1 * x0 + B1 * y0 + C1)) / sqrt(A1**2 + B1**2)
      r2 = (abs(A2 * x0 + B2 * y0 + C2)) / sqrt(A2**2 + B2**2)
      r3 = (abs(A3 * x0 + B3 * y0 + C3)) / sqrt(A3**2 + B3**2)
      max_r = max(r1,r2,r3)
      print ("Расстояние от точки D до наиболее удаленной стороны =", "{:5.3g}".format(max_r))
else:
      print ("Точка вне треугольника")


# Если треугольник неравнобедренный, то какую вершину нужно сдвинуть меньше всего, чтобы
# он стал равнобедренным и на сколько
if abs(AB - BC) < eps or abs(AB - CA) < eps or abs(BC - CA) < eps:
      print ("Треугольник равнобедренный")
else:
      # для вершины А
      # находим координаты середины ВС
      x_m = (x2 + x3) / 2
      y_m = (y2 + y3) / 2
      # уравнение прямой для BC:  A2x + B2y+ C2 = 0
      # составим уравнение прямой перпендикулярной BC и проходящей через середину BC
      if A2 == 0:
            A_perpendicular = 1
            B_perpendicular = 0
            C_perpendicular = - x_m
      elif B2 == 0:
            A_perpendicular = 0
            B_perpendicular = 1
            C_perpendicular = - y_m
      else:
            A_perpendicular = - B2 / A2
            B_perpendicular = 1
            C_perpendicular = - A_perpendicular * x_m - B_perpendicular * y_m
      # составим уравнение прямой параллельной ВC и проходящей через точку A
      C_parallel = -A2 * x1 - B2 * y1
      # найдем коррдинаты (x,y) точки пересечения найденных прямых
      delta = A_perpendicular * B2 - B_perpendicular * A2
      delta1 = -C_perpendicular * B2 + B_perpendicular * C_parallel
      delta2 = -A_perpendicular * C_parallel + C_perpendicular * A2 
      x_for_A = delta1 / delta
      y_for_A = delta2 / delta
      res_for_A = sqrt((x1 - x_for_A)**2 + (y1 - y_for_A)**2)

      # для вершины B
      # находим координаты середины АС
      x_m = (x1 + x3) / 2
      y_m = (y1 + y3) / 2
      # уравнение прямой для AC:  A3x + B3y+ C3 = 0
      # составим уравнение прямой перпендикулярной AC и проходящей через середину AC
      if A3 == 0:
            A_perpendicular = 1
            B_perpendicular = 0
            C_perpendicular = - x_m
      elif B3 == 0:
            A_perpendicular = 0
            B_perpendicular = 1
            C_perpendicular = - y_m
      else:
            A_perpendicular = - B3 / A3
            B_perpendicular = 1
            C_perpendicular = - A_perpendicular * x_m - B_perpendicular * y_m
      # составим уравнение прямой параллельной АC и проходящей через точку B
      C_parallel = -A3 * x2 - B3 * y2
      # найдем коррдинаты (x,y) точки пересечения найденных прямых
      delta = A_perpendicular * B3 - B_perpendicular * A3
      delta1 = -C_perpendicular * B3 + B_perpendicular * C_parallel
      delta2 = -A_perpendicular * C_parallel + C_perpendicular * A3 
      x_for_B = delta1 / delta
      y_for_B = delta2 / delta
      res_for_B = sqrt((x2 - x_for_B)**2 + (y2 - y_for_B)**2)

      # для вершины C
      # находим координаты середины АВ
      x_m = (x1 + x2) / 2
      y_m = (y1 + y2) / 2
      # уравнение прямой для AB:  A1x + B1y+ C1 = 0
      # составим уравнение прямой перпендикулярной AB и проходящей через середину AB
      if A1 == 0:
            A_perpendicular = 1
            B_perpendicular = 0
            C_perpendicular = - x_m
      elif B1 == 0:
            A_perpendicular = 0
            B_perpendicular = 1
            C_perpendicular = - y_m
      else:
            A_perpendicular = - B1 / A1
            B_perpendicular = 1
            C_perpendicular = - A_perpendicular * x_m - B_perpendicular * y_m
      # составим уравнение прямой параллельной АB и проходящей через точку C
      C_parallel = -A1 * x3 - B1 * y3
      # найдем координаты (x,y) точки пересечения найденных прямых
      delta = A_perpendicular * B1 - B_perpendicular * A1
      delta1 = -C_perpendicular * B1 + B_perpendicular * C_parallel
      delta2 = -A_perpendicular * C_parallel + C_perpendicular * A1 
      x_for_C = delta1 / delta
      y_for_C = delta2 / delta
      res_for_C = sqrt((x3 - x_for_C)**2 + (y3 - y_for_C)**2)

      if res_for_A < res_for_B and res_for_A < res_for_C:
            print("Чтобы треугольник стал равнобедренным нужно сдвинуть точку с координатами ({},{}) на ({:3.3g},{:3.3g})".format(x1, y1, x_for_A - x1, y_for_A - y1))
            print("Новые координаты для точки А({:3.3g},{:3.3g})".format(x_for_A, y_for_A))
      elif res_for_B < res_for_C:
            print("Чтобы треугольник стал равнобедренным нужно сдвинуть точку с координатами ({},{}) на ({:3.3g},{:3.3g})".format(x2, y2, x_for_B - x2, y_for_B - y2))
            print("Новые координаты для точки B({:3.3g},{:3.3g})".format(x_for_B, y_for_B))
      else:
            print("Чтобы треугольник стал равнобедренным нужно сдвинуть точку с координатами ({},{}) на ({:3.3g},{:3.3g})".format(x3, y3, x_for_C - x3, y_for_C - y3))
            print("Новые координаты для точки C({:3.3g},{:3.3g})".format(x_for_C, y_for_C))
