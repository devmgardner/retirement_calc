#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Apr 24, 2023 04:41:17 PM EDT  platform: Windows NT

import os, sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

class calc_window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("1280x768+370+156")
        top.minsize(1280, 768)
        top.maxsize(1920, 1080)
        top.resizable(0,  0)
        top.title("Retirement Calculator")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        # defining the menu bar and menu option
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
        self.sub_menu = tk.Menu(self.menubar,
                activebackground='#ececec',
                activeborderwidth=1,
                activeforeground='#000000',
                background='#d9d9d9',
                borderwidth=1,
                disabledforeground='#a3a3a3',
                foreground='#000000',
                tearoff=0)
        self.menubar.add_cascade(label='Reports',menu=self.sub_menu,)
        self.sub_menu.add_command(label='Save Report')
        #
        #
        #
        #
        # defining the main frame to hold all the data
        self.data_frame = tk.Frame(self.top)
        self.data_frame.place(relx=0.01, rely=0.008, relheight=0.976, relwidth=0.76)
        self.data_frame.configure(relief='groove')
        self.data_frame.configure(borderwidth="2")
        self.data_frame.configure(relief="groove")
        self.data_frame.configure(background="#d9d9d9")
        self.data_frame.configure(highlightbackground="#d9d9d9")
        self.data_frame.configure(highlightcolor="black")
        # placeholder widgets for first year calculation #
        self.year1_401k_text = tk.Text(self.data_frame)
        self.year1_401k_text.place(x=10, y=10, height=25, relwidth=80)
        self.year1_401k_text.configure(background="white")
        self.year1_401k_text.configure(font="TkTextFont")
        self.year1_401k_text.configure(foreground="black")
        self.year1_401k_text.configure(highlightbackground="#d9d9d9")
        self.year1_401k_text.configure(highlightcolor="black")
        self.year1_401k_text.configure(insertbackground="black")
        self.year1_401k_text.configure(selectbackground="#c4c4c4")
        self.year1_401k_text.configure(selectforeground="black")
        self.year1_401k_text.configure(wrap="word")
        #
        self.year1_401k_label = tk.Label(self.data_frame)
        self.year1_401k_label.place(x=100, y=10, height=25, width=35)
        self.year1_401k_label.configure(activebackground="#f9f9f9")
        self.year1_401k_label.configure(anchor='w')
        self.year1_401k_label.configure(background="#d9d9d9")
        self.year1_401k_label.configure(compound='left')
        self.year1_401k_label.configure(disabledforeground="#a3a3a3")
        self.year1_401k_label.configure(foreground="#000000")
        self.year1_401k_label.configure(highlightbackground="#d9d9d9")
        self.year1_401k_label.configure(highlightcolor="black")
        self.year1_401k_label.configure(text='''401k''')
        #
        self.year1_match_text = tk.Text(self.data_frame)
        self.year1_match_text.place(x=140, y=10, height=25, width=65)
        self.year1_match_text.configure(background="white")
        self.year1_match_text.configure(font="TkTextFont")
        self.year1_match_text.configure(foreground="black")
        self.year1_match_text.configure(highlightbackground="#d9d9d9")
        self.year1_match_text.configure(highlightcolor="black")
        self.year1_match_text.configure(insertbackground="black")
        self.year1_match_text.configure(selectbackground="#c4c4c4")
        self.year1_match_text.configure(selectforeground="black")
        self.year1_match_text.configure(wrap="word")
        #
        self.year1_match_label = tk.Label(self.data_frame)
        self.year1_match_label.place(x=215, y=10, height=25, width=50)
        self.year1_match_label.configure(activebackground="#f9f9f9")
        self.year1_match_label.configure(anchor='w')
        self.year1_match_label.configure(background="#d9d9d9")
        self.year1_match_label.configure(compound='left')
        self.year1_match_label.configure(disabledforeground="#a3a3a3")
        self.year1_match_label.configure(foreground="#000000")
        self.year1_match_label.configure(highlightbackground="#d9d9d9")
        self.year1_match_label.configure(highlightcolor="black")
        self.year1_match_label.configure(text='''Match''')
        #
        self.year1_savings_text = tk.Text(self.data_frame)
        self.year1_savings_text.place(x=265, y=10, height=25, width=80)
        self.year1_savings_text.configure(background="white")
        self.year1_savings_text.configure(font="TkTextFont")
        self.year1_savings_text.configure(foreground="black")
        self.year1_savings_text.configure(highlightbackground="#d9d9d9")
        self.year1_savings_text.configure(highlightcolor="black")
        self.year1_savings_text.configure(insertbackground="black")
        self.year1_savings_text.configure(selectbackground="#c4c4c4")
        self.year1_savings_text.configure(selectforeground="black")
        self.year1_savings_text.configure(wrap="word")
        #
        self.year1_savings_label = tk.Label(self.data_frame)
        self.year1_savings_label.place(x=355, y=10, height=25, width=55)
        self.year1_savings_label.configure(activebackground="#f9f9f9")
        self.year1_savings_label.configure(anchor='w')
        self.year1_savings_label.configure(background="#d9d9d9")
        self.year1_savings_label.configure(compound='left')
        self.year1_savings_label.configure(disabledforeground="#a3a3a3")
        self.year1_savings_label.configure(foreground="#000000")
        self.year1_savings_label.configure(highlightbackground="#d9d9d9")
        self.year1_savings_label.configure(highlightcolor="black")
        self.year1_savings_label.configure(text='''Savings''')
        #
        self.year1_total_text = tk.Text(self.data_frame)
        self.year1_total_text.place(x=410, y=10, height=25, width=80)
        self.year1_total_text.configure(background="white")
        self.year1_total_text.configure(font="TkTextFont")
        self.year1_total_text.configure(foreground="black")
        self.year1_total_text.configure(highlightbackground="#d9d9d9")
        self.year1_total_text.configure(highlightcolor="black")
        self.year1_total_text.configure(insertbackground="black")
        self.year1_total_text.configure(selectbackground="#c4c4c4")
        self.year1_total_text.configure(selectforeground="black")
        self.year1_total_text.configure(wrap="word")
        #
        self.year1_total_label = tk.Label(self.data_frame)
        self.year1_total_label.place(x=500, y=10, height=25, width=65)
        self.year1_total_label.configure(activebackground="#f9f9f9")
        self.year1_total_label.configure(anchor='w')
        self.year1_total_label.configure(background="#d9d9d9")
        self.year1_total_label.configure(compound='left')
        self.year1_total_label.configure(disabledforeground="#a3a3a3")
        self.year1_total_label.configure(foreground="#000000")
        self.year1_total_label.configure(highlightbackground="#d9d9d9")
        self.year1_total_label.configure(highlightcolor="black")
        self.year1_total_label.configure(text='''Year Saved''')
        #
        self.year1_full_total_text = tk.Text(self.data_frame)
        self.year1_full_total_text.place(x=575, y=10, height=25, width=80)
        self.year1_full_total_text.configure(background="white")
        self.year1_full_total_text.configure(font="TkTextFont")
        self.year1_full_total_text.configure(foreground="black")
        self.year1_full_total_text.configure(highlightbackground="#d9d9d9")
        self.year1_full_total_text.configure(highlightcolor="black")
        self.year1_full_total_text.configure(insertbackground="black")
        self.year1_full_total_text.configure(selectbackground="#c4c4c4")
        self.year1_full_total_text.configure(selectforeground="black")
        self.year1_full_total_text.configure(wrap="word")
        #
        self.year1_full_total_label = tk.Label(self.data_frame)
        self.year1_full_total_label.place(x=665, y=10, height=25, width=65)
        self.year1_full_total_label.configure(activebackground="#f9f9f9")
        self.year1_full_total_label.configure(anchor='w')
        self.year1_full_total_label.configure(background="#d9d9d9")
        self.year1_full_total_label.configure(compound='left')
        self.year1_full_total_label.configure(disabledforeground="#a3a3a3")
        self.year1_full_total_label.configure(foreground="#000000")
        self.year1_full_total_label.configure(highlightbackground="#d9d9d9")
        self.year1_full_total_label.configure(highlightcolor="black")
        self.year1_full_total_label.configure(text='''Total Saved''')
        #
        self.year1_salary_text = tk.Text(self.data_frame)
        self.year1_salary_text.place(x=740, y=10, height=25, width=80)
        self.year1_salary_text.configure(background="white")
        self.year1_salary_text.configure(font="TkTextFont")
        self.year1_salary_text.configure(foreground="black")
        self.year1_salary_text.configure(highlightbackground="#d9d9d9")
        self.year1_salary_text.configure(highlightcolor="black")
        self.year1_salary_text.configure(insertbackground="black")
        self.year1_salary_text.configure(selectbackground="#c4c4c4")
        self.year1_salary_text.configure(selectforeground="black")
        self.year1_salary_text.configure(wrap="word")
        #
        self.year1_salary_label = tk.Label(self.data_frame)
        self.year1_salary_label.place(x=830, y=10, height=25, width=65)
        self.year1_salary_label.configure(activebackground="#f9f9f9")
        self.year1_salary_label.configure(anchor='w')
        self.year1_salary_label.configure(background="#d9d9d9")
        self.year1_salary_label.configure(compound='left')
        self.year1_salary_label.configure(disabledforeground="#a3a3a3")
        self.year1_salary_label.configure(foreground="#000000")
        self.year1_salary_label.configure(highlightbackground="#d9d9d9")
        self.year1_salary_label.configure(highlightcolor="black")
        self.year1_salary_label.configure(text='''Salary''')
        #
        #
        #
        #
        # defining the entry widgets and buttons
        self.years_entry = tk.Entry(self.top)
        self.years_entry.place(relx=0.775, rely=0.008, height=20, relwidth=0.073)
        self.years_entry.configure(background="white")
        self.years_entry.configure(disabledforeground="#a3a3a3")
        self.years_entry.configure(font="TkFixedFont")
        self.years_entry.configure(foreground="#000000")
        self.years_entry.configure(highlightbackground="#d9d9d9")
        self.years_entry.configure(highlightcolor="black")
        self.years_entry.configure(insertbackground="black")
        self.years_entry.configure(selectbackground="#c4c4c4")
        self.years_entry.configure(selectforeground="black")
        #
        def get_years(self):
            self.years = int(self.years_entry.get())
        #
        self.years_label = tk.Label(self.top)
        self.years_label.place(relx=0.862, rely=0.008, height=19, width=31)
        self.years_label.configure(activebackground="#f9f9f9")
        self.years_label.configure(activeforeground="black")
        self.years_label.configure(background="#d9d9d9")
        self.years_label.configure(disabledforeground="#a3a3a3")
        self.years_label.configure(foreground="#000000")
        self.years_label.configure(highlightbackground="#d9d9d9")
        self.years_label.configure(highlightcolor="black")
        self.years_label.configure(text='''Years''')
        #
        self.years_button = tk.Button(self.top)
        self.years_button.place(relx=0.91, rely=0.008, height=20, width=65)
        self.years_button.configure(activebackground="#ececec")
        self.years_button.configure(activeforeground="#000000")
        self.years_button.configure(background="#d9d9d9")
        self.years_button.configure(disabledforeground="#a3a3a3")
        self.years_button.configure(foreground="#000000")
        self.years_button.configure(highlightbackground="#d9d9d9")
        self.years_button.configure(highlightcolor="black")
        self.years_button.configure(pady="0")
        self.years_button.configure(text='''Update''')
        #
        #
        self.salary_entry = tk.Entry(self.top)
        self.salary_entry.place(relx=0.775, rely=0.054, height=20, relwidth=0.073)
        self.salary_entry.configure(background="white")
        self.salary_entry.configure(disabledforeground="#a3a3a3")
        self.salary_entry.configure(font="TkFixedFont")
        self.salary_entry.configure(foreground="#000000")
        self.salary_entry.configure(highlightbackground="#d9d9d9")
        self.salary_entry.configure(highlightcolor="black")
        self.salary_entry.configure(insertbackground="black")
        self.salary_entry.configure(selectbackground="blue")
        self.salary_entry.configure(selectforeground="white")
        #
        def get_salary(self):
            self.salary = float(self.salary_entry.get())
        #
        self.salary_label = tk.Label(self.top)
        self.salary_label.place(relx=0.862, rely=0.054, height=19, width=35)
        self.salary_label.configure(activebackground="#f9f9f9")
        self.salary_label.configure(activeforeground="black")
        self.salary_label.configure(background="#d9d9d9")
        self.salary_label.configure(disabledforeground="#a3a3a3")
        self.salary_label.configure(foreground="#000000")
        self.salary_label.configure(highlightbackground="#d9d9d9")
        self.salary_label.configure(highlightcolor="black")
        self.salary_label.configure(text='''Salary''')
        #
        self.salary_button = tk.Button(self.top)
        self.salary_button.place(relx=0.91, rely=0.054, height=20, width=65)
        self.salary_button.configure(activebackground="#ececec")
        self.salary_button.configure(activeforeground="#000000")
        self.salary_button.configure(background="#d9d9d9")
        self.salary_button.configure(disabledforeground="#a3a3a3")
        self.salary_button.configure(foreground="#000000")
        self.salary_button.configure(highlightbackground="#d9d9d9")
        self.salary_button.configure(highlightcolor="black")
        self.salary_button.configure(pady="0")
        self.salary_button.configure(text='''Update''')
        #
        self.raise_entry = tk.Entry(self.top)
        self.raise_entry.place(relx=0.775, rely=0.097, height=20, relwidth=0.073)
        self.raise_entry.configure(background="white")
        self.raise_entry.configure(disabledforeground="#a3a3a3")
        self.raise_entry.configure(font="TkFixedFont")
        self.raise_entry.configure(foreground="#000000")
        self.raise_entry.configure(highlightbackground="#d9d9d9")
        self.raise_entry.configure(highlightcolor="black")
        self.raise_entry.configure(insertbackground="black")
        self.raise_entry.configure(selectbackground="blue")
        self.raise_entry.configure(selectforeground="white")
        #
        def get_raise(self):
            self._raise = float(self.raise_entry.get())
        #
        self.raise_label = tk.Label(self.top)
        self.raise_label.place(relx=0.862, rely=0.097, height=19, width=35)
        self.raise_label.configure(activebackground="#f9f9f9")
        self.raise_label.configure(activeforeground="black")
        self.raise_label.configure(background="#d9d9d9")
        self.raise_label.configure(disabledforeground="#a3a3a3")
        self.raise_label.configure(foreground="#000000")
        self.raise_label.configure(highlightbackground="#d9d9d9")
        self.raise_label.configure(highlightcolor="black")
        self.raise_label.configure(text='''Raise''')
        #
        self.raise_button = tk.Button(self.top)
        self.raise_button.place(relx=0.91, rely=0.097, height=20, width=65)
        self.raise_button.configure(activebackground="#ececec")
        self.raise_button.configure(activeforeground="#000000")
        self.raise_button.configure(background="#d9d9d9")
        self.raise_button.configure(disabledforeground="#a3a3a3")
        self.raise_button.configure(foreground="#000000")
        self.raise_button.configure(highlightbackground="#d9d9d9")
        self.raise_button.configure(highlightcolor="black")
        self.raise_button.configure(pady="0")
        self.raise_button.configure(text='''Update''')
        #
        self._401k_entry = tk.Entry(self.top)
        self._401k_entry.place(relx=0.775, rely=0.141, height=20, relwidth=0.073)
        self._401k_entry.configure(background="white")
        self._401k_entry.configure(disabledforeground="#a3a3a3")
        self._401k_entry.configure(font="TkFixedFont")
        self._401k_entry.configure(foreground="#000000")
        self._401k_entry.configure(highlightbackground="#d9d9d9")
        self._401k_entry.configure(highlightcolor="black")
        self._401k_entry.configure(insertbackground="black")
        self._401k_entry.configure(selectbackground="blue")
        self._401k_entry.configure(selectforeground="white")
        #
        def get_401k(self):
            self._401k = float(self._401k_entry.get())
        #
        self._401k_label = tk.Label(self.top)
        self._401k_label.place(relx=0.862, rely=0.141, height=18, width=35)
        self._401k_label.configure(activebackground="#f9f9f9")
        self._401k_label.configure(activeforeground="black")
        self._401k_label.configure(background="#d9d9d9")
        self._401k_label.configure(disabledforeground="#a3a3a3")
        self._401k_label.configure(foreground="#000000")
        self._401k_label.configure(highlightbackground="#d9d9d9")
        self._401k_label.configure(highlightcolor="black")
        self._401k_label.configure(text='''401k''')
        #
        self._401k_button = tk.Button(self.top)
        self._401k_button.place(relx=0.91, rely=0.141, height=20, width=65)
        self._401k_button.configure(activebackground="#ececec")
        self._401k_button.configure(activeforeground="#000000")
        self._401k_button.configure(background="#d9d9d9")
        self._401k_button.configure(disabledforeground="#a3a3a3")
        self._401k_button.configure(foreground="#000000")
        self._401k_button.configure(highlightbackground="#d9d9d9")
        self._401k_button.configure(highlightcolor="black")
        self._401k_button.configure(pady="0")
        self._401k_button.configure(text='''Update''')
        #
        self.match_entry = tk.Entry(self.top)
        self.match_entry.place(relx=0.775, rely=0.185, height=20, relwidth=0.073)
        self.match_entry.configure(background="white")
        self.match_entry.configure(disabledforeground="#a3a3a3")
        self.match_entry.configure(font="TkFixedFont")
        self.match_entry.configure(foreground="#000000")
        self.match_entry.configure(highlightbackground="#d9d9d9")
        self.match_entry.configure(highlightcolor="black")
        self.match_entry.configure(insertbackground="black")
        self.match_entry.configure(selectbackground="blue")
        self.match_entry.configure(selectforeground="white")
        #
        def get_match(self):
            self.match = float(self.match_entry.get())
        #
        self.match_label = tk.Label(self.top)
        self.match_label.place(relx=0.862, rely=0.185, height=18, width=35)
        self.match_label.configure(activebackground="#f9f9f9")
        self.match_label.configure(activeforeground="black")
        self.match_label.configure(background="#d9d9d9")
        self.match_label.configure(disabledforeground="#a3a3a3")
        self.match_label.configure(foreground="#000000")
        self.match_label.configure(highlightbackground="#d9d9d9")
        self.match_label.configure(highlightcolor="black")
        self.match_label.configure(text='''Match''')
        #
        self.match_button = tk.Button(self.top)
        self.match_button.place(relx=0.91, rely=0.185, height=20, width=65)
        self.match_button.configure(activebackground="#ececec")
        self.match_button.configure(activeforeground="#000000")
        self.match_button.configure(background="#d9d9d9")
        self.match_button.configure(disabledforeground="#a3a3a3")
        self.match_button.configure(foreground="#000000")
        self.match_button.configure(highlightbackground="#d9d9d9")
        self.match_button.configure(highlightcolor="black")
        self.match_button.configure(pady="0")
        self.match_button.configure(text='''Update''')
        #
        self.savings_entry = tk.Entry(self.top)
        self.savings_entry.place(relx=0.775, rely=0.229, height=20, relwidth=0.073)
        self.savings_entry.configure(background="white")
        self.savings_entry.configure(disabledforeground="#a3a3a3")
        self.savings_entry.configure(font="TkFixedFont")
        self.savings_entry.configure(foreground="#000000")
        self.savings_entry.configure(highlightbackground="#d9d9d9")
        self.savings_entry.configure(highlightcolor="black")
        self.savings_entry.configure(insertbackground="black")
        self.savings_entry.configure(selectbackground="blue")
        self.savings_entry.configure(selectforeground="white")
        #
        def get_savings(self):
            self.savings = float(self.savings_entry.get())
        #
        self.savings_label = tk.Label(self.top)
        self.savings_label.place(relx=0.859, rely=0.229, height=19, width=45)
        self.savings_label.configure(activebackground="#f9f9f9")
        self.savings_label.configure(activeforeground="black")
        self.savings_label.configure(background="#d9d9d9")
        self.savings_label.configure(disabledforeground="#a3a3a3")
        self.savings_label.configure(foreground="#000000")
        self.savings_label.configure(highlightbackground="#d9d9d9")
        self.savings_label.configure(highlightcolor="black")
        self.savings_label.configure(text='''Savings''')
        #
        self.savings_button = tk.Button(self.top)
        self.savings_button.place(relx=0.91, rely=0.229, height=20, width=65)
        self.savings_button.configure(activebackground="#ececec")
        self.savings_button.configure(activeforeground="#000000")
        self.savings_button.configure(background="#d9d9d9")
        self.savings_button.configure(disabledforeground="#a3a3a3")
        self.savings_button.configure(foreground="#000000")
        self.savings_button.configure(highlightbackground="#d9d9d9")
        self.savings_button.configure(highlightcolor="black")
        self.savings_button.configure(pady="0")
        self.savings_button.configure(text='''Update''')
        # create command for updating self.data values
        def update_data(self):
            get_years(self)
            get_salary(self)
            get_raise(self)
            get_401k(self)
            get_match(self)
            get_savings(self)
            # print(f'{self.years=}')
            # print(f'{self.salary=}')
            # print(f'{self._raise=}')
            # print(f'{self._401k=}')
            # print(f'{self.match=}')
            # print(f'{self.savings=}')
        # assign command to all buttons
        self.years_button.configure(command=lambda: update_data(self))
        self.salary_button.configure(command=lambda: update_data(self))
        self.raise_button.configure(command=lambda: update_data(self))
        self._401k_button.configure(command=lambda: update_data(self))
        self.match_button.configure(command=lambda: update_data(self))
        self.savings_button.configure(command=lambda: update_data(self))
        # create empty list for rows
        self.rows = []
        # command to create a row of widgets for a year's output
        def create_row(self):
            pass
        def place_widgets(self):
            pass


def start_up():
    support.main()

if __name__ == '__main__':
    support.main()


