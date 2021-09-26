import field
import random

def game():
    while True:
        # 
        
        # 
        field.print_field()
        nx, ny, act = map(int, input('введите x y act\n').split())
        if(nx == -1):
            field.save(ny)
            continue
        if nx == -2:
            field.load(ny)
            continue
        res = field.make_act(nx, ny, act)
        if not res:
            break
        if field.check_win():
            print("победа")
            break
        field.print_field()
        # 
        res = int(input("""
если желаете сохранить игру, нажмите 1
иначе нажмите 0
"""))
        if res == 1:
            print("уже имеются сохранения:")
            field.show_saves()
            num = int(input("под каким другим номером вы хотите сохраниться?"))
            field.save(num)
            print("сохранено")
        #
       
        
    
    
print("САПЕР (создал ginger.samurai)")
print("""
нажмите 1 чтобы начать новую игру
нажмите 2 чтобы загрузить игру
""")
mode = int(input())
if mode == 1:
    print("""
нажмите 1 чтобы играть на поле 5х5 с 2-5 бомбами
нажмите 2 чтобы настроить размер поля и количество бомб
    """)
    fmode = int(input())
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
    save_num = int(input("выберите сохранение\n"))
    field.load(save_num)
    game()
