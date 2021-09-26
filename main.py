import field
import random

def game():
    while True:
        print(field.csline)
        field.print_field()
        print(field.csline)
        nx, ny, act = input('введите x y act\n').split()
        nx, ny = int(nx) - 1, int(ny) - 1
        print(field.csline)
        if act == 'open':
            act = 2
        elif act == 'flag':
            act = 1
        elif act == 'save':
            field.show_saves()
            print(field.csline)
            num = input("под каким другим названием вы хотите сохраниться? ")
            field.save(num)
            print("сохранено")
            print(field.csline)
            continue
        res = field.make_act(nx, ny, act)
        if not res:
            break
        if field.check_win():
            print("победа")
            break
        # field.print_field()
        # print(field.csline)
            
        
       
        
    
print(field.csline)
print("САПЕР (создал ginger.samurai)")
print("""
управление:
в игре оправляйте команды вида [x y act]
x - номер столбца слева направо начиная с 1
y - номер строки сверху вниз начиная с 1
act - вид действия open: открыть клетку, flag: поставить флаг, save: сохраниться
примеры:    2 3 open открыть клетку на 2 столбце 3 строке
            1 4 flag поставить флаг на 1 столбце 4 строке
            5 6 save сохраниться (первые 2 цифры роли не играют)
""")
print(field.csline)
print("""
нажмите 1 чтобы начать новую игру
нажмите 2 чтобы загрузить игру
""")
print(field.csline)
mode = int(input())
print(field.csline)
if mode == 1:
    print("""
нажмите 1 чтобы играть на поле 5х5 с 2-5 бомбами
нажмите 2 чтобы настроить размер поля и количество бомб
    """)
    fmode = int(input())
    print(field.csline)
    if fmode == 1:
        field.gen(5, 5, random.randint(2, 5))
    elif fmode == 2:
        str_cnt = int(input("введите длину поля:"))
        row_cnt = int(input("введите ширину поля"))
        bomb_cnt = int(input("введите количество бомб:"))
        field.gen(row_cnt, str_cnt, bomb_cnt)
    game()
else:
    field.show_saves()
    print(field.csline)
    save_num = input("выберите сохранение\n")
    print(field.csline)
    field.load(save_num)
    game()
