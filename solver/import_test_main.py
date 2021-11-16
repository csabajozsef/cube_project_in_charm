from cube_import import *
from solver import *

# lehet, hogy kellene egy cubie id mindenkinek mert így pl két egy oldaon szemben lévő él ugyanazt a colort kapja?
# a cubie. l alapján egyértelműek-e a cubiek?
# legyen sima cube.method_manual_interact(), ilyenkor tudunk mi játszani vele // not important
# miközben mennek a lépések tudjuk egérrel forgatni? // how tho
# ha stringből olvasunk akkor ne lehessen keyboarddal belekeverni
# a solver methodunk egy stringet rak ki lépésekből és erre meghívja ezt a fgvt
# lehessen léptetni a kirakást, lehessen megállítani, space, nyilak
# sarokban mutathatná mi a lépéssorozat amit mutat és hogy hol jár benne

#c.cube_method_3d_drawer()
#print(c)

# c.cube_method_did_cubie_move("R","200")
# print("c",c.l[2][0][0])

c=Cube()
print(c)
c.cube_method_all_side_loader()
#t=c.cube_method_get_cubie_pos_name_color()
#print(t)
#c.cube_method_3d_drawer()
adjust_color_middle_to_face(c)
c.cube_method_flipper("y")
adjust_color_middle_to_face(c)
#c.cube_method_3d_drawer()
