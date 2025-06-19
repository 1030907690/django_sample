import pandas as pd


def read_excel():
    path = "D:/works/导数据/xx.xlsx"
    # sheet_name默认为0，即读取第一个sheet的数据
    sheet = pd.read_excel(path, sheet_name=0)
    dict_list = []
    for row in sheet.index.values:
        doc = {}
        doc['key1'] = sheet.iloc[row, 0]
        doc['key2'] = sheet.iloc[row, 1]
        doc['key3'] = sheet.iloc[row, 2]
        doc['key4'] = sheet.iloc[row, 3]
        doc['key5'] = sheet.iloc[row, 4]

        print(doc)
        dict_list.append(doc)

    print(len(dict_list))

    for dict in dict_list:
        print(dict['key5'])


def read_excel_iterrows():
    path = "D:/works/导数据/xx.xlsx"
    try:
        df = pd.read_excel(path, sheet_name=0)

        # 遍历每一行
        for index, row in df.iterrows():
            # 访问每一行的值，例如，访问第一列的值
            first_column_value = row['编号']  # 假设第一列的列名为 '第一列'

            two_column_value = row['简称']

            # 在这里处理每一行的数据
            print(f"行索引: {index}, 第一列的值: {first_column_value} ,第二列 {two_column_value}")
            # 你可以在这里添加任何你想要对每一行进行的操作

    except FileNotFoundError:
        print("错误：未找到文件。")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == '__main__':
    print("This is a module")
    read_excel_iterrows()
