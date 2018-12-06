# 增加自动逐个添加功能
# 备注名为姓名
# 2018.12.6
# cccate

import os
import xlrd


def over_all():
    # 打开文件
    workbook = xlrd.open_workbook(r'excel123.xlsx')

    # 获取所有sheet
    sheet1_name = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    sheet1 = workbook.sheet_by_name('Sheet1')

    # 获取整列的值（数组）
    cols2 = sheet1.col_values(3)  # 获取第4列内容（联系方式）
    cols1 = sheet1.col_values(2)  # 获取第1列内容（备注名）
    cols_2 = list(map(int, cols2))
    # 输出第一列第四列内容（第四列联系方式以整数形式输出）
    print(cols_2)
    # print(cols2)
    print(cols1)

    for i in range(0, len(cols1)):
        #打开微信
        os.system('adb shell am start -n com.tencent.mm/.ui.LauncherUI')

        # "+"
        os.system('adb shell input tap 893 55')

        # 添加朋友
        os.system('adb shell input tap 652 353')

        #定位输入栏
        os.system('adb shell input tap 39 275')

        #输入手机号
        os.system('adb shell input text %d'%(cols_2[i]))

        #查找
        os.system('adb shell input tap 196 245')

        #设置备注和标签
        os.system('adb shell input tap 0 540')

        #删除原来的文本信息（最多删除6个字符）
        os.system('adb shell input keyevent 67')
        os.system('adb shell input keyevent 67')
        os.system('adb shell input keyevent 67')
        os.system('adb shell input keyevent 67')
        os.system('adb shell input keyevent 67')
        os.system('adb shell input keyevent 67')

        #输入备注信息
        os.system('adb shell input text %s'%(cols1[i]))

        #保存
        os.system('adb shell input tap 914 55')

        #添加好友到通讯录
        os.system('adb shell input tap 39 1056')
        os.system('adb shell input tap 39 907')
        os.system('adb shell input tap 39 720')
        #发送
        os.system('adb shell input tap 914 55')

        #返回主界面
        os.system('adb shell input keyevent 4')
        os.system('adb shell input keyevent 4')
        os.system('adb shell input keyevent 4')
        os.system('adb shell input keyevent 4')
        os.system('adb shell am start -n com.tencent.mm/.ui.LauncherUI')

if __name__ == '__main__':

    over_all()
