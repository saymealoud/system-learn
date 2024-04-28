# coding:utf-8

from utils.excel import HandleExcel
from utils.db import Mysql


class Main(object):
    def __init__(self, excel_path, table_name):
        self.db = Mysql()
        self.handle_excel = HandleExcel(excel_path)
        self.table_name = table_name

    # 一键导入学生成绩信息
    def save_data(self):
        res = self.handle_excel.get_data()
        print("\t\t正在导入学生成绩 ", end="")

        # 导入之前清空表中的信息
        self.db.delete_all(self.table_name)

        for stu_k, stu_v in res.items():
            self.db.insert(self.table_name, stu_k, stu_v[0], stu_v[1],
                           stu_v[2], stu_v[3], stu_v[4])
            # 显示输出效果 "正在导入学生成绩 ..........."
            print(".", end="")
        print("\n\t\t导入完成")


    # 查询学生成绩
    # 如果指定学生姓名，则查询指定学生成绩，否则查询所有学生成绩
    def search_user_score(self, username=''):
        # TODO
        pass


    # 总成绩排名
    def total_score_sort(self):
        # TODO
        pass


if __name__ == '__main__':
    excelName = "script/students.xlsx"  # 学生成绩表
    classTableName = "three_three"      # 三年3班
    handle = Main(excelName, classTableName)

    while(True):
        # 主菜单
        print('''
                  学生信息管理系统
        ============= 功能菜单 =============
        1 一键导入学生成绩信息
        2 查询学生成绩信息                                        
        3 班级总成绩排名                                        
        0 退出系统                            
        =====================================
        说明：输入数字选择菜单                
        ''')

        input_str = input("\t\t请选择: ")
        if input_str == '0':  # 退出系统
            # TODO
            pass

        elif input_str == '1':  # 一键导入学生成绩信息
            print("\t\t一键导入，原班级成绩会被覆盖")
            mark = input("\t\t是否继续导入？(y/n): ")
            if mark == "y":
                handle.save_data()
            else:
                print("\t\t暂不导入")

        elif input_str == '2':  # 查询学生成绩
            # TODO
            pass

        elif input_str == '3':  # 班级总成绩排名
            # TODO
            pass

        else:
            print("\t\t输入有误，请重新输入")

