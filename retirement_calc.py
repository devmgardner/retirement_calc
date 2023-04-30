# importing modules for report generation
import os, sys, openpyxl
# importing GUI modules
import customtkinter as tk
from tkinter import Menu
from tkinter.filedialog import asksaveasfilename
import tkinter.ttk as ttk
from tkinter.constants import *
# importing support module
import support
# importing locale module for international currencies
import locale
locale.setlocale(locale.LC_ALL, locale.getlocale())
# setting colors (probably not needed)
_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_compcolor = '#d9d9d9'
_ana1color = '#d9d9d9'
_ana2color = '#ececec'
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 
#
# defining resource_path function for after compile
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(base_path, relative_path)
# defining the main window
class calc_window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        # setting geometry
        top.geometry("1280x768+370+156")
        top.minsize(1280, 768)
        top.maxsize(1920, 1080)
        top.resizable(0,  0)
        top.title("Retirement Calculator")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        # assigning toplevel
        self.top = top
        # defining the menu bar and menu option
        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
        self.sub_menu = Menu(self.menubar,
                activebackground='#ececec',
                activeborderwidth=1,
                activeforeground='#000000',
                background='#d9d9d9',
                borderwidth=1,
                disabledforeground='#a3a3a3',
                foreground='#000000',
                tearoff=0)
        self.menubar.add_cascade(label='Reports',menu=self.sub_menu,)
        # defining a scrollable area to place the frame
        self.canvas = tk.CTkCanvas(self.top)
        self.canvas.place(x=10,y=10,relheight=0.976,relwidth=0.815)
        # defining the data_frame that will house the output data and configuring it
        self.data_frame = tk.CTkFrame(self.canvas)
        self.data_frame.configure(width=1043)
        self.data_frame.configure(height=750)
        self.data_frame_id = self.canvas.create_window(0,0,window=self.data_frame,anchor='nw')
        # defining the entry widgets and buttons
        self.years_entry = tk.CTkEntry(self.top, height=20, width=65)
        self.years_entry.place(relx=0.835, rely=0.008)
        #
        def get_years(self):
            self.years = int(self.years_entry.get())
        #
        self.years_label = tk.CTkLabel(self.top, height=20, width=31, fg_color="black")
        self.years_label.place(relx=0.895, rely=0.008)
        self.years_label.configure(text='''Years''')
        #
        self.years_button = tk.CTkButton(self.top, height=20, width=65)
        self.years_button.place(relx=0.94, rely=0.008)
        self.years_button.configure(text='''Update''')
        #
        #
        self.salary_entry = tk.CTkEntry(self.top, height=20, width=65)
        self.salary_entry.place(relx=0.835, rely=0.054)
        #
        def get_salary(self):
            self.salary = {}
            self.salary[1] = float(self.salary_entry.get())
        #
        self.salary_label = tk.CTkLabel(self.top, height=20, width=35, fg_color="black")
        self.salary_label.place(relx=0.895, rely=0.054)
        self.salary_label.configure(text='''Salary''')
        #
        self.salary_button = tk.CTkButton(self.top, height=20, width=65)
        self.salary_button.place(relx=0.94, rely=0.054)
        self.salary_button.configure(text='''Update''')
        #
        self.raise_entry = tk.CTkEntry(self.top, height=20, width=65)
        self.raise_entry.place(relx=0.835, rely=0.097)
        #
        def get_raise(self):
            self._raise = float(self.raise_entry.get())
        #
        self.raise_label = tk.CTkLabel(self.top, height=20, width=35, fg_color="black")
        self.raise_label.place(relx=0.895, rely=0.097)
        self.raise_label.configure(text='''Raise''')
        #
        self.raise_button = tk.CTkButton(self.top, height=20, width=65)
        self.raise_button.place(relx=0.94, rely=0.097)
        self.raise_button.configure(text='''Update''')
        #
        self._401k_entry = tk.CTkEntry(self.top, height=20, width=65)
        self._401k_entry.place(relx=0.835, rely=0.141)
        #
        def get_401k(self):
            self._401k = float(self._401k_entry.get())
        #
        self._401k_label = tk.CTkLabel(self.top, height=20, width=35, fg_color="black")
        self._401k_label.place(relx=0.895, rely=0.141)
        self._401k_label.configure(text='''401k''')
        #
        self._401k_button = tk.CTkButton(self.top, height=20, width=65)
        self._401k_button.place(relx=0.94, rely=0.141)
        self._401k_button.configure(text='''Update''')
        #
        self.match_entry = tk.CTkEntry(self.top, height=20, width=65)
        self.match_entry.place(relx=0.835, rely=0.185)
        #
        def get_match(self):
            self.match = float(self.match_entry.get())
        #
        self.match_label = tk.CTkLabel(self.top, height=20, width=35, fg_color="black")
        self.match_label.place(relx=0.895, rely=0.185)
        self.match_label.configure(text='''Match''')
        #
        self.match_button = tk.CTkButton(self.top, height=20, width=65)
        self.match_button.place(relx=0.94, rely=0.185)
        self.match_button.configure(text='''Update''')
        #
        self.savings_entry = tk.CTkEntry(self.top, height=20, width=65)
        self.savings_entry.place(relx=0.835, rely=0.229)
        #
        def get_savings(self):
            self.savings = float(self.savings_entry.get())
        #
        self.savings_label = tk.CTkLabel(self.top, height=20, width=45, fg_color="black")
        self.savings_label.place(relx=0.892, rely=0.229)
        self.savings_label.configure(text='''Savings''')
        #
        self.savings_button = tk.CTkButton(self.top, height=20, width=65)
        self.savings_button.place(relx=0.94, rely=0.229)
        self.savings_button.configure(text='''Update''')
        # creating blank list of rows
        self.rows = []
        # setting total savings amount
        self.savings_total = 0
        # creating blank dictionary for storing data for report generation
        self.finances = {}
        # command to create a row of widgets for a year's output
        def create_row(self):
            if len(self.rows) == 0:
                y = 10
            else:
                y = 10 + (len(self.rows)*35)
            # setting year_total for calculation later
            year_total = 0
            # creating a dictionary to return all the new widgets
            new_row = {}
            # saving the y value, don't remember why i originally did this
            new_row['y'] = y
            # creating the widgets and assigning to dictionary to return
            new_401k_label = tk.CTkLabel(self.data_frame, height=25, width=35)
            new_401k_label.place(x=230, y=y)
            new_401k_label.configure(anchor='w')
            new_401k_label.configure(text='''401k''')
            new_row['401k_label'] = new_401k_label
            #
            new_401k_text = tk.CTkTextbox(self.data_frame, height=25, width=85)
            new_401k_text.place(x=270, y=y)
            new_row['401k_text'] = new_401k_text
            #
            new_match_label = tk.CTkLabel(self.data_frame, height=25, width=50)
            new_match_label.place(x=365, y=y)
            new_match_label.configure(anchor='w')
            new_match_label.configure(text='''Match''')
            new_row['match_label'] = new_match_label
            #
            new_match_text = tk.CTkTextbox(self.data_frame, height=25, width=80)
            new_match_text.place(x=415, y=y)
            new_row['match_text'] = new_match_text
            #
            new_savings_label = tk.CTkLabel(self.data_frame, height=25, width=55)
            new_savings_label.place(x=505, y=y)
            new_savings_label.configure(anchor='w')
            new_savings_label.configure(text='''Savings''')
            new_row['savings_label'] = new_savings_label
            #
            new_savings_text = tk.CTkTextbox(self.data_frame, height=25, width=85)
            new_savings_text.place(x=565, y=y)
            new_row['savings_text'] = new_savings_text
            #
            new_total_label = tk.CTkLabel(self.data_frame, height=25, width=65)
            new_total_label.place(x=660, y=y)
            new_total_label.configure(anchor='w')
            new_total_label.configure(text='''Year Saved''')
            new_row['total_label'] = new_total_label
            #
            new_total_text = tk.CTkTextbox(self.data_frame, height=25, width=90)
            new_total_text.place(x=730, y=y)
            new_row['total_text'] = new_total_text
            #
            new_full_total_label = tk.CTkLabel(self.data_frame, height=25, width=65)
            new_full_total_label.place(x=830, y=y)
            new_full_total_label.configure(anchor='w')
            new_full_total_label.configure(text='''Total Saved''')
            new_row['full_total_label'] = new_full_total_label
            #
            new_full_total_text = tk.CTkTextbox(self.data_frame, height=25, width=120)
            new_full_total_text.place(x=900, y=y)
            new_row['full_total_text'] = new_full_total_text
            #
            new_salary_label = tk.CTkLabel(self.data_frame, height=25, width=50)
            new_salary_label.place(x=65, y=y)
            new_salary_label.configure(anchor='w')
            new_salary_label.configure(text='''Salary''')
            new_row['salary_label'] = new_salary_label
            #
            new_salary_text = tk.CTkTextbox(self.data_frame, height=25, width=105)
            new_salary_text.place(x=115, y=y)
            # calculating salary and other values
            new_salary = self.salary[1] * ((1+(self._raise/100))**len(self.rows))
            last_year = max(self.salary.keys())
            # assigning salary to self
            self.salary[last_year+1] = new_salary
            # creating year in self.finances for report generation
            self.finances[len(self.rows)+1] = {}
            self.finances[len(self.rows)+1]['salary'] = locale.currency(new_salary,symbol=True,grouping=True)
            # inserting salary to text widget and disabling
            new_salary_text.insert(INSERT,locale.currency(new_salary,symbol=True,grouping=True))
            new_salary_text.configure(state=DISABLED)
            new_row['salary_text'] = new_salary_text
            # process 401k calculations, update the widget, and update self.finances for this year
            new_401k_amount = self._401k / 100 * self.salary[len(self.rows)+2]
            year_total += new_401k_amount
            new_401k_text.insert(INSERT,locale.currency(new_401k_amount,symbol=True,grouping=True))
            new_401k_text.configure(state=DISABLED)
            self.finances[len(self.rows)+1]['401k'] = locale.currency(new_401k_amount,symbol=True,grouping=True)
            # process 401k match calculations, update the widget, and update self.finances for this year
            new_match_amount = self.match / 100 * self.salary[len(self.rows)+2]
            year_total += new_match_amount
            new_match_text.insert(INSERT,locale.currency(new_match_amount,symbol=True,grouping=True))
            new_match_text.configure(state=DISABLED)
            self.finances[len(self.rows)+1]['match'] = locale.currency(new_match_amount,symbol=True,grouping=True)
            # process savings calculations, update the widget, and update self.finances for this year
            new_savings_amount = self.savings / 100 * self.salary[len(self.rows)+2]
            year_total += new_savings_amount
            new_savings_text.insert(INSERT,locale.currency(new_savings_amount,symbol=True,grouping=True))
            new_savings_text.configure(state=DISABLED)
            self.finances[len(self.rows)+1]['savings'] = locale.currency(new_savings_amount,symbol=True,grouping=True)
            self.finances[len(self.rows)+1]['year'] = locale.currency(year_total,symbol=True,grouping=True)
            # update total savings for this calculation and for self.finances for this year
            self.savings_total += year_total
            self.finances[len(self.rows)+1]['total'] = locale.currency(self.savings_total,symbol=True,grouping=True)
            new_total_text.insert(INSERT,locale.currency(year_total,symbol=True,grouping=True))
            new_total_text.configure(state=DISABLED)
            # update overall savings amount widget
            new_full_total_text.insert(INSERT,locale.currency(self.savings_total,symbol=True,grouping=True))
            new_full_total_text.configure(state=DISABLED)
            # add year number widget for readability
            year_num_label = tk.CTkLabel(self.data_frame, height=25, width=65)
            year_num_label.place(x=0, y=y)
            year_num_label.configure(text=f'''Year {len(self.rows)+1}''')
            new_row['year_num_label'] = year_num_label
            # return the dictionary of new widgets
            return new_row
        # defining a function to actually place the widgets
        def place_widgets(self):
            # check if there are existing rows of widgets, and if so destroy them
            if len(self.rows) > 0:
                for row in self.rows:
                    for item in row.keys():
                        if not item == 'y':
                            row[item].destroy()
            # reinitialize the list of rows
            self.rows = []
            # iterate through the years from the entry field, creating a new row of widgets for each year
            for i in range(self.years):
                self.rows.append(create_row(self))
        # create command for updating self.data values
        def update_data(self):
            # initialize a new self.finances dictionary
            self.finances = {}
            # if there is an existing scrollbar, destroy it
            if hasattr(self,'scrollbar'):
                self.scrollbar.destroy()
            # if there is an existing savings_total value, reinitialize it
            if hasattr(self,'savings_total'):
                self.savings_total = 0
            # get all the entry fields
            get_years(self)
            get_salary(self)
            get_raise(self)
            get_401k(self)
            get_match(self)
            get_savings(self)
            # place the widgets
            place_widgets(self)
            # if there are more than 21 years in the calculation, a scrollbar will be needed to display them all properly
            if self.years > 21:
                # adjust the size of the interior frame
                self.canvas.children['!ctkframe'].configure(height=(10+(self.years*35)))
                # adjust the size of the canvas to match
                self.canvas.configure(height=(10+(self.years*35)))
                # create the vertical scrollbar and pack it in place
                self.scrollbar = tk.CTkScrollbar(self.canvas,orientation='vertical')
                self.scrollbar.pack(side='right',fill='y')
                # configure all the scroll commands so the scrollbar works
                self.canvas.configure(yscrollcommand=self.scrollbar.set)
                self.scrollbar.configure(command=self.canvas.yview)
                self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        # assign command to all buttons
        self.years_button.configure(command=lambda: update_data(self))
        self.salary_button.configure(command=lambda: update_data(self))
        self.raise_button.configure(command=lambda: update_data(self))
        self._401k_button.configure(command=lambda: update_data(self))
        self.match_button.configure(command=lambda: update_data(self))
        self.savings_button.configure(command=lambda: update_data(self))
        # beginning report creation command
        def run_report(self):
            # initialize a new workbook and get the active sheet
            wb = openpyxl.Workbook()
            ws = wb.active
            # assign column headers and apply bold format
            ws['A1'] = 'Year Number'
            ws['A1'].font = openpyxl.styles.Font(bold=True)
            ws['B1'] = 'Salary'
            ws['B1'].font = openpyxl.styles.Font(bold=True)
            ws['C1'] = '401k Contribution'
            ws['C1'].font = openpyxl.styles.Font(bold=True)
            ws['D1'] = 'Employer 401k Match'
            ws['D1'].font = openpyxl.styles.Font(bold=True)
            ws['E1'] = 'Savings Contribution'
            ws['E1'].font = openpyxl.styles.Font(bold=True)
            ws['F1'] = 'Total Saved This Year'
            ws['F1'].font = openpyxl.styles.Font(bold=True)
            ws['G1'] = 'Total Saved Overall'
            ws['G1'].font = openpyxl.styles.Font(bold=True)
            # iterate through self.years, adding 2 to account for python indexing and header row
            for i in range(2,self.years+2):
                # assign all values to their cells
                ws[f'A{i}'] = f'Year {i-1}'
                ws[f'B{i}'] = self.finances[i-1]['salary']
                ws[f'C{i}'] = self.finances[i-1]['401k']
                ws[f'D{i}'] = self.finances[i-1]['match']
                ws[f'E{i}'] = self.finances[i-1]['savings']
                ws[f'F{i}'] = self.finances[i-1]['year']
                ws[f'G{i}'] = self.finances[i-1]['total']
            # create a border style
            medium_border = openpyxl.styles.Border(left=openpyxl.styles.Side(style='thin'), right=openpyxl.styles.Side(style='thin'), top=openpyxl.styles.Side(style='thin'), bottom=openpyxl.styles.Side(style='thin'))
            # iterate through all cells, applying the border
            for row in ws.rows:
                for cell in row:
                    cell.border = medium_border
            # list of columns to iterate
            columns = ['A','B','C','D','E','F','G']
            # iterate through columns, adjusting width as necessary
            for column in columns:
                # get the max value length out of the cells in the column
                new_column_length = max(len(str(cell.value)) for cell in ws[column])
                if new_column_length > 0:
                    # adjust the width to fit all characters with healthy padding
                    ws.column_dimensions[column].width = new_column_length*1.23
            # assign filetypes for filedialog
            filetypes = (
                ('Excel Workbook','*.xlsx'),
            )
            # get a filepath from the user where they want their report saved
            file_path = asksaveasfilename(filetypes=filetypes)
            # save the workbook to that path
            wb.save(f'{resource_path(file_path)}.xlsx')
        # add the command to the menu
        self.sub_menu.add_command(label='Save Report',command=lambda: run_report(self))

def start_up():
    support.main()

if __name__ == '__main__':
    support.main()


