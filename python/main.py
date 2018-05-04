#!/usr/bin/python 
# -*- coding:UTF-8 -*-

from Tkinter import *
import random
import numpy as np
import time

class LifeData:
  
  #two consts use in this class
  kDie = 0
  kLive = 1

  def __init__(self, data, size, periodic, live, multiply):
    #self is the obj
    #data is a 2D np.array size*size 
    #periodic is a bool
    #live and multiply both are cell content 2 element
    
    self.size = (size[0]+2, size[1]+2)
    #initialize the data 2D array
    add_cloumn = np.zeros(size[0], int)
    add_row = np.zeros(self.size[1], int)
    data = np.column_stack((data, add_cloumn))
    data = np.column_stack((add_cloumn, data))
    data = np.row_stack((data, add_row))
    data = np.row_stack((add_row, data))
    self.data = data
    
    self.periodic = periodic
    self.live = live
    self.multiply = multiply
    #creat a 2D list for store the data temperary 
    self.temperary_data = np.zeros([self.size[0], self.size[1]], int)
  
  #initialize the 2D list depend on periodic is True or False
  def set_data_periodic(self):
    if self.periodic:
      self.data[0] = self.data[self.size[0]-2]
      self.data[self.size[0]-1] = self.data[1]
      for row_num in range(1,self.size[0]-1):
        self.data[row_num][0] = self.data[row_num][self.size[1]-2]
        self.data[row_num][self.size[1]-1] = self.data[row_num][1]
    else:
      self.data[0] = LifeData.kDie
      self.data[self.size[0]-1] = LifeData.kDie
      for row_num in range(1,self.size[0]-1):
        self.data[row_num][0] = LifeData.kDie
        self.data[row_num][self.size[1]-1] = LifeData.kDie

  #evelution of the life game data
  def evelution(self):
    self.set_data_periodic()
    #start the evelution
    for row_num in range(1, self.size[0]-1):
      for column_num in range(1, self.size[1]-1):
        #count the life number around the element observe 
        element_around = [self.data[row_num-1][column_num-1], 
                          self.data[row_num-1][column_num], 
                          self.data[row_num-1][column_num+1],
                          self.data[row_num][column_num-1],
                          self.data[row_num][column_num+1],
                          self.data[row_num+1][column_num-1],
                          self.data[row_num+1][column_num],
                          self.data[row_num+1][column_num+1]]
        num_neighbor = element_around.count(LifeData.kLive)
        #if this element live before, and will die
        if LifeData.kLive == self.data[row_num][column_num] and \
        (num_neighbor<self.live[0] or num_neighbor>self.live[1]):
          self.temperary_data[row_num][column_num] = LifeData.kDie
        #if this element die before, and will be created again 
        elif LifeData.kDie == self.data[row_num][column_num] and \
        (num_neighbor>=self.multiply[0] and num_neighbor<=self.multiply[1]):
          self.temperary_data[row_num][column_num] = LifeData.kLive
    #for for ..again
    for row_num in range(1, self.size[0]-1):
      for column_num in range(1, self.size[1]-1):
        self.data[row_num][column_num] = self.temperary_data[row_num][column_num]

    return self.data


class LifePlot:
  
  def __init__(self, root, pixel_size, size_window):
    self.pixel_size = pixel_size
    self.root = root
    self.canvas = Canvas(root, bg = 'white')
    self.canvas.pack()
    self.canvas.config(width=size_window[1],height=size_window[0])
    #add the menu bar 
    self.menubar = Menu(root)
    #add the selections in the menu bar
    #game menu
    self.gamemenu = Menu(self.menubar, tearoff = 0)
    self.gamemenu.add_command(label = 'New', command = self.new_one)
    self.gamemenu.add_command(label = 'Quit', command = self.quit_gui)
    self.menubar.add_cascade(label = 'Game', menu = self.gamemenu)

    #help menu
    self.helpmenu = Menu(self.menubar, tearoff = 0)
    self.helpmenu.add_command(label = 'How to Play', command = self.game_info)
    self.helpmenu.add_command(label = 'About...', command = self.author_info)
    self.menubar.add_cascade(label = 'Help', menu = self.helpmenu)
       
  def new_one(self):
    return 

  def quit_gui(self):
    self.root.quit()

  def game_info(self):
    return

  def author_info(self):
    return

  def plot_game(self, data):
    #size of the data --> 2D array
    row_size = len(data)
    column_size = len(data[0])
    size = (row_size, column_size)
    #color option
    color_dict = {LifeData.kDie:'white', LifeData.kLive:'black'}
    #plot core
    self.canvas.delete(ALL)
    for row_num in range(1, size[0]-1):
      for column_num in range(1, size[1]-1):
         self.canvas.create_rectangle(self.pixel_size*(column_num+1), 
                                      self.pixel_size*(row_num+1),
                                      self.pixel_size*(column_num+2), 
                                      self.pixel_size*(row_num+2),
                                      fill=color_dict[data[row_num][column_num]],
                                      outline="black")
    self.canvas.update()
  
  def excution(self, callback):
    self.start_button = Button(self.root,
                               text="Push the Evelution", 
                               font = 'time 15 bold',  
                               command = callback)
    self.start_button.pack()
    

def evelution_callback(data_handle, plot_handle, step_num, sleep_time):
  for cir in range(step_num):
    plot_handle.plot_game(data_handle.evelution())
    #time.sleep(sleep_time)
def center_window(root, width, height):  
  screenwidth = root.winfo_screenwidth()  
  screenheight = root.winfo_screenheight()  
  size = '%dx%d+%d+%d' \
          %(width, 
            height, 
            (screenwidth - width) / 2, 
            (screenheight - height) / 2)    
  root.geometry(size)  

if __name__ == '__main__':
  kPeriodic = True
  kLiveRange = (2,3)
  kMultiplyRange = (3,3)
  kStepNum = 100
  kSleepTime = 0.1 #second
  kPixelSize = 10  #size of one pixel plot
  kButtonSpace = 40

  root = Tk()
  root.title('Life Game')
  
  data = np.loadtxt('.lifedata')

  row_size = len(data)
  column_size = len(data[0])
  size = (row_size, column_size)
  size_window_width = (size[1] + 4) * kPixelSize
  size_window_height = (size[0] + 4) * kPixelSize
  size_window = (size_window_height, size_window_width)

  center_window(root, size_window[1], size_window[0]+kButtonSpace)  

  life_game_data = LifeData(data, size, kPeriodic, kLiveRange, kMultiplyRange)
  life_game_window = LifePlot(root, kPixelSize, size_window)

  life_game_window.plot_game(life_game_data.data)
  life_game_window.excution(lambda:evelution_callback(life_game_data, 
                                               life_game_window, 
                                               kStepNum, 
                                               kSleepTime))
  root.mainloop()