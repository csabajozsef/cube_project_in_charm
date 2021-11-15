
import random
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Cubie:

    def __init__(self,x=[-1,-1,-1]): # x y z irányban a színek
        self.l=np.array(x)

    def RL(self):
        # print("t")
        # füzetben ábra, z küröl forgatás, azaz első index helyén marad, másik 2 csere
        # kérdés az, hogy ez lehet-e jó reprezentáció cubiera? él, sarok forgatás vizualizáció úgy, hogy
        # a hiányzó színek -1 esek?
        self.l
        self.l[[1,2]]=self.l[[2,1]]  # x körüli forgatás, ez az R és L is, R' L' is

    def UD(self):
      self.l
      self.l[[0,2]]=self.l[[2,0]]

    def FB(self):
      self.l
      self.l[[0,1]]=self.l[[1,0]]

    def __str__(self):
        return str(self.l)

class Cube:

    def __init__(self,x=[[[str(k)+str(j)+str(i) for i in range(3)] for j in range(3)]for k in range(3)]): # ide kell immutabel inicializálás, fix tárhely miatt
        self.l=np.array(x) #itt ha self.l=x volt akkor az a mindegyiknél létrejövő x=np.array([[[]]]) re mutatott?
        self.dict_of_num_cubie={}
        self.dict_of_cubie_num={}

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    self.dict_of_num_cubie[str(i)+str(j)+str(k)]=Cubie()

    def __str__(self):
        return str(self.l)

    def X_to_Y(self): #a numpy array-t átkonvertálja X szerinti rétegződésből Y szerinti rétegződésbe

      self.l[0,[0,2],:]=self.l[0,[2,0], :]
      self.l[[0,2], 0, :]=self.l[[2,0], 0, :]
      self.l[0,[0,1],:]=self.l[0,[1,0], :]
      self.l[[0,1], 0, :]=self.l[[1,0], 0, :]
      self.l[0,[0,2],:]=self.l[0,[2,0], :]
      self.l[0,[1,2],:]=self.l[0,[2,1], :]
      self.l[2,[0,1],:]=self.l[2,[1,0], :]
      self.l[1,[0,2],:]=self.l[1,[2,0], :]
      self.l[[1,2], 0, :]=self.l[[2,1], 0, :]
      self.l[1,[0,2],:]=self.l[1,[2,0], :]
      self.l[2,[0,1],:]=self.l[2,[1,0], :]

    def Y_to_X(self): #a numpy array-t átkonvertálja Y szerinti rétegződésből X szerinti rétegződésbe

      self.l[0,[0,1],:]=self.l[0,[1,0],:]
      self.l[[0,1],0,:]=self.l[[1,0], 0,:]
      self.l[0,[0,1],:]=self.l[0,[1,0],:]
      self.l[0,[0,2],:]=self.l[0,[2,0],:]
      self.l[[0,2],0,:]=self.l[[2,0],0,:]
      self.l[0,[0,2],:]=self.l[0,[2,0],:]
      self.l[1,[0,2],:]=self.l[1,[2,0],:]
      self.l[2,[0,1],:]=self.l[2,[1,0],:]
      self.l[[1,2],0,:]=self.l[[2,1],0,:]
      self.l[2,[0,1],:]=self.l[2,[1,0],:]
      self.l[1,[0,2],:]=self.l[1,[2,0],:]

    def X_to_Z(self): #a numpy array-t átkonvertálja X szerinti rétegződésből Z szerinti rétegződésbe

      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[[0,2],:,0]=self.l[[2,0],:,0]
      self.l[0,:,[0,1]]=self.l[0,:,[1,0]]
      self.l[[0,1], :, 0]=self.l[[1,0],:, 0]
      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[0,:,[1,2]]=self.l[0,:,[2,1]]
      self.l[2,:,[0,1]]=self.l[2,:,[1,0]]
      self.l[1,:,[0,2]]=self.l[1,:,[2,0]]
      self.l[[1,2],:, 0]=self.l[[2,1],:,0]
      self.l[1,:,[0,2]]=self.l[1,:,[2,0]]
      self.l[2,:,[0,1]]=self.l[2,:,[1,0]]

    def Z_to_X(self): #a numpy array-t átkonvertálja Z szerinti rétegződésből X szerinti rétegződésbe

      self.l[0,:,[0,1]]=self.l[0,:,[1,0]]
      self.l[[0,1],:,0]=self.l[[1,0],:,0]
      self.l[0,:,[0,1]]=self.l[0,:,[1,0]]
      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[[0,2],:,0]=self.l[[2,0],:,0]
      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[1,:,[0,2]]=self.l[1,:,[2,0]]
      self.l[2,:,[0,1]]=self.l[2,:,[1,0]]
      self.l[[1,2],:,0]=self.l[[2,1],:,0]
      self.l[2,:,[0,1]]=self.l[2,:,[1,0]]
      self.l[1,:,[0,2]]=self.l[1,:,[2,0]]

    def converter(to_what,self): #swtich
        pass

    def R(self): # x y z koordináták, z=0 front, x=2 right

        for i in self.l[2,:,:]:
            for j in i:
                #print(j)
                self.dict_of_num_cubie[j].RL() # minden forgatott cubie saját helyzetét is megváltoztatja

        self.l[2,:,:]=self.l[2,:,:].transpose() # jobbra forg T aztán oszlopcsere
        self.l[2,:,[0,2]]=self.l[2,:,[2,0]]

    def L(self):

        for i in self.l[0,:,:]:
            for j in i:
                #print(j)
                self.dict_of_num_cubie[j].RL() # minden forgatott cubie saját helyzetét is megváltoztatja

        self.l[0,:,:]=self.l[0,:,:].transpose() # jobbra forg T aztán oszlopcsere
        self.l[0,:,[2,0]]=self.l[0,:,[0,2]]

    def U(self):

      self.X_to_Y()

      for i in self.l[0,:,:]:
            for j in i:
                #print(j)
                self.dict_of_num_cubie[j].UD()

      self.l[0,:,:]=self.l[0,:,:].transpose() # jobbra forg T aztán oszlopcsere
      self.l[0,:,[2,0]]=self.l[0,:,[0,2]]

      self.Y_to_X()

    def D(self):

      self.X_to_Y()

      for i in self.l[2,:,:]:
            for j in i:
                #print(j)
                self.dict_of_num_cubie[j].UD()

      self.l[2,:,:]=self.l[2,:,:].transpose() # jobbra forg T aztán oszlopcsere
      self.l[2,:,[0,2]]=self.l[2,:,[2,0]]

      self.Y_to_X()

    def F(self):

      self.X_to_Z()

      for i in self.l[0,:,:]:
            for j in i:
                #print(j)
                self.dict_of_num_cubie[j].FB()

      self.l[0,:,:]=self.l[0,:,:].transpose() # jobbra forg T aztán oszlopcsere
      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]

      self.Z_to_X()

    def B(self):

      self.X_to_Z()

      for i in self.l[2,:,:]:
            for j in i:
                #print(j)
                self.dict_of_num_cubie[j].FB()

      self.l[2,:,:]=self.l[2,:,:].transpose() # jobbra forg T aztán oszlopcsere
      self.l[2,:,[2,0]]=self.l[2,:,[0,2]]

      self.Z_to_X()

    def R_r(self):

      for i in range(3):
        self.R()

    def L_r(self):

      for i in range(3):
        self.L()

    def U_r(self):

      for i in range(3):
        self.U()

    def D_r(self):

      for i in range(3):
        self.D()

    def F_r(self):

      for i in range(3):
        self.F()

    def B_r(self):

      for i in range(3):
        self.B()

    def cube_method_mixer(self,steps=20):
    # ebbe jöhet stringsorozat vagy szám
      if type(steps)==int:
          for i in range(steps):
            a=random.randint(1,12)
            if a==1:
              self.R()
            if a==2:
              self.L()
            if a==3:
              self.U()
            if a==4:
              self.D()
            if a==5:
              self.F()
            if a==6:
              self.B()
            if a==7:
              self.R_r()
            if a==8:
              self.L_r()
            if a==9:
              self.U_r()
            if a==10:
              self.D_r()
            if a==11:
              self.F_r()
            if a==12:
              self.B_r()
      else:
          for current_step_string in steps:
            if current_step_string=="R":
                self.R()
            if current_step_string=="L":
                self.L()
            if current_step_string=="U":
                self.U()
            if current_step_string=="D":
                self.D()
            if current_step_string=="F":
                self.F()
            if current_step_string=="B":
                self.B()
            if current_step_string=="r":
                self.R()
            if current_step_string=="l":
                self.L()
            if current_step_string=="u":
                self.U()
            if current_step_string=="d":
                self.D()
            if current_step_string=="f":
                self.F()
            if current_step_string=="b":
                self.B()

    def cube_method_all_side_loader(self,string="".join(["W"*9,"Y"*9,"O"*9,"G"*9,"R"*9,"B"*9])):
        # alapállapotba betölti a kockát
        sorrend="UDLFRB"
        sides=[
        self.l[:,0,:], # U 3 W
        self.l[:,2,:], # D 2 Y
        self.l[0,:,:], # L 5 O
        self.l[:,:,0], # F 6 G
        self.l[2,:,:], # R 1 R
        self.l[:,:,2], # B 4 B
        ]

        tuples_of_strings=[]
        counter_of_sides=0
        for i in range(0,len(string),9):
            print(string[i:i+9])
            tuples_of_strings.append((string[i:i+9],sorrend[counter_of_sides],sides[counter_of_sides]))
            counter_of_sides+=1
            print(tuples_of_strings)
            # minde 3 koord lehet 0 1 2 ez 3*3*3 aza 27 koord amik a cubiek
            # oldalak:x - 0:: , 2::
            #    z- ::0 ::2

        dict_of_num_color={1: "R", 2:"Y",3:"W", 4:"B", 5:"O", 6:"G"}
        dict_of_color_num={"R":1, "Y":2,"W":3, "B":4, "O":5, "G":6}

        index=0

        for i in sides: #
            ninestring=tuples_of_strings[index][0]
            print(ninestring)
            #index+=1
            # i a sor
            #print(i)
            stringindex=0
            for j in i:
                for k in j:
                # j az elem
                    #print(k)
                    #print(cube.dict_of_num_cubie[j])
                    if tuples_of_strings[index][1]=="U" or tuples_of_strings[index][1]=="D":
                        self.dict_of_num_cubie[k].l[1]=dict_of_color_num[ninestring[stringindex]] # 0 mert a cubie 0.eleme az x koord,
                    if tuples_of_strings[index][1]=="R" or tuples_of_strings[index][1]=="L":
                        self.dict_of_num_cubie[k].l[0]=dict_of_color_num[ninestring[stringindex]] # 0 mert a cubie 0.eleme az x koord,
                    if tuples_of_strings[index][1]=="F" or tuples_of_strings[index][1]=="B":
                        self.dict_of_num_cubie[k].l[2]=dict_of_color_num[ninestring[stringindex]] # 0 mert a cubie 0.eleme az x koord,

                    print(self.dict_of_num_cubie[k])
                    #cube.dict_of_num_cubie[j].L()
                    #print(cube.dict_of_num_cubie[j])
                    stringindex+=1
            index+=1
            #print(dict_of_num_cubie[j])

    def vertices_of_all_cubies_maker(self):
        # listát gyárt a 3d kiíratáshoz, ezt saját self.vertices_of_all_cubies attr-ba menti
        counter=0
        list_of_touples=[]

        for i in self.l[:,:,:]: # x=2 re nézzük= R oldal
            # i a sor
            for j in i:
                # j az elem
                for k in j:
                    list_of_touples.append((counter,self.dict_of_num_cubie[k].l))
                    counter+=1


        vertices= (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
            )

        vertices16=tuple([tuple([vertex[0]+2,vertex[1]+2,vertex[2]-2])for vertex in vertices ])
        vertices25=tuple([tuple([vertex[0]+2,vertex[1]+2,vertex[2]])for vertex in vertices ])
        vertices21=tuple([tuple([vertex[0]+2,vertex[1]+2,vertex[2]+2])for vertex in vertices ])

        vertices10=tuple([tuple([vertex[0]+2,vertex[1],vertex[2]-2])for vertex in vertices ])
        vertices5=tuple([tuple([vertex[0]+2,vertex[1],vertex[2]])for vertex in vertices ])
        vertices27=tuple([tuple([vertex[0]+2,vertex[1],vertex[2]+2])for vertex in vertices ])

        vertices14=tuple([tuple([vertex[0]+2,vertex[1]-2,vertex[2]-2])for vertex in vertices ])
        vertices8=tuple([tuple([vertex[0]+2,vertex[1]-2,vertex[2]])for vertex in vertices ])
        vertices15=tuple([tuple([vertex[0]+2,vertex[1]-2,vertex[2]+2])for vertex in vertices ])

        # ez az x[0] az x[:::] sorrendben

        vertices23=tuple([tuple([vertex[0],vertex[1]+2,vertex[2]-2])for vertex in vertices ])
        vertices3=tuple([tuple([vertex[0],vertex[1]+2,vertex[2]])for vertex in vertices ])
        vertices12=tuple([tuple([vertex[0],vertex[1]+2,vertex[2]+2])for vertex in vertices ])

        vertices7=tuple([tuple([vertex[0],vertex[1],vertex[2]-2])for vertex in vertices ])
        #vertices
        vertices4=tuple([tuple([vertex[0],vertex[1],vertex[2]+2])for vertex in vertices ])

        vertices9=tuple([tuple([vertex[0],vertex[1]-2,vertex[2]-2])for vertex in vertices ])
        vertices6=tuple([tuple([vertex[0],vertex[1]-2,vertex[2]])for vertex in vertices ])
        vertices26=tuple([tuple([vertex[0],vertex[1]-2,vertex[2]+2])for vertex in vertices ])

        # ez az x[1] az x[:::] sorrendben

        vertices19=tuple([tuple([vertex[0]-2,vertex[1]+2,vertex[2]-2])for vertex in vertices ])
        vertices11=tuple([tuple([vertex[0]-2,vertex[1]+2,vertex[2]])for vertex in vertices ])
        vertices18=tuple([tuple([vertex[0]-2,vertex[1]+2,vertex[2]+2])for vertex in vertices ])

        vertices24=tuple([tuple([vertex[0]-2,vertex[1],vertex[2]-2])for vertex in vertices ])
        vertices2=tuple([tuple([vertex[0]-2,vertex[1],vertex[2]])for vertex in vertices ])
        vertices13=tuple([tuple([vertex[0]-2,vertex[1],vertex[2]+2])for vertex in vertices ])

        vertices17=tuple([tuple([vertex[0]-2,vertex[1]-2,vertex[2]-2])for vertex in vertices ])
        vertices22=tuple([tuple([vertex[0]-2,vertex[1]-2,vertex[2]])for vertex in vertices ])
        vertices20=tuple([tuple([vertex[0]-2,vertex[1]-2,vertex[2]+2])for vertex in vertices ])

        self.vertices_of_all_cubies=[vertices16,
                                vertices25,
                                vertices21,

                                vertices10,
                                vertices5,
                                vertices27,

                                vertices14,
                                vertices8,
                                vertices15,

                                vertices23,
                                vertices3,
                                vertices12,

                                vertices7,
                                vertices,
                                vertices4,

                                vertices9,
                                vertices6,
                                vertices26,

                                vertices19,
                                vertices11,
                                vertices18,

                                vertices24,
                                vertices2,
                                vertices13,

                                vertices17,
                                vertices22,
                                vertices20

                               ]

    def Cube_3d(self,verticesl,colornumsl):

        edges = ((0,1),
         (0,3),
         (0,4),
         (2,1),
         (2,3),
         (2,7),
         (6,3),
         (6,4),
         (6,7),
         (5,1),
         (5,4),
         (5,7))

        surfaces = ((3, 2, 7, 6), #xyz xyz
                    (1, 5, 7, 2),
                    (0, 1, 2, 3),

                    (4, 5, 1, 0),
                    (4, 0, 3, 6),
                    (6, 7, 5, 4),)

        dict_of_num_color={1: "R", 2:"Y",3:"W", 4:"B", 5:"O", 6:"G"}
        dict_of_color_num={"R":1, "Y":2,"W":3, "B":4, "O":5, "G":6}
        dict_of_colornum_rbg={1: (256, 0, 0), 2:(256, 256, 0),3:(256, 256, 256), 4:(0, 0, 256), 5:(0, 0, 0), 6:(0, 256, 0)}

        colors = ((1, 0, 0), # red
                  (0, 1, 0), # green
                  (252, 173, 3), #orange
                  (1, 1, 0), #yellow
                  (256, 256, 256), # white
                  (0, 0, 1)) # blue

        glBegin(GL_QUADS)

        cnum=2
        for surface in surfaces:
            cnum+=1
            cnum=cnum%3

            for vertex in surface:

                if colornumsl[cnum] in dict_of_colornum_rbg.keys():
                    glColor3fv(dict_of_colornum_rbg[colornumsl[cnum]])
                else:

                    glColor3fv((252,0,210))
                glVertex3fv(verticesl[vertex])

        glEnd()

        glBegin(GL_LINES) # line-drawing code
        for edge in edges:
            for vertex in edge:
                glVertex3fv(verticesl[vertex]) # sorban a pontok minden élre
        glEnd()

    def cube_method_3d_drawer(self,string_of_steps=None):
        pygame.init()
        display = (800,600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
        glTranslatef(0.0,0.0, -20) # z irábyan -5 move a kamerának, hogy lássuk a kockát
        glRotatef(25, 2, 1, 0)

        steps_current_pos=0 # ennek majd meg kell írni hogy ha out of range a string_of_stepsben akkor csak =None és csá, tovább megy a loop simán
        while True:

            if string_of_steps!=None:
                # kell egy léptető a nyilakkal
                pygame.time.wait(500)
                current_step_string=string_of_steps[steps_current_pos]
                if current_step_string=="R":
                    self.R()
                if current_step_string=="L":
                    self.L()
                if current_step_string=="U":
                    self.U()
                if current_step_string=="D":
                    self.D()
                if current_step_string=="F":
                    self.F()
                if current_step_string=="B":
                    self.B()
                if current_step_string=="r":
                    self.R_r()
                if current_step_string=="l":
                    self.L_r()
                if current_step_string=="u":
                    self.U_r()
                if current_step_string=="d":
                    self.D_r()
                if current_step_string=="f":
                    self.F_r()
                if current_step_string=="b":
                    self.B_r()
                pygame.time.wait(1000)
                steps_current_pos+=1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("quit")
                    pygame.display.quit()

                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    #pygame.time.Clock.tick(120)
                    # UDLFRB
                    if event.key == pygame.K_x:
                        self.cube_method_flipper("x")
                    if event.key == pygame.K_y:
                        self.cube_method_flipper("y")
                    if event.key == pygame.K_u:
                        self.U()
                    if event.key == pygame.K_d:
                        self.D()
                    if event.key == pygame.K_f:
                        self.F()
                    if event.key == pygame.K_b:
                        self.B()
                    if event.key == pygame.K_l:
                        self.L()
                    if event.key == pygame.K_r:
                        self.R()

                    if event.key == pygame.K_SPACE:
                        pygame.quit()
                    if event.key == pygame.K_LEFT:
                        glTranslatef(-0.5,0,0)
                    if event.key == pygame.K_RIGHT:
                        glTranslatef(0.5,0,0)

                    if event.key == pygame.K_UP:
                        glTranslatef(0,1,0)
                    if event.key == pygame.K_DOWN:
                        glTranslatef(0,-1,0)
                if event.type == pygame.MOUSEMOTION:
                    mouseMove = pygame.mouse.get_rel()
                    #glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)
                    glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)
                    #glRotatef(1.0, mouseMove[1]*0.1, 1.0, 0.0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0,0,1.0)

                    if event.button == 5:
                        glTranslatef(0,0,-1.0)


            #glRotatef(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # clear

            glEnable (GL_DEPTH_TEST)
            num_of_colors=6

            counter=0
            list_of_touples=[]

            for i in self.l[:,:,:]: # x=2 re nézzük= R oldal
                # i a sor
                for j in i:
                    # j az elem
                    for k in j:
                        list_of_touples.append((counter,self.dict_of_num_cubie[k].l))
                        counter+=1

            self.vertices_of_all_cubies_maker()

            for tup in list_of_touples:
                vertices=self.vertices_of_all_cubies[tup[0]]
                chosen_tree=tup[1]
                self.Cube_3d(vertices,chosen_tree)

            pygame.display.flip() # updates the display
            pygame.time.wait(10) # wait?

        self.cube_method_3d_drawer()
        #test

    def cube_method_flipper(self,dir_of_flip="x"):
        if dir_of_flip=="x":
            # def R(self): # x y z koordináták, z=0 front, x=2 right
            for i in self.l[:,:,:]:
                print(i)
                for j in i:
                    print(j)
                    for k in j:
                        print(k)
                        self.dict_of_num_cubie[k].RL() # minden forgatott cubie saját helyzetét is megváltoztatja

            self.l[2,:,:]=self.l[2,:,:].transpose() # jobbra forg T aztán oszlopcsere
            self.l[2,:,[0,2]]=self.l[2,:,[2,0]]

            self.l[1,:,:]=self.l[1,:,:].transpose() # jobbra forg T aztán oszlopcsere
            self.l[1,:,[0,2]]=self.l[1,:,[2,0]]

            self.l[0,:,:]=self.l[0,:,:].transpose() # jobbra forg T aztán oszlopcsere
            self.l[0,:,[0,2]]=self.l[0,:,[2,0]]

        if dir_of_flip=="y":
            # def R(self): # x y z koordináták, z=0 front, x=2 right
            for i in self.l[:,:,:]:
                print(i)
                for j in i:
                    print(j)
                    for k in j:
                        print(k)
                        self.dict_of_num_cubie[k].UD() # minden forgatott cubie saját helyzetét is megváltoztatja

            self.l[:,2,:]=self.l[:,2,:].transpose() # jobbra forg T aztán oszlopcsere
            self.l[:,2,[0,2]]=self.l[:,2,[2,0]]

            self.l[:,1,:]=self.l[:,1,:].transpose() # jobbra forg T aztán oszlopcsere
            self.l[:,1,[0,2]]=self.l[:,1,[2,0]]

            self.l[:,0,:]=self.l[:,0,:].transpose() # jobbra forg T aztán oszlopcsere
            self.l[:,0,[0,2]]=self.l[:,0,[2,0]]

    def cube_method_one_char_to_move(self,current_step_string):
        if current_step_string=="R":
            self.R()
        if current_step_string=="L":
            self.L()
        if current_step_string=="U":
            self.U()
        if current_step_string=="D":
            self.D()
        if current_step_string=="F":
            self.F()
        if current_step_string=="B":
            self.B()
        if current_step_string=="r":
            self.R_r()
        if current_step_string=="l":
            self.L_r()
        if current_step_string=="u":
            self.U_r()
        if current_step_string=="d":
            self.D_r()
        if current_step_string=="f":
            self.F_r()
        if current_step_string=="b":
            self.B_r()

    def cube_method_did_cubie_move(self,current_step_string,cubieposnum):

        did_it_turn=False

        koord1=int(cubieposnum[0])
        koord2=int(cubieposnum[1])
        koord3=int(cubieposnum[2])

        temp=self.l[koord1][koord2][koord3]

        self.cube_method_one_char_to_move(current_step_string)

        if self.dict_of_num_cubie[cubieposnum].l!=temp:
            print('MOZDULT')
            did_it_turn=True
            self.cube_method_one_char_to_move(current_step_string)
            self.cube_method_one_char_to_move(current_step_string)
            self.cube_method_one_char_to_move(current_step_string)

        else:
            print('Nomove')

        return did_it_turn


    def
