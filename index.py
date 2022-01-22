import xlrd

# book = xlrd.open_workbook('./datas/sheet1.xls')
book.sheet_loaded(0)    # 是否被加载
#book.unload_sheet(0)    # 取消加载
# print(book.sheet_loaded(0))

# print(book.sheets()) # 获取工作表
# print(book.sheets()[0])

# print(book.sheet_by_index(0))   #根据索引获取工作表
# print(book.sheet_by_name('Sheet1'))

# print(book.sheet_names())   # 获取工作表的名称
# print(book.nsheets)     # 获取工作表数

sheet=book.sheet_by_index(0)

# print(sheet.nrows)
# print(sheet.row(0))
# print(sheet.row_types(0))
# print(sheet.row(0)[2].value)
# print(sheet.row_values(1))
# print(sheet.row_len(1))

# print(sheet.ncols)
# print(sheet.col(0))
# print(sheet.col_values(0))
# print(sheet.col_types(0))


# print(sheet.cell(1,2))
# print(sheet.cell_type(1,2))
# print(sheet.cell(1,2).ctype)
# print(sheet.cell(1,2).value)
# print(sheet.cell_value(1,2))

