import json

"""
 从json文件中，按照路径找到jsonArr，并提取指定字段
"""


def json_2csv(json_file, csv_file, path_names, label_names):
    # 读取JSON文件
    with open(source_file) as read_file:
        rf_data = json.load(read_file)

    # 提取字段，人工指定路径
    if path_names != "":
        the_list = rf_data[path_names[0]]
        for i in range(1, len(path_names)):
            the_list = the_list[path_names[i]]
    else:
        the_list = rf_data

    # 写入内容
    # 场景：hassan账号解析
    with open(result_file, 'a') as f:  # a 表示在尾部添加内容，重写改成w
        for d in the_list:
            for label in label_names:
                f.write(str(d[label]) + ",")
            f.write("\n")


if __name__ == '__main__':
    result_file = '/{文件路径}/fruit.csv'
    paths = "data,fruitList".split(",")
    labels = "id,color,cover".split(",")
    # 处理单个文件，使用以下代码块
    source_file = "/{文件路径}/fruit.json"
    json_2csv(source_file, result_file, paths, labels)

    # 需要循环处理文件时，使用以下代码块
    # i = 1
    # while i < 7:
    #     source_file = "/{文件路径}/fruit" + str(i) + ".json"
    #     json_2csv(source_file, result_file, paths, labels)
    #     i += 1

    print('Json导出csv完成')
