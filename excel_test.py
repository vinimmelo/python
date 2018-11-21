# Created on 19 November 2018
# @author vinimmelo
# Excel (spreadsheet) control, fill and manipulation.

import openpyxl

caminho = r'C:\Users\brmelovi\Desktop\Pasta1.xlsx'

def excel_test1(path: str):
    wb = openpyxl.load_workbook(path)
    sheet = wb['Planilha1']
    cell = sheet['D2']
    print("Row: "  + str(cell.row) + "\n" + "Column: " + cell.column)
    print("Value: " + cell.value)
    print("Cell " + cell.coordinate + " is: " + cell.value)



if __name__ == '__main__':
    excel_test1(caminho)
