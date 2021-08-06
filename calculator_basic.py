#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 18:58:30 2021

@author: dkaminer
"""

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()   
        
    def set_plain_text(self):
        self.plain_text = ''
        
    def get_plain_text(self):
        return self.plain_text

    def update_text(self, new_text):
        self.plain_text = new_text
        
    def create_widgets(self):
        self.plain_text = ''
        self.display = tk.Button(self, text = '', fg = 'white', bg = 'black')
        self.display.grid(row = 6, column = 0,columnspan = 4)
        for i in range(3):
            for j in range(3):
                self.num_key = tk.Button(self, text = str(3 * i + j +1))
                self.num_key['command'] = lambda num_value = str(3 * i + j +1) : self.add_to_string(num_value)
                self.num_key.grid(row = i,column = j)

        self.zero = tk.Button(self, fg = "red", text = '0',command = lambda: self.add_to_string("0"))
        self.zero.grid(row = 3,column = 1)
        self.times = tk.Button(self, text = "*", command = lambda: self.add_to_string("*"))
        self.times.grid(row = 3, column = 3)
        self.divide = tk.Button(self, text = "/", command = lambda: self.add_to_string("/"))
        self.divide.grid(row = 3, column = 2)
        self.decimal = tk.Button(self, text = ".", command = lambda: self.add_to_string("."))
        self.decimal.grid(row = 3, column = 0)
        self.enter = tk.Button(self, text = "enter", command = lambda: self.enter_key())
        self.enter.grid(row = 4,column = 2, columnspan =2)        
        self.quit = tk.Button(self, text = "QUIT", command = self.master.destroy)
        self.minus = tk.Button(self, text = "-", command = lambda: self.add_to_string("-"))
        self.minus.grid(row = 1, column = 3)
        self.plus = tk.Button(self, text = "+", command = lambda: self.add_to_string("+"))
        self.plus.grid(row = 2, column = 3)
        self.quit.grid(row = 5,column = 2,columnspan =2)
        self.clear = tk.Button(self, text = "C", command = lambda: self.clear_key()).grid(row = 0, column = 3)
    def update(self):
\        self.display['text'] = self.plain_text

    def add_to_string(self,arg):
        new_text = self.plain_text
        new_text += arg
        self.plain_text = new_text        
        self.update()

#        print(new_text)
    def clear_key(self):
        self.plain_text = ''
        self.update()

#        print(self.plain_text)
    def enter_key(self):
        try:
            self.plain_text = str(eval(self.plain_text))
#            print(eval(self.plain_text))
            self.update()

        except SyntaxError:
            print("There was an ERROR")
            self.plain_text = ''
            self.update()

        except ZeroDivisionError:
            print("Divide by Zero ERROR")
            self.plain_text = ''
            self.update()

        
        
root = tk.Tk()
app = Application(master =root)
app.mainloop()

