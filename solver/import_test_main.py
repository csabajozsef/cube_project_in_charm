from cube_import import *

c=Cube()
print(c)
c.cube_method_all_side_loader()
c.cube_method_mixer("RRUUuurr")
c.cube_method_3d_drawer()

print(c)
c.cube_method_flipper()
# legyen sima cube.method_manual_interact(), ilyenkor tudunk mi játszani vele // not important

# miközben mennek a lépések tudjuk egérrel forgatni? // how tho
# ha stringből olvasunk akkor ne lehessen keyboarddal belekeverni
# a solver methodunk egy stringet rak ki lépésekből és erre meghívja ezt a fgvt
# lehessen léptetni a kirakást, lehessen megállítani, space, nyilak
# sarokban mutathatná mi a lépéssorozat amit mutat és hogy hol jár benne


