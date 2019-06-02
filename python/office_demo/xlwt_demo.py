#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description: 操作 excel 文件

import xlwt
import xlrd


def create_excel(data: 'List[List[]]', filepath):
    '''创建 Excel 文件'''
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = workbook.add_sheet('first_sheet',cell_overwrite_ok=True)
    for r in range(len(data)):
        col = data[r]
        for c in range(len(col)):
            sheet.write(r, c, col[c])
    workbook.save('/tmp/tmp_excel.xlsx')

def read_excel(filepath):
    '''读取 Excel 文件'''
    f = xlrd.open_workbook(filepath)    # 打开excel文件对象

    table = f.sheet_by_index(0)         # 通过索引顺序获取表格
    # table = file.sheet_by_name('n')   # 通过表名获取对应表格
    #  tables = f.sheets()              # 获取表列表

    rows = table.nrows                  # 总的行数
    #  columns = table.ncols            # 总的列数

    for r in range(rows):               # 遍历每一行，包括标题
        row = table.row_values(r)       # 获取每一行的数据，返回一个列表
        print(row)


if __name__ == "__main__":
    data = [
        ['姓名', '年龄'],
        ['wxnacy', '18'],
        ['wen', '18'],
    ]
    filepath = '/tmp/tmp_excel.xlsx'
    create_excel(data, filepath)
    read_excel(filepath)
