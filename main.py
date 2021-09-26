import field
import random

def game():
    while True:
        print(field.csline)
        field.print_field()
        print(field.csline)
        nx, ny, act = map(int, input('введите x y act\n').split())
        print(field.csline)
        res = field.make_act(nx, ny, act)
        if not res:
            break
        if field.check_win():
            print("победа")
            break
        field.print_field()
        print(field.csline)
        res = int(input("""
если желаете сохранить игру, нажмите 1
иначе нажмите 0
"""))
        print(field.csline)
        if res == 1:
            field.show_saves()
            print(field.csline)
            num = int(input("под каким другим номером вы хотите сохраниться? "))
            field.save(num)
            print("сохранено")
            print(field.csline)
        
       
        
    
print(field.csline)
print("САПЕР (создал ginger.samurai)")
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
    save_num = int(input("выберите сохранение\n"))
    print(field.csline)
    field.load(save_num)
    game()
