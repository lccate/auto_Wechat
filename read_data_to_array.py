import xlrd


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'excel123.xlsx')

    # 获取所有sheet
    sheet1_name = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    sheet1 = workbook.sheet_by_name('Sheet1')

    # 获取整列的值（数组）
    cols2 = sheet1.col_values(3)  # 获取第4列内容（联系方式）
    cols1 = sheet1.col_values(0)  # 获取第1列内容（备注名）

    # 输出第一列第四列内容（第四列联系方式以整数形式输出）
    print(list(map(int, cols2)))
    # print(cols2)
    print(cols1)


if __name__ == '__main__':
    read_excel()
