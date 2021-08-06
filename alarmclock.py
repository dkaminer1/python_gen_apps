#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 20:14:37 2021

@author: dkaminer
"""

import tkinter as tk
import time
import webbrowser

'''
display then enter a time, big a random song
'''

class AlarmClock(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
#    def clear_clock(self):
    def create_widgets(self):
        self.coord_dict = {}
        self.name_plate = tk.Label(self, text = "24 Hour Alarm Clock")
        self.name_plate.grid(row = 0, column = 0, columnspan = 4)
        self.hour_one = tk.Label(self, text = '0')
        self.hour_one.grid(row = 2, column =0)
        self.hour_two = tk.Label(self, text = '0')
        self.hour_two.grid(row = 2, column =1)
        self.min_one = tk.Label(self,text = '0')
        self.min_one.grid(row = 2, column =2)
        self.min_two = tk.Label(self,text = '0')
        self.min_two.grid(row = 2, column =3 )
        self.quit = tk.Button(self, text = "Close", command = self.master.destroy)
        self.quit.grid(row = 4, column = 0, columnspan = 2)
        self.start = tk.Button(self, text = "Start",command = self.start_clock)
        self.start.grid(row = 4, column = 2, columnspan = 2)
        self.time_dict= {self.hour_one: [2,0], self.hour_two: [2,1], self.min_one:[2,2], self.min_two: [2,3]}
#        self.alarm_seconds = tk.Label(self, text = '0')
#        self.alarm_seconds.grid(row = 5, column =0, columnspan = 2)
#        self.time_difference = tk.Label(self, text = '0')
#        self.time_difference.grid(row = 5, column = 3, columnspan = 2)
#        self.current_time = tk.Label(self, text = '0')
#        self.current_time.grid(row = 6, column = 0)
           
        
        for i in [1,3]:
            for j in range(4):
                if i == 1:
                    self.up_arrow = tk.Button(self, text = '\u2191', command = lambda cord = [i,j]: self.up_arrow_func(cord))
                    self.up_arrow.grid(row = 1, column = j)
                    
                else:
                    self.down_arrow = tk.Button(self, text = '\u2193', command = lambda cord = [i,j]: self.down_arrow_func(cord))
                    self.down_arrow. grid( row = 3, column = j)
        
                    
                    
    def up_arrow_func(self, cord):
        for cordinates in self.time_dict.values():
            if cordinates == [cord[0]+1,cord[1]] :                
                if self.time_dict[self.hour_one] == cordinates:
                    time_val = int(self.hour_one['text']) + 1
                    self.hour_one['text'] =  (time_val % 3)
                if self.time_dict[self.hour_two] == cordinates:
                    time_val = int(self.hour_two['text']) + 1
                    if self.hour_one['text'] == 2 :
                        self.hour_two['text'] =  (time_val % 5)
                    else :
                        self.hour_two['text'] = time_val % 10
                if self.time_dict[self.min_one] == cordinates:
                    time_val = int(self.min_one['text']) + 1
                    self.min_one['text'] =  (time_val % 6)
                if self.time_dict[self.min_two] == cordinates:
                    time_val = int(self.min_two['text']) + 1
                    self.min_two['text'] =  (time_val % 10)
                else:
                    pass
                
    def down_arrow_func(self,cord):
        for cordinates in self.time_dict.values():
            if cordinates == [cord[0]-1,cord[1]] :                
                if self.time_dict[self.hour_one] == cordinates:
                    time_val = int(self.hour_one['text']) - 1
                    self.hour_one['text'] =  (time_val % 3)
                if self.time_dict[self.hour_two] == cordinates:
                    time_val = int(self.hour_two['text']) - 1
                    if self.hour_one['text'] == 2 :
                        self.hour_two['text'] =  (time_val % 5)
                    else :
                        self.hour_two['text'] = time_val % 10
                if self.time_dict[self.min_one] == cordinates:
                    time_val = int(self.min_one['text']) - 1
                    self.min_one['text'] =  (time_val % 6)
                if self.time_dict[self.min_two] == cordinates:
                    time_val = int(self.min_two['text']) - 1
                    self.min_two['text'] =  (time_val % 10)
                else:
                    pass
    def start_clock(self):
        hours= 3600 * (int(self.hour_one['text'])*10 + int(self.hour_two['text']))
        minutes = 60*(int(self.min_one['text'])*10 + int(self.min_two['text']))
        total_time = hours + minutes
#        self.alarm_seconds['text'] = total_time
        cur_time = time.strftime('%H:%M', time.localtime())
        t_split = cur_time.split(':')
        cur_t_sec = int(t_split[0])*3600 + int(t_split[1])*60
        t_diff = total_time - cur_t_sec
        if t_diff > 0 :
            alarm_time = t_diff
        else:
            alarm_time = t_diff+ 24*3600
        
        while abs(t_diff) > .01:
            cur_time = time.strftime('%H:%M', time.localtime())
            t_split = cur_time.split(':')
            cur_t_sec = int(t_split[0])*3600 + int(t_split[1])*60
            t_diff = total_time - cur_t_sec
        webbrowser.open('https://www.youtube.com/watch?v=RDbvC5I9wtw')
        print('Yay it worked')
        
#       Insert songs here to play after the alarm worked.
root = tk.Tk()
app = AlarmClock(master =root)
#print(root.winfo_children())
app.mainloop()