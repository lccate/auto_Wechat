# auto_Wechat
使用ADB和蟒等实现电脑端对微信的控制，实现加好友的功能。
最近做了个需求，从电脑上通过数据线控制安卓手机加微信好友，第一反应是从github上寻找类似代码，但是找到的代码都很复杂功能很多，思考后决定自己写一个，运行环境为python3.5.2（用到os和xlrd模块）。
1.下载adb工具
adb工具已上传到adb文件夹，这里就不放下载链接了，尽量下载比较新的adb工具，如果是旧版的后期无法输入中文（别问我怎么知道的，试了巨多次）
2.手机配置
需要将手机的的开启开发者选项，然后开启usb调试，允许usb控制以及模拟点击之类的设置，这个随手机型号的不同而不同。 
3.测试adb命令
从cmd中进到下载好的adb工具文件夹内，就可以开始敲命令了
一些基础的指令可以看我主页的另一个repository——ADBKeyBoard
//电源键
adb shell input keyevent 26
//菜单键
adb shell input keyevent 82
//home键
adb shell input keyevent 3
//返回键
adb shell input keyevent 4
//打开微信
adb shell am start -n com.tencent.mm/.ui.LauncherUI
4.获取页面坐标
这里推荐一个超级方便的方法！打开手机的指针功能，手指放在手机屏幕上时，会看到最上面一行有相关的坐标信息，有了这些坐标信息，我们就可以控制手机，想点哪里点哪里（注意！不同型号的手机坐标位置是不同的）
//模拟点击 100 300是坐标
adb shell input tap 100 300
