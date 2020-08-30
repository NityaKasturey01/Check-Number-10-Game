from tkinter import *
import tkinter as tk
import random,math
import numpy as np

# Colours of each tile on the basis of number
BACKGROUND_COLOR_CELLS = {1: "#f5f5f5", 2: "#e0f2f8", 3: "#b8dbe5",
                         4: "#71b1bd", 5: "#27819f", 6: "#0073b9",
                         7: "#7fa8d7", 8: "#615ea6", 9: "#2f3490",
                         10: "#1c1691",11:"#22549d",12:"#92549d"}


class Grid_num(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title('Check Number')

        self.grid_cells = []
        self.game_widgets()
        self.init_grid()
        self.init_matrix()
        self.start_grid()
        self.game_widgets()
        self.mainloop()
        
    
    def init_grid(self):
        self.background = Frame(self, bg="#72549d",width=500, height=500,padx=40,pady=40)
        self.background.grid()
        
        for i in range(6):
            grid_row = []
            for j in range(10):
                self.cell = Frame(self.background, bg="#9e948a",
                             width=400 / 6,
                             height=400 / 6)
                self.cell.grid(row=i, column=j, padx=10,
                          pady=10)
                t = Label(master=self.cell, text="",
                          bg="#9e948a",
                          justify=CENTER, font=("Verdana", 20, "bold"), width=4, height=2)
                t.grid()
                grid_row.append(t)

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
        
    def game_widgets(self):
        self.buttonframe = tk.Frame(self)
        self.buttonframe.grid(row=1, column=0, columnspan=1)
        tk.Label(self.buttonframe, text = "      SCORE:   ",fg="red",font=("Helvetica", 14)).grid(row=1, column=1)
        tk.Label(self.buttonframe, textvariable=2).grid(row=1, column=2)
        tk.Label(self.buttonframe, text = "TIME:   ",fg="red",font=("Helvetica", 14)).grid(row=1, column=3)
        tk.Label(self.buttonframe, textvariable=2).grid(row=1, column=4)  
        tk.Button(self.buttonframe, text = "New Game",font=("Verdana", 12, "bold"),fg="#f5f5f5",bg = "#28b4bd",command=self.start,justify=LEFT).grid(row=1, column=0)
    
    def start(self):
        print("start")
        
    def score(self):
        self.score_num = 3
        
    def Time(self):
        self.time_left = 10
        print(self.time_left)
Start=Grid_num()
