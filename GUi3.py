import pandas as pd
import sys
from tkinter import *
from tkinter import ttk
import FinalFile as F
F.obj.Data()
root = Tk()
root.title("Main Window")
root.geometry('1920x1080')


class GUI:


    def GeneralEnteries(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        root.title("Main Window")
        View= Button(root,
                              text="View",
                              width=20,
                              padx=40,
                              pady=10,
                              bg='brown',
                              fg='white',
                              command=B.GeneralEnteriesView).place(x=100, y=100)
        mainloop()

    def GeneralEnteriesView(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        (F.obj.GeneralEnteries())
        mainloop()


    def Ledger(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()

        Generalleger = Button(root,
                              text="GeneralEntryLedger",
                              width=20,
                              padx=40,
                              pady=10,
                              bg='brown',
                              fg='white',
                              command=B.GeneralLedger).place(x=100, y=100)

        Adjustedleger = Button(root,
                              text="AdjustedEntryLedger",
                              width=20,
                              padx=40,
                              pady=10,
                              bg='brown',
                              fg='white',
                              command=B.AjdustedLedger).place(x=100, y=170)

        Closingleger = Button(root,
                              text="ClosingLedger",
                              width=20,
                              padx=40,
                              pady=10,
                              bg='brown',
                              fg='white',
                              command=B.ClosingLedger).place(x=100, y=240)

        mainloop()


    def GeneralLedger(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        (F.obj.Allledger())
        mainloop()

    def AjdustedLedger(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        (F.obj.AdAllLedgers())
        mainloop()

    def ClosingLedger(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        (F.obj.AdAllledger())
        (F.obj.InSumLedger())
        mainloop()

    def TrialBalance(self):
        root1 = Tk()
        t1 = Text(root1)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        (F.obj.TrialBalance())
        mainloop()

    def AdjGeneralEnteries(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        View= Button(root,
                              text="View",
                              width=20,
                              padx=40,
                              pady=10,
                              bg='brown',
                              fg='white',
                              command=B.AdjGeneralEnteriesView).place(x=100, y=100)
        mainloop()

    def AdjGeneralEnteriesView(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        (F.obj.AdGeneralEnteries())
        mainloop()

    def AdjTrialBalance(self):
        root1 = Tk()
        t1 = Text(root1)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        (F.obj.AdTrialBalance())
        mainloop()

    def FinancialStatements(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        IncomeStatement = Button(root,
                              text="IncomeStatement",
                              width=20,
                              padx=40,
                              pady=10,
                              bg='brown',
                              fg='white',
                              command=B.IncomeStatement).place(x=100, y=100)

        OwnerEquityStatement = Button(root,
                              text="Owner'sEquityStatement",
                              width=20,
                              padx=40,
                              pady=10,
                              bg='brown',
                              fg='white',
                              command=B.OwnerEquityStatement).place(x=100, y=170)

        BalanceSheet = Button(root,
                              text="BalanceSheet",
                              width=20,
                              padx=40,
                              pady=10,
                              bg='brown',
                              fg='white',
                              command=B.BalanceSheet).place(x=100, y=240)

        mainloop()

    def IncomeStatement(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()

        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)

        sys.stdout = PrintToT1()
        (F.obj.IncomeStatent())
        mainloop()

    def OwnerEquityStatement(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()

        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)

        sys.stdout = PrintToT1()
        (F.obj.EquityStatement())
        mainloop()

    def BalanceSheet(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()

        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)

        sys.stdout = PrintToT1()
        (F.obj.BalanceSheet())
        mainloop()

    def ClosingEnteries(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        View= Button(root,
                      text="View",
                      width=20,
                      padx=40,
                      pady=10,
                      bg='brown',
                      fg='white',
                      command=B.ClosingEnteriesView).place(x=100, y=100)
        mainloop()

    def ClosingEnteriesView(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        (F.obj.ClosingEntry())
        mainloop()

    def PostClosingTrial(self):
        root = Tk()
        t1 = Text(root)
        t1.pack()
        class PrintToT1(object):
            def write(self, s):
                t1.insert(END, s)
        sys.stdout = PrintToT1()
        (F.obj.ClsTrialBalance())
        mainloop()




label_0 = Label(root,
                text = "Financial Accounting Software",
                width = 40,
                font = ("bold", 20))
label_0.place(x =500, y = 40)

B=GUI()

GenrealEnteries=Button(root,
       text = "General Enteries",
       width = 20,
       padx = 40,
       pady = 10,
       bg = 'brown',
       fg = 'white',
       command=B.GeneralEnteries).place(x = 100, y = 100)

ledger=Button(root,
       text = "Ledger",
       width = 20,
       padx = 40,
       pady = 10,
       bg = 'brown',
       fg = 'white',
       command=B.Ledger).place(x = 100, y = 170)

TrialBalance=Button(root,
       text = "Trial Balance",
       width = 20,
       padx = 40,
       pady = 10,
       bg = 'brown',
       fg = 'white',
       command=B.TrialBalance).place(x = 100, y = 240)

AdjGenrealEnteries=Button(root,
       text = "Adjusted General Enteries",
       width = 20,
       padx = 40,
       pady = 10,
       bg = 'brown',
       fg = 'white',
       command=B.AdjGeneralEnteries).place(x = 100, y = 310)

AdjTrialBalance=Button(root,
       text = "Adjusted Trial Balance",
       width = 20,
       padx = 40,
       pady = 10,
       bg = 'brown',
       fg = 'white',
       command=B.AdjTrialBalance).place(x = 100, y = 380)

FinancialStatements=Button(root,
       text = "Financial Statements",
       width = 20,
       padx = 40,
       pady = 10,
       bg = 'brown',
       fg = 'white',
       command=B.FinancialStatements).place(x = 100, y = 450)

ClosingEnteries=Button(root,
       text = "Closing Enteries",
       width = 20,
       padx = 40,
       pady = 10,
       bg = 'brown',
       fg = 'white',
       command=B.ClosingEnteries).place(x = 100, y = 520)

PostClosingTrial=Button(root,
       text = "Post-Closing Trial Balance",
       width = 20,
       padx = 40,
       pady = 10,
       bg = 'brown',
       fg = 'white',
       command=B.PostClosingTrial).place(x = 100, y = 590)

from tkinter import *
from PIL import ImageTk, Image



img = ImageTk.PhotoImage(Image.open("b.png"))

panel = Label(root, image = img,text="Created By",compound="bottom",font="bold")
panel.place(relx = 0.9, x =1, y = 550, anchor = NE)



root.mainloop()
