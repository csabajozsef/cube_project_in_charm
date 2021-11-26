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

def adjust_color_middle_to_face(c, middlecolor, side_to_flip_to, middlesidecolor, middle_side_to_flip_to):
    '''
    input: middle cubie szín, hova akarjuk, middle cubie szín, hova akarjuk
    '''
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
    #print(dict_of_middles) # dictben van a color és a position
    dict_of_middle_sides={'L': [0, 1, 1], 'U': [1, 0, 1], 'F': [1, 1, 0], 'B': [1, 1, 2], 'D': [1, 2, 1], 'R': [2, 1, 1]}
    steps=["y","y","y","y",
           "x","y","y","y","y",
           "x","y","y","y","y",
           "x","y","y","y","y",
           "x","y","y","y","y",
           "x",
           "y",
           "x","y","y","y","y",
           "x","y","y","y","y",
           "x","y","y","y","y",
           "x","y","y","y","y",]
    stepper=0
    while dict_of_middles[middlecolor]!=dict_of_middle_sides[side_to_flip_to] or dict_of_middles[middlesidecolor]!=dict_of_middle_sides[middle_side_to_flip_to]:
        c.cube_method_flipper(steps[stepper])
        list_of_cubie_pos_name_color=c.cube_method_get_cubie_pos_name_color() # aktuális állapot
        # dict_of_middles={} # color : middleactualpos , ha a kért color key re az actual pos == kért hely keyre a kért pos akkor done
        for tup in list_of_cubie_pos_name_color:
            if list(tup[2]).count(-1)==2:
                # print(tup)
                for color in tup[2]:
                    if color!=-1:
                        dict_of_middles[dict_of_num_color[color]]=tup[0]

        print("stepper: ", stepper)
        print((dict_of_middles))
        print("sides: ")
        print(dict_of_middle_sides)
        stepper+=1
        if stepper>=len(steps):
            print("NOOOO")
            break

    if dict_of_middles[middlecolor]==dict_of_middle_sides[side_to_flip_to] and dict_of_middles[middlesidecolor]==dict_of_middle_sides[middle_side_to_flip_to]:
        pass
        # print("TRUE")
    else:
        pass
        # print("NOT TRUE")
    # minden
    # dictben kell addig újrahívni ezt amíg mondjuk red az U nem lesz
    # ez még lehet cube tulajdonságnak tenni

def side_koords(c):
    list_of_cubie_pos_name_color=c.cube_method_get_cubie_pos_name_color()
    for tup in list_of_cubie_pos_name_color:
        if list(tup[2]).count(-1)==1:
            # print(tup)
            str_name=""
            for color in tup[2]:
                if color!=-1:
                    str_name+=dict_of_num_color[color]
            dict_of_sides_col_pos[str_name]=tup[0]

def dict_of_sides_positions_one_color(c,color):
    '''returnöl egy dictet amiben az adott color side-jai vannak színnel kódolva'''
    list_of_cubie_pos_name_color=c.cube_method_get_cubie_pos_name_color()
    dict_of_num_color={1: "R", 2:"Y",3:"W", 4:"B", 5:"O", 6:"G"}
    dict_of_sides_col_pos={}
    for tup in list_of_cubie_pos_name_color:
        if list(tup[2]).count(-1)==1:
            # print(tup)
            str_name=""
            for color in tup[2]:

                if color!=-1:
                    str_name+=dict_of_num_color[color]
            dict_of_sides_col_pos[str_name]=tup[0]
    #print("LOOOOOL: ",dict_of_sides_col_pos) # dictben van a color és a position
    return dict_of_sides_col_pos

def pos_of_side_with_two_color(c,col1,col2):
    '''dict of side pos 2colorral'''
    dict_of_sides_col_pos=dict_of_sides_positions_one_color(c,col1)
    if col1+col2 in dict_of_sides_col_pos.keys():
        side_pos_dict_name=col1+col2
        #print(dict_of_sides_col_pos[col1+col2])
    if col2+col1 in dict_of_sides_col_pos.keys():
        side_pos_dict_name=col2+col1
        #print(dict_of_sides_col_pos[col2+col1])
    return (side_pos_dict_name,dict_of_sides_col_pos[side_pos_dict_name])

def white_cross(c):
    adjust_color_middle_to_face(c,"W","U","G","F")
    # 16 helyen lehet a keresett side

    white_blue_str,white_blue_pos=pos_of_side_with_two_color(c,"W","B")
    print(white_blue_str,white_blue_pos)
    def firs_side_in_cross(c):
        "minden side a helyére aztán forgató algo h orientation meglegyen"
        white_blue_str,white_blue_pos=pos_of_side_with_two_color(c,"W","B")
        if white_blue_pos==[1, 0, 2]:
            return True
        # if white_blue_pos==[]

    firs_side_in_cross(c)

