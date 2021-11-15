from cube_import import *

# legyen sima cube.method_manual_interact(), ilyenkor tudunk mi játszani vele // not important
# miközben mennek a lépések tudjuk egérrel forgatni? // how tho
# ha stringből olvasunk akkor ne lehessen keyboarddal belekeverni
# a solver methodunk egy stringet rak ki lépésekből és erre meghívja ezt a fgvt
# lehessen léptetni a kirakást, lehessen megállítani, space, nyilak
# sarokban mutathatná mi a lépéssorozat amit mutat és hogy hol jár benne



c=Cube()
print(c)
c.cube_method_all_side_loader()
#c.cube_method_mixer("RRUUuurr")

c.dict_of_num_cubie['000'].l[0]=-1
c.dict_of_num_cubie['000'].l[1]=-1
c.dict_of_num_cubie['000'].l[2]=-1

# print("c",c.l[2][0][0])

c.dict_of_num_cubie['010'].l[0]=-1
c.dict_of_num_cubie['010'].l[1]=-1
c.dict_of_num_cubie['010'].l[2]=-1
#c.cube_method_3d_drawer()
#print(c)

c.cube_method_did_cubie_move("R","200")
# print("c",c.l[2][0][0])
