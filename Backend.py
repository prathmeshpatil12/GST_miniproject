import pandas as pd
import xlsxwriter

"""
Variables for File: fmain, (Contains the file with all Acesis)
                    f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12 (Contains monthly data)
"""

def Backend_Cal(lst):
    fmain = pd.ExcelFile("Excel_Files/" + str(lst[0]))
    for s in fmain.sheet_names:
        df_main = fmain.parse(s)
        fmain_workbook = xlsxwriter.Workbook("Excel_Files/" + str(lst[0]))
        fmain_Wsheet = fmain_workbook.add_worksheet()
        for file in lst[1:]:
            f = pd.ExcelFile("Excel_Files/" + str(file))
            writer = pd.ExcelWriter("Excel_Files/" + str(lst[0]))
            for sheet in f.sheet_names:
                df = f.parse(sheet)
                print(len(df.columns) )
                print(len(df_main.columns))
                fmain_Wsheet.write(0, len(df.columns)+1 ,'hello')


l = ['Full_demo.xlsx', 'April_demo.xlsx']
Backend_Cal(l)