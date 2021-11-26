from cube_import import *

# fgv ami végiglépi az első sorra az algot
# fgv ami teszteli h megvan-e
c=Cube()

def first_row_tester(cube,num_of_tests,tester_func,solver):
    pairs_of_string_truth_values=[]
    for testnum in range(num_of_tests):
        cube.cube_method_mixer()
        temp_mix_string=cube.historystring
        cube.historystring=" "
        solver(cube)
        tempstring=cube.historystring
        temptruth=tester_func(cube)
        if temptruth==False:
            pairs_of_string_truth_values.append((temp_mix_string ,tempstring, temptruth))
    print(pairs_of_string_truth_values)

    # bekeverés, eltároljuk a keverés stringet
    # lefutattajuk az első sor kirakást
    # meghívjuk az ellenőrző fgvt
    # beadunk egy stringet 3d drawerbe
#
