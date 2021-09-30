print("This is a sample applicaiton")


import xlrd

workbook = xlrd.open_workbook("sample.xls")

firstsheet = workbook.sheet_by_index(0)

# value  = firstsheet.cell_value(1,1)

value = firstsheet.row_values(1)

# value = firstsheet.col_values(1)
# print(value)


# for i in range(firstsheet.nrows):
#     print(firstsheet.cell_value(i, 0))

for i in range(firstsheet.nrows):
    addressvalue = firstsheet.cell_value(i, 2) #address
    print(addressvalue)
    if len(addressvalue) >0:
        print('The value exists')
    else:
        print('The value is  null')
        # trigger a validation

