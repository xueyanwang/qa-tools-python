import pandas as pd

# excel 生成为 sql
if __name__ == '__main__':
    result_name = "/{文件路径}/table_name.sql"
    source_file_name = "/{文件路径}/data_source.xlsx"
    file = open(result_name, 'w')
    data = pd.read_excel(source_file_name)
    rows = data.index.values.size  # 行数
    cols = data.columns.values.size  # 列数
    cols_name = data.columns.values
    print("行数：" + str(rows) + "，列数：" + str(cols) + "\n")

    values_name = "Insert into table_name ("
    for t in range(1, cols_name.size):  # 先拼接sql头，不要第一列
        if t == cols - 1:
            values_name = values_name + ("`{}`".format(data.columns.values[t]) + ") values ")
        else:
            values_name = values_name + ("`{}`".format(data.columns.values[t]) + ",")
    file.write(values_name + '\n')
    print(values_name + "\n")
    for i in range(0, rows):  # 再拼接value，不要第一列
        values = "("
        for j in range(1, cols):
            if pd.isna(data.values[i][j]):
                values = values + "''"
            else:
                tmp = str(data.values[i][j]).replace("\'", "\\\'").replace("\"", "\\\"")
                values = values + ("'{}'".format(tmp))
            if j == cols - 1:
                if i == rows-1:
                    values = values + ");"
                else:
                    values = values + "),"
            else:
                values = values + ","
        sql_str = str(values)
        file.write(sql_str + '\n')
    file.close()
    print('excel 生成 sql 成功')
