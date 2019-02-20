# 修改备注名为：姓名+身份证号
# 不支持中文名称可能是adb版本的问题
# 添加好友时加对方姓名提高通过率
# 解决有的人改不了备注的问题（加一个点亮屏幕的操作，等待加载完成）
# 2018.12.4
# cccate

import os
import xlrd
import time

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
    cols3 = sheet1.col_values(1)  # 获取第2列内容（姓名）
    cols1 = sheet1.col_values(0)  # 获取第1列内容（备注名）
    cols_2 = list(map(int, cols2))
    # 输出第一列第四列内容（第四列联系方式以整数形式输出）
    print(cols_2)
    # print(cols2)
    print(cols1)
    print(cols3)

    for i in range(0, len(cols1)):
        #打开微信
        os.system('adb shell am start -n com.tencent.mm/.ui.LauncherUI')

        # "+"
        os.system('adb shell input tap 893 55')

        # 添加朋友
        os.system('adb shell input tap 652 353')

        #定位输入栏
        os.system('adb shell input tap 39 275')

        #输入手机
        time.sleep(3)
        os.system('adb shell input text %d' % (cols_2[i]))

        #查找
        os.system('adb shell input tap 196 245')

        #先点亮屏幕，避免有的加载不出来改不了备注，再设置备注和标签
        os.system('adb shell input keyevent 224')
        time.sleep(3)
        os.system('adb shell input tap 200 600')

        #删除原来的文本信息（最多删除6个字符）
        os.system('adb shell input keyevent 67')
        os.system('adb shell input keyevent 67')
        os.system('adb shell input keyevent 67')
        os.system('adb shell input keyevent 67')
        os.system('adb shell input keyevent 67')
        os.system('adb shell input keyevent 67')

        #输入备注信息
        #os.system('adb shell ime set com.android.adbkeyboard /.AdbIME')
        #os.system('adb shell input text %s'%(cols1[i]))
        time.sleep(3)
        os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '%s'" % (cols1[i]))

        #保存
        os.system('adb shell input tap 914 55')

        #添加好友到通讯录
        time.sleep(3)
        os.system('adb shell input tap 39 1056')
        os.system('adb shell input tap 39 907')
        os.system('adb shell input tap 39 720')

        #加好友时请求信息加上对方名字
        os.system('adb shell input tap 977 364.7')
        time.sleep(3)
        os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '%s你好，我是船员短期培训刘老师'" % (cols3[i]))

        # 发送
        time.sleep(3)
        os.system('adb shell input tap 914 55')
        time.sleep(3)

        #返回主界面
        os.system('adb shell input keyevent 4')
        os.system('adb shell input keyevent 4')
        time.sleep(2)
        os.system('adb shell input keyevent 4')
        os.system('adb shell input keyevent 4')
        os.system('adb shell input keyevent 4')
        time.sleep(2)
        os.system('adb shell am start -n com.tencent.mm/.ui.LauncherUI')
        print("%s完成"%(cols3[i]))
1
if __name__ == '__main__':

    over_all()