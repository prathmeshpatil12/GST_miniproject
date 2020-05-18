import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()


def addMainFile():
    mainfile = filedialog.askopenfile(title="Select File",
                                      filetypes=(("Excel Files", "*.xlsx"), ("All Files", "*.*")))
    main_file=str(mainfile)
    main_start_i = main_file.find("'")
    main_end_i = main_file.find("'", main_start_i + 1)
    main_file=main_file[main_start_i+1: main_end_i]
    labels = tk.Label(frame, text="\n\nMain File")
    labels.pack()
    label=tk.Label(frame, text=main_file)
    label.pack()


MonthFileName=[]


def addMonthlyFiles():
    for widget in frame.winfo_children():
        widget.destroy()

    monthlyfile = filedialog.askopenfile(title="Select File", filetypes=(("Excel Files", "*.xlsx"), ("All Files", "*.*")))
    monthly_file = str(monthlyfile)
    start_i=monthly_file.find("'")
    end_i=monthly_file.find("'", start_i+1)
    monthly_file=monthly_file[start_i+1:end_i]
    MonthFileName.append(monthly_file)
    labels = tk.Label(frame, text="Monthly Files")
    labels.pack()
    for file in MonthFileName:
        label = tk.Label(frame, text=file)
        label.pack()


canvas = tk.Canvas(root, height=500, width=750, bg="#619eff")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.75, relheight=0.75, relx=0.1, rely=0.1)

openMonthlyFile = tk.Button(root, text="Open Monthly Files", padx=10, pady=5, fg="white", bg="#9c43fa", command=addMonthlyFiles)
openMonthlyFile.pack()

openMainFile = tk.Button(root, text="Open Main File", padx=10, pady=5, fg="white", bg="#9c43fa", command=addMainFile)
openMainFile.pack()

root.mainloop()