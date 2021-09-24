import field


def game():
    while True:
        field.print_field()
        nx, ny, act = map(int, input("[x, y, act(1 - flag, 2 - use)]:").split())
        res = field.make_act(nx, ny, act)
        if not res:
            break
    
    

mode = int(input("выберите режим. Введие число от 1 до 3:"))
if mode == 1:
    bomb_cnt = int(input("введите количество мин:"))
    field.gen(5, 5, bomb_cnt)
    field.dbg_print()
    game()
elif mode == 2:
    str_cnt = int(input("введите длину поля:"))
    row_cnt = int(input("введите ширину поля"))
    bomb_cnt = int(input("введите количество бомб:"))
    field.gen(row_cnt, str_cnt, bomb_cnt)
    field.dbg_print()
    game()
elif mode == 3:
    str_cnt = int(input("введите длину поля:"))
    row_cnt = int(input("введите ширину поля"))
    bomb_cnt = int(input("введите количество бомб:"))
    # activate bot
else:
    print("вы ввели не то число. Попробуйте снова через 24 часа.")