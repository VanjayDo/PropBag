# Touch Bar Preset (For BTT)

这是我配置的[BetterTouchTool](https://folivora.ai/)中关于Touch Bar的预设置文件，供参考使用。

预览：
<img style="display:block; margin-left:auto; margin-right:auto; width:1000px;" src="https://cdn.safeandsound.cn/ML_Study_Notes/image/触控栏快照 2019-03-24 下午4.55.34.png?imageslim"/>

## 一. Global配置详解（从左到右顺序)

### 1. ToolKit(Group)
工具箱，存放一些小工具的快捷打开方式。打开如下图，这里只添加了一个自带的拾色器（Picker），
<img style="display:block; margin-left:auto; margin-right:auto; width:1000px;" src="https://cdn.safeandsound.cn/ML_Study_Notes/image/触控栏快照 2019-03-24 下午7.14.36.png?imageslim"/>

### 2. PicGo(Button)
[PicGo](https://github.com/Molunerfinn/PicGo)为开源图片上传软件，支持多种图床，且能复制图片后一键上传。

复制图片后点击该按钮即可上传图片至图床。

**注1：** 点击该按钮后，显示器会给出文字反馈（HUD overlay）。

**注2：** 本配置文件绑定的上传快捷键为`⌃⌥⇧⌘P`，如需使用此button，请确保与你PicGo设置的上传快捷键相符。

### 3. Music(Group)
我使用的是网易云音乐，打开后如图👇
<img style="display:block; margin-left:auto; margin-right:auto; width:1000px;" src="https://cdn.safeandsound.cn/ML_Study_Notes/image/触控栏快照 2019-03-24 下午4.57.05.png?imageslim"/>

对于的按钮功能分别为 `上一首` | `暂停/播放` | `下一首` | `喜欢当前歌曲/取消喜欢当前歌曲` | `打开/关闭歌词` | `打开网易云音乐`。

**注1：** 本配置文件绑定的“喜欢歌曲”“打开歌词”快捷键为网易云音乐默认的App内快捷键，歌词可以在网易云中设置在桌面/菜单栏显示。如需使用这些功能，请确保快捷键相符。

**注2：** 根据当前BTT的版本V2.728和网易云音乐V2.0.0，在使用该组按钮的时候，有时会导致网易云音乐异常，原因未知。

**注3：** 如果你不使用网易云音乐可以自定义本组button，以适配其他的播放器。

**注4：** 点击该组内的按钮后，显示器会给出文字反馈（HUD overlay）。

### 4. App Switcher(Widget)
App切换组件，显示当前所有打开的App。

**注：** 根据当前BTT的版本V2.728，在使用该组件切换App的过程中，如果目标App没有打开的窗口或全部被最小化了，那么切换后将无法自动新建或打开窗口，需要手动操作。

### 5. 电量指示(Widget)
* 点击该电量指示按钮可以切换系统是否静音。点击该按钮后，显示器会给出文字反馈（HUD overlay）。

* 电池满电的情况下充电显示（预计使用时间为无穷`∞`）：

<img style="display:block; margin-left:auto; margin-right:auto; width:1000px;" src="https://cdn.safeandsound.cn/ML_Study_Notes/image/触控栏快照 2019-03-24 下午4.55.34.png?imageslim"/>

* 电池未充满电的情况下充电显示（显示时间为预计充满电所需时间，PS: 不准，你看MacOS的电量预计什么时候准过🤫）：

<img style="display:block; margin-left:auto; margin-right:auto; width:1000px;" src="https://cdn.safeandsound.cn/ML_Study_Notes/image/触控栏快照 2019-03-25 下午2.10.31.png?imageslim"/>

* 电池未充电的情况下显示（显示时间为根据当前电量预计使用时长，PS: 不准，你看MacOS的电量预计什么时候准过🤭）：

<img style="display:block; margin-left:auto; margin-right:auto; width:1000px;" src="https://cdn.safeandsound.cn/ML_Study_Notes/image/触控栏快照 2019-03-25 上午12.33.33.png?imageslim"/>

* 电脑充电状态发生变化时（由使用电池变为连接电源、由连接电源变为电池供电或是刚从睡眠状态恢复过来），时间会显示`?:??`，使用过一段时间后生成统计数据即可正常预计显示：

<img style="display:block; margin-left:auto; margin-right:auto; width:1000px;" src="https://cdn.safeandsound.cn/ML_Study_Notes/image/触控栏快照 2019-03-24 下午11.00.32.png?imageslim"/>

### 6. 日期时间指示(Widget)
* 点击该日期时间指示按钮可以切换输入法。点击该按钮后，显示器会给出文字反馈（HUD overlay）。

* **注：** 该配置文件绑定的切换输入法快捷键是`⌥Space`，如需使用请确保相符。

### 7. TouchBar手势预设(Widget)
* 二指：向左拖动：降低音量；向右拖动：提高音量；
* 三指：向左拖动：降低屏幕亮度；向右拖动：提高屏幕亮度；
* 四指：向左拖动：降低键盘背光亮度；向右拖动：提高键盘背光亮度；

## 二. 对特定App的配置
### 1. Finder
* `touch`按钮：用于创建新文件，取名自Unix-like OS中的touch命令；

## 三. 其他presets
该配置文件中的有不少配置项参考了该repo👉[btt-touchbar-presets](https://github.com/vas3k/btt-touchbar-presets)中的设置，你也可以参考中的其他presets进行客制化。