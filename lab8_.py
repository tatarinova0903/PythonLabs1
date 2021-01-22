# # Татаринова ИУ7-14Б
# # Вычисление интегралла методом парабол(Симпсона) и методом Буля

# # Метод парабол(Симпсона)
# def simpsonMethod(a, b, n, eps, function):
#     result = function(a) + function (b)
#     h = (b - a) / (2 * n)
#     i = 1
#     sum4 = sum2 = 0
#     for i in range(1, 2 * n + 1, 2):
#         sum4 += function(a + h * i)
#         sum2 += function(a + h * (i + 1)) 
#     result = function(a) + 4 * sum4 + 2 * sum2 + function(b)
#     return result * h / 3 


# # def simpsonMethod(a, b, n, eps, function):
# #     I1 = eps + 1
# #     I2 = 0
# #     N = n
# #     while abs(I2 - I1) > eps:
# #         I1 = I2
# #         h = (b - a) / N
# #         x = a + h
# #         I2 = function(a) + function(b)
# #         i = 1
# #         while (x < b or abs(x-b) < eps):
# #             if i % 2 == 0:
# #                 I2 += 2 * function(x)
# #             else:
# #                 I2 += 4 * function(x)
# #             x += h
# #             i += 1
# #         I2 = I2 * h / 3
# #         N *= 2
# #     return I2


# # Метод Буля
# def boolMethod(a, b, n, eps, function):
#     result = function(a) * 7 + function(b) * 7
#     h = (b - a) / n
#     x = a + h
#     i = 1
#     while x < b: # or abs(I2 - I1) > eps:
#         if i % 4 == 0:
#             result += 14 * function(x)
#         elif i % 4 == 1 or i % 4 == 3:
#             result += 32 * function(x)
#         else:
#             result += 12 * function(x)
#         x += h
#         i += 1
#     return result * 2 * h / 45 


# def function1(x):
#     return x*x


# n1 = 100
# n2 = 1000
# eps = float(input("Введите точность: "))
# print ("{:^15}{:>7}{:<7d}{:>7}{:<7d}".format("Метод", "n1 = ", n1, "n2 = ", n2))
# print("{:^15}{:^14.10}{:^14.10}".format("Метод парабол", simpsonMethod(1, 4, n1, eps, function1), simpsonMethod(1, 4, n2, eps, function1)))
# print("{:^15}{:^14.10}{:^14.10}".format("Метод Буля", boolMethod(1, 4, n1, eps, function1), boolMethod(1, 4, n1, eps, function1)))

# def Integ(x):
#     return x**3 + x**2 + 8

# def S2n(n, a, b):
#     sum=0
#     h=(b-a)/(2*n)
#     i = 1
#     while i<=(2*n-1):
#         sum+=(3+pow(-1,i+1))*Integ(a+i*h)
#         i += 1
#     return h/3*(Integ(a)+Integ(b)+sum)


# e=0.0001
# n=100
# a=1
# b=4
# print(S2n(4*n,a,b), "  ", S2n(2*n,a,b))
# while abs(S2n(4*n,a,b)-S2n(2*n,a,b))>=e:
#     n*=2
# print("S4n=",S2n(4*n,a,b))


from scipy import integrate

 
func = lambda x: x*x
 
answer = integrate.quad(func, 0, 4)
print(answer[0])