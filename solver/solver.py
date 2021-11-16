# kellene egy olyan cube_method hogy input : ""
# ,color,facekar
# kell a white közép
# kellenek a közepek
# ezek koordinátái: minden oldalon a középső:1

# az adott pozíción lesz egy string ami a cubie kódja ami ott van
# a dictben ezzel a kóddal érjük el a cubie színeit

# new idea: F-ben tudjuk a fix positiont [1][1][0] itt a cubie.l[2]==F
# van még cubie amire ez igaz?
# addig megy a flip xy amíg ez igaz nem lesz

def adjust_color_middle_to_face(c, middlecolor, side_to_flip_to):
    #c.cube_method_did_cubie_move(facekar)
    list_of_cubie_pos_name_color=c.cube_method_get_cubie_pos_name_color()
    # ebben keresem a közepeket, (ezek amiknek a col ban 2 db -1 és egy col van)
    # ha megvannak elmentem dictben, a colorral együtt
    # ezután forgatom az egész kockát flippel amíg a lekért listában
    # a pos nem az ahova akarom forgatni a kockát
    dict_of_num_color={1: "R", 2:"Y",3:"W", 4:"B", 5:"O", 6:"G"}
    dict_of_color_num={"R":1, "Y":2,"W":3, "B":4, "O":5, "G":6}
    dict_of_middles={}
    for tup in list_of_cubie_pos_name_color:
        if list(tup[2]).count(-1)==2:
            # print(tup)
            for color in tup[2]:
                if color!=-1:
                    dict_of_middles[dict_of_num_color[color]]=tup[0]
    print(dict_of_middles) # dictben van a color és a position
    dict_of_middle_sides={'L': [0, 1, 1], 'U': [1, 0, 1], 'F': [1, 1, 0], 'B': [1, 1, 2], 'D': [1, 2, 1], 'R': [2, 1, 1]}
    steps=["x","x","x","x","y","y","y","y"]
    stepper=0
    while dict_of_middles[middlecolor]!=dict_of_middle_sides[side_to_flip_to]:
        c.cube_method_flipper(steps[stepper])
        list_of_cubie_pos_name_color=c.cube_method_get_cubie_pos_name_color()
        dict_of_middles={}
        for tup in list_of_cubie_pos_name_color:
            if list(tup[2]).count(-1)==2:
                # print(tup)
                for color in tup[2]:
                    if color!=-1:
                        dict_of_middles[dict_of_num_color[color]]=tup[0]


        print("stepper: ", stepper)
        stepper+=1
        if stepper>=len(steps):
            print("NOOOO")
            break

    if dict_of_middles[middlecolor]==dict_of_middle_sides[side_to_flip_to]:
        print("TRUE")
    else:
        print("NOT TRUE")
    # minden
    # dictben kell addig újrahívni ezt amíg mondjuk red az U nem lesz
    # ez még lehet cube tulajdonságnak tenni
