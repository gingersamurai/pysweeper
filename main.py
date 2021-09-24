mode = int(input("выберите режим. Введие число от 1 до 3:"))
if mode == 1:
    bomb_cnt = int(input("введите количество мин:"))
    # gen
elif mode == 2:
    str_cnt = int(input("введите длину поля:"))
    row_cnt = int(input("введите ширину поля"))
    bomb_cnt = int(input("введите количество бомб:"))
    # gen
elif mode == 3:
    str_cnt = int(input("введите длину поля:"))
    row_cnt = int(input("введите ширину поля"))
    bomb_cnt = int(input("введите количество бомб:"))
    # activate bot
else:
    print("вы ввели не то число. Попробуйте снова через 24 часа.")