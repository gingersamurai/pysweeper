import random


row_cnt = int()
str_cnt = int()
bomb_cnt = int()
field_user_see = [] 
# 0 close 1 flag 2 used
field_bomb_near = []


def gen(user_row_cnt, user_str_cnt, user_bomb_cnt):
    global row_cnt
    global str_cnt
    global bomb_cnt
    row_cnt = user_row_cnt
    str_cnt = user_str_cnt
    bomb_cnt = user_bomb_cnt
    field_user_see = [[0 for i in range(row_cnt)] for i in range(str_cnt)]


    field_bomb_near = [[0 for i in range(row_cnt)] for i in range(str_cnt)]

def gen_bombs():
    pret = []
    res = []
    for x in range(row_cnt):
        for y in row_cnt(str_cnt):
            pret.append([x, y])
    for _ in range(bomb_cnt):
        res_now = random.choice(pret)
        res.append(res_now)
        pret.append(res)
        pret.pop(pret.index(res_now))
        