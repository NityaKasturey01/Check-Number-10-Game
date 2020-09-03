
from tkinter import *
import tkinter as tk
import random
import numpy as np


# Colours of each button on the basis of number on it
BACKGROUND_COLOR_CELLS = {1: "#f5f5f5", 2: "#e0f2f8", 3: "#b8dbe5",
                         4: "#71b1bd", 5: "#27819f", 6: "#0073b9",
                         7: "#7fa8d7", 8: "#615ea6", 9: "#2f3490",
                         10: "#1c1691"}


class Grid_num(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title('Check Number')
        self.l = list(range(1,11))
        
        self.grid_cells = []
        self.background = Frame(self, bg="#72549d",width=600, height=400,padx=400,pady=200)
        self.rootframe = tk.Frame(self,width=200, height=200,padx=200,pady=200)

        self.buttonframe = tk.Frame(self)
        self.buttonframe.grid(row=1, column=0, columnspan=1)
        self.background.grid()
        self.start()
        self.rnum=0
        self.list_comb=[]
        self.sub=[]
        self.gindex=[]
        self.allinone=[]

    def tileselect(self,event):
        """Selection of tiles on the basis of random number"""
        x=event.widget._coords[0]
        y=event.widget._coords[1]
        
        #checking for the element exist in the list
        if self.matrix[x][y] not in self.list_comb: 
            if self.matrix[x][y]==self.rnum:
                self.list_comb.append(self.matrix[x][y])
                self.matrix[x][y]=0
                self.grid_cells[x][y].configure(text=" ", bg="red")
                self.score+=1
                self.scorel.config(text = "NUMBER: "+str(self.score))

            else:
                
                #chacking for the last element in the list and pairing them sum  
                self.sub.append(self.matrix[x][y])
                self.gindex.append([x,y])
                len_sub=len(self.sub)
                len_ind=len(self.gindex)

                if len_sub==1:
                    print(" ")
                    
                elif (self.sub[len_sub-1]+self.sub[len_sub-2])==self.rnum:
                    self.list_comb.append(self.sub[len_sub-1])
                    self.list_comb.append(self.sub[len_sub-2])
                    self.score+=2
                    self.scorel.config(text = "NUMBER: "+str(self.score))

                    x1=self.gindex[len(self.gindex)-1][0]
                    y1=self.gindex[len(self.gindex)-1][1]
                    x2=self.gindex[len(self.gindex)-2][0]
                    y2=self.gindex[len(self.gindex)-2][1]
                    self.matrix[x1][y1]=0
                    self.matrix[x2][y2]=0
                    self.grid_cells[x1][y1].configure(text=" ", bg="red")
                    self.grid_cells[x2][y2].configure(text=" ", bg="red")
                    
                    
        else:
            print("")
        self.allinone.append(self.list_comb)    
    
    def init_grid(self):
        self.grid_cells = []
        self.background = Frame(self, bg="#72549d",width=500, height=500,padx=30,pady=30)
        self.background.grid()
        
        for i in range(6):
            grid_row = []
            for j in range(10):
                self.cell = Frame(self.background, bg="#9e948a",
                             width=500 / 6,
                             height=500 / 10)
                self.cell.grid(row=i, column=j, padx=5,
                          pady=5)
                self.t = Button(master=self.cell, text="",
                          bg="#9e948a",
                          justify=CENTER, font=("Verdana", 20, "bold"), width=4, height=2)
                self.t._coords = i, j
                self.t.grid()
                grid_row.append(self.t)

            self.grid_cells.append(grid_row)
    
    def init_matrix(self):
        
        self.matrix = []
        for i in range(6):
            self.matrix.append([]) 
            for j in range(10):
                self.matrix[i].append(0)
        self.num=np.random.choice(10,60,p=[0.181,0.169,0.15,0.134,0.117,0.084,0.066,0.05,0.033,0.016])
        
        self.matrix=np.reshape(self.num,(6,10))
        for i in range(6):
            for j in range(10):
                self.matrix[i][j]+=1
        
                    
    def start_grid(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                new_number = self.matrix[i][j]
                self.grid_cells[i][j].configure(text=str(new_number), bg=BACKGROUND_COLOR_CELLS[new_number])
        self.update_idletasks() 
     
    def countdown(self):       
        if self.timeleft > 0: 
            self.timeleft -= 1
            self.timeLabel.config(text = "Time left: "+str(self.timeleft)) 
            self.timeLabel.after(1000, self.countdown)

    def random_num(self):
        if len(self.l)==0:
            print("Game over!! Check your score")
        else:
            
            random.shuffle(self.l)
            self.rnum=self.l[0]
            self.l.remove(self.l[0])
            self.numLabel.config(text = "NUMBER: "+str(self.rnum))
            self.list_comb.clear()
            self.timeLabel.after(10000, self.random_num)

    
    def game_widgets(self):
        self.buttonframe = tk.Frame(self)
        self.buttonframe.grid(row=1, column=0, columnspan=1)
        

        self.scorel=tk.Label(self.buttonframe, text = "      SCORE: "+str(self.score),fg="red",font=("Helvetica", 14))
        self.scorel.grid(row=1, column=5)
        self.timeLabel=tk.Label(self.buttonframe, text = "Time left: " +
              str(self.timeleft), font = ('Helvetica', 12))
        self.timeLabel.grid(row=1, column=4)
        self.numLabel=tk.Label(self.buttonframe, text = "NUMBER: " +
              str(self.rnum), font = ('Helvetica', 12))
        self.numLabel.grid(row=1, column=1)
        
        if self.timeleft==100:
            self.countdown()
        self.random_num()
        
        #tk.Button(self.buttonframe, text = "New Game",font=("Verdana", 12, "bold"),fg="#f5f5f5",bg = "#28b4bd",command=self.startgame,justify=RIGHT).grid(row=1, column=10)
        tk.Button(self.buttonframe, text = "INSTRUCTIONS",font=("Verdana", 12, "bold"),fg="#f5f5f5",bg = "#72549d",command=self.instruction,justify=RIGHT).grid(row=1, column=12)
        tk.Button(self.buttonframe, text = "MENU",font=("Verdana", 12, "bold"),fg="#f5f5f5",bg = "#9e948a",command=self.start,justify=RIGHT).grid(row=1, column=14)

    def start(self):
        """Menu page of the game where user will have two options"""
        self.rootframe.destroy()
        self.background.destroy()
        self.buttonframe.destroy()
        self.rootframe = tk.Frame(self)
        self.rootframe.grid(row=1, column=0, columnspan=1)
        tk.Label(self.rootframe, text = "CHECK NUMBERS",bg="#72549d",width=80, height=25,padx=1,pady=1,fg="white",font=("Helvetica", 14)).grid(row=1, column=2)
        tk.Button(self.rootframe, text = "Start Game",font=("Verdana", 12, "bold"),fg="#f5f5f5",bg = "#28b4bd",command=self.startgame,justify=RIGHT).grid(row=2, column=1)
        tk.Button(self.rootframe, text = "INSTRUCTIONS",font=("Verdana", 12, "bold"),fg="#f5f5f5",bg = "#72549d",command=self.instruction,justify=RIGHT).grid(row=2, column=3)
              
    def startgame(self):
        """Start the game with orginal grid by generating new number and started time"""
        self.score=0
        self.rootframe.destroy()
        self.background.destroy()
        self.timeleft=100
        self.game_widgets()
        self.init_grid()
        self.init_matrix()
        self.start_grid()
        for i in range(6):
             for j in range(10):
                 self.grid_cells[i][j].bind("<Button-1>",self.tileselect)


    def instruction(self):
        """Instructions display on the frame when clicked"""
        #destroy the existing frames
        self.rootframe.destroy()
        self.background.destroy()
        self.rootframe = tk.Frame(self,width=200, height=200,padx=100,pady=200)
        self.rootframe.grid(row=1, column=0, columnspan=1)
        tk.Button(self.rootframe, text = "MENU",font=("Verdana", 12, "bold"),fg="#f5f5f5",bg = "#9e948a",command=self.start).grid(row=0, column=0)
        tk.Button(self.rootframe, text = "Start Game",font=("Verdana", 12, "bold"),fg="#f5f5f5",bg = "#28b4bd",command=self.startgame).grid(row=0, column=1)
        tk.Label(self.rootframe, text = "\nINSTRUCTIONS",fg="red",font=("Helvetica", 14)).grid(row=3, column=0)
        lb=tk.Label(self.rootframe, text = "\n1. Look at the random number and time left \n "
                    "2. Select pair of numbers whose sum will be equal to random number \n"
                    "3. You can also select the random number as well which is present in the grid\n"
                    "4. Each random number will arise after every 10 sec\n"
                    "5. You need to select as mush as tiles as possible and increase your score\n"
                    "READY   START THE GAME!!",font=("Helvetica", 14))
        lb.grid(row=4,column=0)
        

                   
if __name__=="__main__":
    Start=Grid_num()
    mainloop()