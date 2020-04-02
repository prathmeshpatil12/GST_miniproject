import pandas as pd
import xlsxwriter
import xlrd

def Backend_Cal(lst):
    fmain = pd.ExcelFile("Excel_Files/" + str(lst[0]))
    for s in fmain.sheet_names:  # Traversing the sheets of the main file
        df_main = fmain.parse(s)
        df_main.insert(len(df_main.columns), "CGST", df_main.shape[0] * [0])
        df_main.insert(len(df_main.columns), "SGST/UGST", df_main.shape[0] * [0])
        df_main.insert(len(df_main.columns), "IGST", df_main.shape[0] * [0])
        df_main.insert(len(df_main.columns), "CESS", df_main.shape[0] * [0])

        for file in lst[1:]:  # Traversing all the files except the main file.
            f = pd.ExcelFile("Excel_Files/" + str(file))

            # writer = pd.ExcelWriter("Excel_Files/" + "demo.xlsx")  # str(lst[0]
            for sheet in f.sheet_names:
                df = f.parse(sheet)
                # --------------------- YOUR CODE HERE ---------------------#
                for i in range(len(df)):
                    for j in range(len(df_main)):
                        if str(df_main["GSTIN"][j]) == str(df["GSTIN"][i]):
                            s1 = str(df_main["CGST"][j])
                            m1 = str(df["CGST"][i])
                            df_main["CGST"][j] = s1.replace(',','') + m1.replace(',','')
                            s2 = str(df_main["SGST/UGST"][j])
                            m2 = str(df["SGST/UGST"][i])
                            df_main["SGST/USGT"][j] = int(s2.replace(',','')) + int(m2.replace(',',''))
                            s3 = str(df_main["IGST"][j])
                            m3 = str(df["IGST"][i])
                            df_main["IGST"][j] = int(s3.replace(',','')) + int(m3.replace(',',''))
                            s4 = str(df_main["CGST"][j])
                            m4 = str(df["CGST"][i])
                            df_main["CESS"][j] = int(s4.replace(',','')) + int(m4.replace(',',''))

                # -------------------------- XXX --------------------------#

                # df['CGST'] = df.shape[0]*[0]

                print(df_main)

        # SAVING THE FINAL FILE
        df_main.to_excel("Excel_Files/demo.xlsx", 'sheet1')


# Temperory function call with demo excel files.
l = ['Full_demo.xlsx', 'April_demo.xlsx']
Backend_Cal(l)