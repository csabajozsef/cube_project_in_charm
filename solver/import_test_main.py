from cube_import import *
from solver import *
# lehet, hogy kellene egy cubie id mindenkinek mert így pl két egy oldaon szemben lévő él ugyanazt a colort kapja?
# a cubie. l alapján egyértelműek-e a cubiek?
# legyen sima cube.method_manual_interact(), ilyenkor tudunk mi játszani vele // not important
# miközben mennek a lépések tudjuk egérrel forgatni? // how tho
# ha stringből olvasunk akkor ne lehessen keyboarddal belekeverni
# a solver methodunk egy stringet rak ki lépésekből és erre meghívja ezt a fgvt
# sarokban mutathatná mi a lépéssorozat amit mutat és hogy hol jár benne
# drawer string végén ne lépjen ki
# lehessen léptetni a kirakást, lehessen megállítani, space, nyilak
c=Cube()
c.cube_method_all_side_loader()
c.dict_of_num_cubie[c.l[0][0][0]].l[0]=-1
c.dict_of_num_cubie[c.l[0][0][0]].l[1]=-1
c.dict_of_num_cubie[c.l[0][0][0]].l[2]=-1

c.dict_of_num_cubie[c.l[1][0][0]].l[1]=-1

# white_cross(c)
c.cube_method_3d_drawer()
