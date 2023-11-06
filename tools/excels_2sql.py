import pandas as pd

# 多个excel文件生成insert sql
"""
excel表格式范例：
id  name1   name2   name3
12  小王  15522223344 游泳
433 小红  17788990066 游泳,"铁人三项(游泳,自行车,跑步)"

表名：table_name
导出的文件内容
Insert into table_name (`name1`,`name2`,`name3`) values
("小王",15522223344,"游泳"),
("小红",17788990066,"游泳,\"铁人三项(游泳,自行车,跑步)\"");
"""
if __name__ == '__main__':
    result_name = "/{文件路径}/table_name.sql"
    file = open(result_name, 'w')
    min = 1
    max = 9
    for x in range(min, max):
        source_file_name = "/{文件路径}/ 文件名" + str(x) + ".xlsx"
        print(x)
        data = pd.read_excel(source_file_name)
        rows = data.index.values.size  # 行数
        cols = data.columns.values.size  # 列数
        cols_name = data.columns.values
        print("行数：" + str(rows) + "，列数：" + str(cols) + "\n")

        if x == min:
            values_name = "Insert into table_name ("
            for t in range(1, cols_name.size): # 先拼接insert字段名，不要第一列的"id"
                if t == cols - 1:
                    values_name = values_name + ("`{}`".format(data.columns.values[t]) + ") values ")
                else:
                    values_name = values_name + ("`{}`".format(data.columns.values[t]) + ",")
            file.write(values_name + '\n')
            print(values_name + "\n")
        for i in range(0, rows):
            values = "("
            for j in range(1, cols):  # 再拼接各字段的value，不要第一列id
                if pd.isna(data.values[i][j]):
                    values = values + "''"
                else:
                    tmp = str(data.values[i][j]).replace("\'", "\\\'").replace("\"", "\\\"")
                    values = values + ("'{}'".format(tmp))
                if j == cols - 1:   # 最后一列拼后括号和逗号
                    if x == max-1 and i == rows-1:  # 最后一个文件且是最后一行时，最后拼分号
                        values = values + ");"
                    else:
                        values = values + "),"
                else:
                    values = values + ","   # 非最后一列，拼逗号
            file.write(str(values) + '\n')
    file.close()
    print('所有excel 生成 sql 成功')
