a = int(input())
b = int(input())
c = int(input())
d = int(input())
S = 3*(a+b+c+d)
print(S)



print((int(input()) + int(input()) + int(input()) + int(input())) * 3)


print((sum((int(input()) for i in range(4))) * 3))



def purchase_price(cost_of_the_monitor, the_cost_of_the_system_unit, keyboard_cost, mouse_cost):  # функция для расчёта стоимости покупки (трех компьютеров)
    x = (cost_of_the_monitor + the_cost_of_the_system_unit + keyboard_cost + mouse_cost) * 3
    return x

cost_of_the_monitor = int(input())  # стоимость монитора
the_cost_of_the_system_unit = int(input())  # стоимость системного блока
keyboard_cost = int(input())  # стоимость клавиатуры
mouse_cost = int(input())  # стоимость мыши

print(purchase_price(cost_of_the_monitor, the_cost_of_the_system_unit, keyboard_cost, mouse_cost))  # вывод стоимости покупки (трех компьютеров)


nums = 0
for _ in range(4):
    num = int(input())
    nums += num

print(nums * 3)


print(
    sum(
        [int(input()) for _ in range(4)]) * 3
    )


from sys import stdin
print(3 * sum([int(p) for p in stdin]))


print(sum([int(input()) for i in range(4)]*3))


a = [int(input()), int(input()), int(input()), int(input())]
print(sum(a)*3)