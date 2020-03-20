import pandas as pd
import xlsxwriter

"""
Variables for File: fmain, (Contains the file with all Acesis)
                    f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12 (Contains monthly data)
"""

def Backend_Cal(lst):
    fmain = pd.ExcelFile("Excel_Files/" + str(lst[0]))
    for s in fmain.sheet_names:   # Traversing the sheets of the main file
        df_main = fmain.parse(s)
        for file in lst[1:]:  # Traversing all the files except the main file.
            f = pd.ExcelFile("Excel_Files/" + str(file))

            #writer = pd.ExcelWriter("Excel_Files/" + "demo.xlsx")  # str(lst[0]
            for sheet in f.sheet_names:
                df = f.parse(sheet)



                #--------------------- YOUR CODE HERE ---------------------#






                """
                    for i in range(len(df):
                        df['CSGT'][i] --> will print the value in that particular row
                
                """






                # -------------------------- XXX --------------------------#




                df_main.insert(len(df_main.columns), "CGST", df_main.shape[0] * [0])
                df_main.insert(len(df_main.columns), "SGST/UGST", df_main.shape[0] * [0])
                df_main.insert(len(df_main.columns), "IGST", df_main.shape[0] * [0])
                df_main.insert(len(df_main.columns), "CESS", df_main.shape[0] * [0])


                #df['CGST'] = df.shape[0]*[0]

                print(df_main)

        # SAVING THE FINAL FILE
        df_main.to_excel("Excel_Files/demo.xlsx", 'sheet1')

# Temperory function call with demo excel files.
l = ['Full_demo.xlsx', 'April_demo.xlsx']
Backend_Cal(l)