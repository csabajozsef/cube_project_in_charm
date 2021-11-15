def adjust_color_middle_to_face(c,color,facekar):
    # kell az hogy hol van az a color amit keresünk
    # keresünk egy sarkot/élet ahol van a szín, ennek a cubieát - ezt beadjuk a cube_method_did_cubie_move
    # ha mozog, tudjuk melyik oldalon van pl R, utána addig forgatjuk a kockát amígy a jó oldalon nem mozog
    # ha ez teljesül akkor done
