# SleepWithLidOff

### 说明
Windows bat 脚本文件.

因为平时使用笔记本时总是有调整"关闭盖子是否睡眠"选项的需要, 所以写了这么个脚本, 以方便使用命令操作.

### 命令说明
以`dosleep.bat`文件中的命令为例 👇

```
powercfg -SetDcValueIndex 381b4222-f694-41f0-9685-ff5bb260df2e 4f971e89-eebd-4455-a8de-9e59040e7347 5ca83367-6e45-459f-a27b-476b1d01c936 1
rem powercfg -SetAcValueIndex 381b4222-f694-41f0-9685-ff5bb260df2e 4f971e89-eebd-4455-a8de-9e59040e7347 5ca83367-6e45-459f-a27b-476b1d01c936 1
powercfg /s 381b4222-f694-41f0-9685-ff5bb260df2e
```

`powercfg`即电源配置命令, `-SetDcValueIndex`和`-SetAcValueIndex`很明显就是分别设置直流(Direct Current, 即使用电池)和交流电(Alternating Current, 即使用充电电源)的选项, 

后面跟的`381b4222-f694-41f0-9685-ff5bb260df2e`是电源方案的GUID(设置你当前使用的电源方案, 平衡? 高性能? 自定义? 一般都是平衡吧, 这里以平衡为例, 可以使用`powercfg -q`查询), 如果设置的不是你当前使用的电源方案, 那么是不会在当前方案下生效的;

接着后面的`4f971e89-eebd-4455-a8de-9e59040e7347`是电源按钮和盖子的操作选项

然后的`5ca83367-6e45-459f-a27b-476b1d01c936`是合上盖子的操作选项

最后的`1`为睡眠, `0`则为不睡眠

第二行的`rem`起注释的作用, 因为这里的dosleep.bat脚本的作用是设置在使用电池的时候如果关上盖子则睡眠, 不关心使用充电电源时候的操作, 所以对于设置`-SetAcValueIndex`选项的命令就注释忽略了, 你可以根据需要修改

最后的`powercfg /s`命令是使系统上的指定电源方案处于活动状态, 这里设置激活的也就是平衡了.

### 使用方法
建议在`%appdata%\Microsoft\Windows\Start Menu\Programs`文件夹下新建一个文件夹保存脚本, 然后对脚本新建快捷方式, 然后将快捷方式移动到`C:\Windows\System32`文件夹下, 这样在cmd或者poweshell默认打开(默认打开后都是以`C:\Windows\System32`为当前路径)后就可以直接输入命令`dosleep.lnk`(一般输入dosl后使用tab键补全即可, 具体输入长度要看你的其他文件有没有前面部分重名的), 命令执行完毕即可关闭盖子睡眠.