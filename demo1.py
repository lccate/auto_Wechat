# 加一个好友
# 2018.12.6
# cccate
import os


def over_all():
    # "+"
    os.system('adb shell input tap 893 55')

    # 添加朋友
    os.system('adb shell input tap 652 353')

    #定位输入栏
    os.system('adb shell input tap 39 275')

    #输入手机号
    os.system('adb shell input text 18363996178')

    #查找
    os.system('adb shell input tap 196 245')

    #设置备注和标签
    os.system('adb shell input tap 0 540')

    #删除原来的文本信息（最多删除5个字符）
    os.system('adb shell input keyevent 67')
    os.system('adb shell input keyevent 67')
    os.system('adb shell input keyevent 67')
    os.system('adb shell input keyevent 67')
    os.system('adb shell input keyevent 67')

    #输入备注信息
    os.system('adb shell input text 刘123')

    #保存
    os.system('adb shell input tap 914 55')

    #添加好友到通讯录
    os.system('adb shell input tap 39 1056')

    #发送
    os.system('adb shell input tap 914 55')

    #返回主界面
    os.system('adb shell input keyevent 4')
    os.system('adb shell input keyevent 4')
    os.system('adb shell input keyevent 4')


if __name__ == '__main__':
    over_all()
