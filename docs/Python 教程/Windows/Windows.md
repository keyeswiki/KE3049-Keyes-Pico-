# Python 教程 Windows

## 开发环境设置（重要）

在开始构建项目之前，你需要首先做一些准备，这是非常重要的，你不能跳过。

1.  安装Thonny(重要)

Thonny是一个免费、开源的软件平台，体积小，界面简单，操作简单，功能丰富，是一个适合初学者的Python IDE。在本教程中，我们使用这个IDE在整个过程中开发树莓派Pico。Thonny支持多种操作系统，包括Windows, Mac OS, Linux。

1.  下载Thonny软件

(1)进入软件官网：[https://thonny.org](https://thonny.org)下载Thonny软件，最好下载最新版的，否则可能不支持树莓派
Pico.

(2)Thonny的开源代码库：[https://github.com/thonny/thonny](https://github.com/thonny/thonny)

请按照官网的指导安装或点击下面的链接下载安装。(请根据您的操作系统选择相应的选项.)

|操作系统|下载链接/方法|
|-|-|
|MAC OS：|[https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.pkg"](https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.pkg)|
|Windows：|[https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.exe"](https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.exe)|
|Linux：|最新版本: Binary bundle for PC (Thonny+Python): bash <(wget -O - https://thonny.org/installer-for-linux) With pip: pip3 install thonny Distro packages (may not be the latest version): Debian, Rasbian, Ubuntu, Mint and others: sudo apt install thonny Fedora: sudo dnf install thonny|

![](media/99f54f311de9fd9be58e768d329a61dc.png)

2.  在Windows上安装Thonny软件



1.  下载后的Thonny图标如下。

![](media/d3caa98d406fa06a124d5c98195b90db.png)

2.  双击“thonny-3.3.13.exe”，会出现下面对话框，我这里是选择“![](media/11fb59a50abe0bf54df7e4cb891ad2c0.png)”进行操作的。你也可以选择“![](media/37be3f3bcc9aa0eb48c8b844eb46a71c.png)”进行操作的。

![](media/4c044b255da8b14fe674eb9cce01627d.png)

3.  如果您不熟悉电脑软件安装，您可以一直单击“Next”直到安装完成。

![](media/995b36640124b6a9b23f10473ff8a38a.png)

![](media/8bcc17840b9fc15d76f79fee8a0168ee.png)

4.  如果您需要更改Thonny软件的安装路径，可以单击“Browse...”进行修改。选择安装路径后，单击“OK”。

如果您不想更改安装路径，只需单击“Next”；然后又继续单击“Next”。

![](media/df6f63b42ebb1676b22c26b25dc9c7aa.png)

![](media/f5cd6d619b4645601c5b098ffdbec12a.png)

5.  选中“Create desktop     icon”，Thonny软件会在你的桌面上生成一个快捷方式，方便你稍后打开Thonny软件。

![](media/a30c89dde3de81ad00aced30510071be.png)

6.  单击“Install”安装软件。

![](media/6ace65142291e5e8af5f81e4a6b2f180.png)

7.  在安装过程中，您只需等待安装完成，千万不要点击“Cancel”，否则将无法安装成功。

![](media/a504b3a3ab16b4d91040cd5878acea0c.png)

8.  一旦看到如下界面，就表示已经成功安装了Thonny软件，点击“Finish”就可以。

![](media/a1fb6027e54a975de1c0aa1e1a0d6a29.png)

9.  如果你在安装过程中选择了“Create desktop     icon”，则可以在桌面上看到如下图标。

![](media/80f35044d91d66f734e36059db35f273.png)

2.  Thonny软件基本配置



1.  双击Thonny软件的桌面图标，可以看到如下界面，同时还可以进行语言选择(这里选择简体中文)和初始设置。设置完了点击“Let’s     go！”。

![](media/ee240978a4f844184f1ea9f5a21d0395.png)

![](media/bfb4c5bdce61fdd384c32afb17ba9145.png)

![](media/fb2631689bfa02c2476fb12e16f7cd16.png)

![](media/ec56f1d21d0e2010d306acb9195228f8.png)

![](media/64478dcfa0ca3caf1032ac9afdd8d063.png)

2.  选择“视图”→“文件”和“Shell”。

![](media/48c91a00e2a97ce165ab422f94973e52.png)

![](media/f5e2d0186537cb919a7b16411b68be17.png)

![](media/ee856098d9f39b73fb1733a418598502.png)

3.  更新Micropython固件（重要）

要在树莓派Pico板上运行MicroPython程序，我们需要先烧入一个固件到树莓派Pico板中。

1.  为什么我们需要更新固件

树莓派Pico板可以用C语言和MicroPython语言编程，并且树莓派Pico板出厂时没有MicroPython固件，使用MicroPython编程之前需要下载MicroPython固件。

注意：MicroPython固件只需要下载一次，当使用MicroPython编程时不需要再次下载。如果你已经下载了用C语言编写的 .uf2
程序固件，则MicroPython固件将会被覆盖，那下次你使用MicroPython时，你需要按照以下步骤更新树莓派Pico板的固件。

2.  下载Micropython固件

方法1：树莓派Pico的官网：[https://www.raspberrypi.com/documentation/microcontrollers/](https://www.raspberrypi.com/documentation/microcontrollers/)

1.  单击上面的链接，你可以看到以下界面：

![](media/6e018e1b1bbfb884f6de8db5b4e5f7d4.png)

2.  滚动鼠标，你又可以看到以下内容：

![](media/06c6ed643e6b559f0c0ae9f1d08b9d6a.png)

3.  单击“MicroPython(Getting started     MicroPython)”进入固件下载页面。

![](media/e8d9658a60f750a654bd2d7a98fe3bb5.png)

方法2：通过单击下载链接：[https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2)，可以直接下载。

方法3：如果你因为网络问题或其他原因无法下载，可以使用我们准备的 .uf2
文件，它位于以下文件路径

![](media/fe7933eaf8947f37d71b2ee220f43f68.png)

3.  烧入MicroPython固件的步骤

①连接microUSB线一端到你的电脑USB口。

②长按“树莓派Pico板”上的白色按钮（BOOTSEL）。然后，通过microUSB线另一端将树莓派Pico板与电脑连接。

![](media/33c91d51b2aeb2c943691706354aaad1.png)

③松开按钮，当连接成功时，在你的电脑上打开\[设备管理器\]，电脑将自动识别可移动磁盘(RPI-RP2)，如下所示:

![](media/87e24af3ea812b5492a06b0141060b86.png)

④复制文件（rp2-pico-20210902-v1.17.uf2）到可移动磁盘(RPI-RP2)，并等待它完成，就像复制文件到U盘一样。

![](media/cc6317c1e32813f5edde9331af35c150.png)

![](media/72720a19e39fe9105ffc364bd7f56d4b.png)

⑤当固件烧入完成后，树莓派Pico板会自动重启。之后，你可以运行Micropython。

四、Thonny软件连接上树莓派Pico板

1.打开Thonny软件，点击“运行”并选择“选择解释器…”

![](media/d5e1560eef5a889f9dead50e6327e09e.png)

3.  选择“Micropython (一般)”或“Micropython (Raspberry Pi     Pico)”均可。如何选择“Micropython(Raspberry Pi Pico)”?
    如下所示：

![](media/c746f079db6a1e174371b3e8e123b08c.png)

3.选择“USB-SERIAL (COMx)”，“COMx”的编号在不同的电脑之间可能会有所不同。你只需要确保选择“USB-SERIAL (COMx)”就行。

如何确定你的树莓派Pico板与电脑通信的端口?

步骤1:当你的树莓派Pico板没有连接到电脑时，打开Thonny软件，点击“运行”，选择“选择解释器...”，弹出对话框，点击“端口”，可以查看当前连接的端口，如下图所示:

![](media/b54aba987917cb42fe6a6266b61e3d0b.png)

步骤2:关闭对话框。将树莓派Pico板连接到电脑，再次单击“运行”并选择“选择解释器...”。单击弹出窗口中的“端口”，查看当前端口。现在又增加了一个端口，那么这个端口是用来与电脑通信的。

![](media/8001573d8beb85a0b8fc2b3adb724ce5.png)

4.  选择“Micropython(Raspberry Pi Pico)”和端口后，单击“确定”。

![](media/5ef3eeaabb007608ab6d88863d7c6bfa.png)

5.  当在Thonny软件上显示以下消息时，表明Thonny软件已成功连接到树莓派Pico板。

![](media/c7c043895f31d3b5282edb41354b09fe.png)

到目前为止，所有的准备工作都已就绪。

五、测试代码(重要)

1.测试Shell命令

在“Shell”窗口输入“print(Hello World!)”，按“Enter”键。

![](media/38ae83697f7fe9e78bdcf6d2feb77ab3.png)

2.在线运行代码：

要在线运行树莓派Pico，你需要把树莓派Pico板连接到电脑上。这样就可以使用Thonny软件编译或调试程序。

优点：（1）你可以使用Thonny软件编译或调试程序。

（2）通过“Shell”窗口，你可以查看程序运行过程中产生的错误信息和输出结果，并可以在线查询相关功能信息，帮助改进程序。

缺点：（1）要在线运行树莓派Pico，你必须将树莓派Pico板连接到一台电脑上并和Thonny软件一起运行。

（2）如果树莓派Pico板与电脑断开连接，当它们重新连接时，程序将无法再次运行。

基本操作：

（1）打开Thonny软件，并且单击![](media/6388aa0daa514f9325fb07fd5ab6749b.png)“打开...”。

![](media/72919465d3c2650ce9c5e08dec1bdba3.png)

（2）在新弹出的窗口中，点击“此电脑”。

![](media/4a648e13d503cef0dad076d295eeff7e.png)

在新的对话框中，进入文件夹2. 项目教程\项目 01：Hello World
选中“Project_01_HelloWorld.py”,单击“Open”。本教程中使用的代码保存在“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

![](media/16bf665b42375d352eda2a40e48bb13f.png)

（3）单击![](media/f79b2c42507d12b91ca23ea0bb87c5c2.png)“运行当前脚本”来执行程序“Hello World!”, "Welcome keyes" 将打印在“Shell”窗口。

![](media/db4bada12ee67e86b74d14ece7e8c59e.png)

退出在线运行

当在线运行时，单击Thonny软件上的![](media/fee1916cdaf53677f5117fbc5b65f4cf.png)“停止
/重启后端进程”或按Ctrl+C退出程序。

![](media/780ca09b2d54377ea8f6effc00897d97.png)

3.离线运行代码：

在离线运行时，树莓派Pico板不需要连接电脑和Thonny软件。一旦上电，它就可以运行存储在树莓派Pico板中的main.py程序。

优点：不需要连接电脑和Thonny软件就可以运行程序。

缺点：出现错误或树莓派Pico板没电时，程序会自动停止，并且代码不容易更改。

基本操作：

一旦上电后，树莓派Pico板会自动检查设备上是否存在main.py。如果有，则运行main.py中的程序，然后进入shell命令系统。(如果你想让代码离线运行，你可以将它保存为main.py);
如果main.py不存在，则直接进入shell命令系统。

（1）单击 “文件”→“新文件” 创建并编写代码。

![](media/a37e32734e9502db5706d851c355c71d.png)

（2）在新打开的文件中输入代码。这里我们以Project_02_Onboard_LED_flashing.py代码为例。

![](media/56e5eeb11c2bce71fd154a5f5bb7acbe.png)

（3）单击菜单栏上的![](media/861d55963959682fdb0ffe4b7f892fe1.png)“保存”,
你可以将代码保存到此电脑或Raspberry Pi Pico。

![](media/5114c0e31230ef5257860c60f2b58fef.png)

4.  选择“Raspberry Pi     Pico”，在新弹出的窗口中输入“main.py”并单击“确认”。

![](media/6bfa098bf88de82695ef2c1945aa424d.png)

![](media/2d3e53ef359ac655530856974e2401a2.png)

5.  你可以看到代码已经被上传到树莓派Pico板。

![](media/3e67f7e50d111608405029879b87f16b.png)

（6）断开树莓派Pico板的microUSB线，再重新连接，树莓派Pico板上的LED会反复闪烁。

![](media/e12ecf9006915a143134d18d53643ee4.png)
![](media/6f49241878e04e8ba4edd30fb2714249.png)

0.5秒

退出离线运行

连接树莓派Pico板到电脑，点击Thonny软件上的![](media/9994536062b2b521a194db65bbea995e.png)“停止
/重启后端进程”结束离线运行。

![](media/caa403fdfd27fcbf518a23f027f751b9.png)

如果它不能工作，请点击Thonny软件上的![](media/9994536062b2b521a194db65bbea995e.png)“停止
/重启后端进程”多次或重新连接树莓派Pico板。

![](media/c67a902a13876744d413773f28a6c62f.png)

我们提供了一个main.py文件用于离线运行。添加到main.py中的代码是执行用户代码文件的引导程序。你只需要将离线项目的代码文件(.py)上传到“Raspberry Pi Pico”。

①将程序文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”提前移动到Disk(D)，路径为D:\2.
项目课程。打开Thonny软件。

![](media/c6b188dea3d4d1bab710e120c5e489c5.png)

②在Disk(D)目录下D:\\2.
项目课程中展开“项目
00：main”，鼠标左键双击main.py，我们提供的main.py可以使“Raspberry Pi Pico”中的代码离线运行。

![](media/d1aaebe176f73b4b138768bbcfac80bc.png)

这里，我们使用项目 00和项目
02案例作为演示。使用树莓派Pico板上的LED（GP25引脚）显示结果。如果你已经修改了Project_02_Onboard_LED_flashing.py文件，那么你需要相应地修改它。如下图所示，鼠标右键单击Project_02_Onboard_LED_flashing.py文件，选择“上载到
/“上传代码到 Raspberry Pi Pico。

![](media/9ff7c48a057163dfb278ed9027960756.png)

用同样的方法上传main.py

![](media/b1b92c0e264fc75c4eae33f678928070.png)

![](media/3d2e9ed98307c9605fb109fac29edf0f.png)

断开树莓派Pico板的microUSB线并重新连接，树莓派Pico板上的LED将反复闪烁。

![](media/e12ecf9006915a143134d18d53643ee4.png)
![](media/6f49241878e04e8ba4edd30fb2714249.png)

0.5秒

注意:

这里的代码是离线运行的。如果你想停止离线运行并且在“Shell”窗口显示对应信息，只需单击Thonny软件上的![](media/9994536062b2b521a194db65bbea995e.png)“停止
/重启后端进程”。

![](media/37adb2c653f32aff1430d84b57ef1420.png)

六、Thonny常见的操作

上传代码至Raspberry Pi Pico

在Project 01：Hello World文件夹中，鼠标右键单击选中Project_01_HelloWorld.py，选择“上载到/”上传代码到
Raspberry Pi Pico的根目录。

![](media/95686a19321bb411ab4a5b6ba078c997.png)

下载代码至电脑

在“Raspberry Pi Pico”中，鼠标右键单击选中Project_01_HelloWorld.py，选择“下载到/”将代码下载到你的电脑。

![](media/5360cc2e106c0cb14bb2da87e53c2f68.png)

删除Raspberry Pi Pico根目录中的文件

在“Raspberry Pi Pico”中，鼠标右键单击选中Project_01_HelloWorld.py，选择“删除”，从Raspberry Pi Pico根目录中删除Project_01_Hello World.py。

![](media/44eef0acff104423cb7d4afeade6e92d.png)

删除电脑目录中的文件

在Project 01：Hello World文件夹中，鼠标右键单击选中Project_01_HelloWorld.py，选择“移动到回收站”，即可从Project 01：Hello World文件夹中删除。

![](media/70f40ec3fe52a7f1e27728f26b3ae763.png)

创建和保存代码

（1）单击 “文件”→“新文件” 创建并编写代码。

![](media/a37e32734e9502db5706d851c355c71d.png)

（2）在新打开的文件中输入代码。这里我们以Project_02_Onboard_LED_flashing.py代码为例。

![](media/56e5eeb11c2bce71fd154a5f5bb7acbe.png)

（3）单击菜单栏上的![](media/861d55963959682fdb0ffe4b7f892fe1.png)“保存”,
你可以将代码保存到此电脑或Raspberry Pi Pico。

![](media/5114c0e31230ef5257860c60f2b58fef.png)

6.  选择“Raspberry Pi     Pico”，在新弹出的窗口中输入“main.py”并单击“确认”。

![](media/6bfa098bf88de82695ef2c1945aa424d.png)

![](media/2d3e53ef359ac655530856974e2401a2.png)

7.  你可以看到代码已经被上传到Raspberry Pi Pico。

![](media/3e67f7e50d111608405029879b87f16b.png)

⑥单击![](media/abd47da3d3d7e2e2acd2d8fa46397c95.png)“当前运行脚本”,树莓派Pico板上的LED会周期性闪烁。

![](media/12b2ab96e0b9de0081068a4cd62f9917.png)





## 项目课程

### 项目 01: Hello World

项目介绍：

对于树莓派Pico初学者，我们将从一些简单的东西开始。在这个项目中，你只需要一个树莓派Pico板，USB线和电脑就可以完成“Hello World!”项目。它不仅是树莓派Pico和电脑的通信测试，也是树莓派Pico板的初级项目。

项目元件：








|![](media/ea4c22ac79b4e3cf9c6185c6ccf3717a.jpg)|![](media/3bdcc62cfa661d2b860a76e28537e21e.png)|
|-|-|
|树莓派Pico板*1|USB 线*1|




项目接线：

在本项目中，我们通过USB线将树莓派Pico板和电脑连接起来。连接方法请参照文档：开发环境设置

![](media/bbebdf7f2c0f4c223b6f2548d7ff6607.png)![](media/ea4c22ac79b4e3cf9c6185c6ccf3717a.jpg)

在线运行代码：

要在线运行树莓派Pico，你需要把树莓派Pico板连接到电脑上。这样就可以使用Thonny软件编译或调试程序。

优点：
1.你们可以使用Thonny软件编译或调试程序。

2. 通过“Shell”窗口，你们可以查看程序运行过程中产生的错误信息和输出结果，并可以在线查询相关功能信息，帮助改进程序。

缺点：

1.要在线运行树莓派Pico，你必须将树莓派Pico板连接到一台电脑上并和Thonny软件一起运行。

2.如果树莓派Pico板与电脑断开连接，当它们重新连接时，程序将无法再次运行。

基本操作：

1.打开Thonny软件，并且单击![](media/6388aa0daa514f9325fb07fd5ab6749b.png)“打开...”。

![](media/72919465d3c2650ce9c5e08dec1bdba3.png)

2.在新弹出的窗口中，点击“此电脑”。

![](media/4a648e13d503cef0dad076d295eeff7e.png)

在新的对话框中，选中“Project_01_HelloWorld.py”,单击“Open”。本教程中使用的代码保存在“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

![](media/16bf665b42375d352eda2a40e48bb13f.png)

3.单击![](media/f79b2c42507d12b91ca23ea0bb87c5c2.png)“运行当前脚本”来执行程序“Hello World!”, "Welcome keyes" 将打印在“Shell”窗口。

![](media/db4bada12ee67e86b74d14ece7e8c59e.png)

退出在线运行

当在线运行时，单击Thonny软件上的![](media/fee1916cdaf53677f5117fbc5b65f4cf.png)“停止
/重启后端进程”或按Ctrl+C退出程序。

![](media/780ca09b2d54377ea8f6effc00897d97.png)






### 项目 02：板载灯闪烁

项目介绍：

树莓派Pico板上有个板载LED，这个LED是固定接在树莓派Pico板上的GP25引脚，在这个项目中，我们将来学习使板载LED闪烁的效果。

项目元件：








|![](media/ea4c22ac79b4e3cf9c6185c6ccf3717a.jpg)|![](media/3bdcc62cfa661d2b860a76e28537e21e.png)|
|-|-|
|树莓派Pico板*1|USB 线*1|




项目接线：

在本项目中，用USB线将树莓派Pico板和电脑连起来。连接方法请参照文档：开发环境设置

![](media/bbebdf7f2c0f4c223b6f2548d7ff6607.png)![](media/ea4c22ac79b4e3cf9c6185c6ccf3717a.jpg)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

代码在线运行：

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
02：板载灯闪烁”。

![](media/f53af2742508818b162febd58c9ba562.png)

展开文件夹“项目
02：板载灯闪烁”，鼠标左键双击“Project_02_Onboard_LED_flashing.py”打开它。如下图所示：

![](media/9b2a98cd4675782eae5b109fc64f2ed1.png)



确保树莓派Pico板已经连接到电脑上。单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/启动后端进程”，然后去看看“Shell”窗口将显示什么界面。

![](media/f88ceeb17f9125111a6b47814b8cea21.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：树莓派Pico板的LED开始闪烁。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/启动后端进程”退出程序。

![](media/3e08be885fc89a08e1c1c40076ad65a0.png)

![](media/e12ecf9006915a143134d18d53643ee4.png)
![](media/6f49241878e04e8ba4edd30fb2714249.png)

0.5秒

注意：这是在线运行的代码。如果你断开USB线，重新启动“Raspberry Pi Pico”，树莓派Pico板上的LED停止闪烁。在Thonny软件“Shell”窗口将显示如下信息：

![](media/1b2662df68f1b6ca9b27d7a61faf5384.png)

代码离线运行（上传代码到Raspberry Pi Pico）：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/启动后端进程”。

![](media/d78060922a01cecad16d524c57ac6786.png)

如下图所示，鼠标右键单击文件“Project_02_Onboard_LED_flashing.py”，选择“上载到/”上传代码到Raspberry Pi Pico。

![](media/c9c693c286da79aa8fde929421a90607.png)

用同样的方法上传main.py

![](media/9b7807007828f06c0b9f7d48cbf1fcc7.png)

![](media/adb91d4636fc5ea4299526c51eda87dd.png)

断开树莓派Pico板上的USB线并重新连接，树莓派Pico板的LED会反复闪烁。

![](media/e12ecf9006915a143134d18d53643ee4.png)
![](media/6f49241878e04e8ba4edd30fb2714249.png)

0.5秒

注意：这里的代码是离线运行的。如果你想停止离线运行并且在“Shell”窗口显示对应信息，只需单击Thonny软件中的![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/启动后端进程”。

![](media/dd098f448a5c0f0a4209f6b102893289.png)





### 项目 03：外接灯闪烁 

项目介绍：

在这个项目中，我们将向你展示外接LED闪烁效果。我们使用树莓派Pico板的数字引脚打开LED，让它闪烁。

项目元件：










|![](media/c6e2dacdcbf063ed4ee92f619c6cb961.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|公对母杜邦线若干|USB 线*1|
|![](media/7eb361d680dfa351f07f8527aeb37abd.png)|![](media/f7784bea849600eb35d1a52730050dd2.png)|![](media/01e1718266f97a76fa59685d5d339430.png)||
|红色LED*1|220Ω电阻*1|面包板*1||




元件知识：

（1）LED:

![](media/626a5da07f0aa2aee972c73a879896da.jpg)

LED是一种被称为“发光二极管”的半导体，是一种由半导体材料(硅、硒、锗等)制成的电子器件。它有正极和负极。短腿为负极，接GND，长腿为正极，接3.3V或5V。

![](media/14a84d5f016d7566151a5563c502787e.png)

（2）五色环电阻

电阻是电路中限制或调节电流流动的电子元件。左边是电阻器的外观，右边是电阻在电路中表示的符号。电阻(R)的单位为欧姆(Ω)，1 mΩ= 1000 kΩ，1kΩ= 1000Ω。

![](media/915dcbfa3e0a610e57747f292049f3a5.jpg)
![](media/b8c2bb90c0248dc176e003ab283305a2.png)

我们可以使用电阻来保护敏感组件，如LED。电阻的强度（以Ω为单位）用小色环标记在电阻器的主体上。每种颜色代表一个数字，你可以用电阻对照卡查找。

\-色带1 – 1st Digit.

-色带 2 – 2nd Digit.

-色带 3 – 3rd Digit.

-色带 4 – Multiplier.

-色带 5 – Tolerance.

![](media/c3df005312cd9f6d4cdae6abf3cddb83.png)

在这个套件中，我们提供了3个具有不同电阻值的五色环电阻。这里以3个五色环电阻为例：

220Ω 电阻*10

![](media/36975a2bb15b26b3a05d358b4ea3429d.png)

10KΩ 电阻*10

![](media/cf6d6c9c02527cd2b9155e5385c20c24.png)

1KΩ 电阻*10

![](media/f72eafc0548a81c4624a081f8380675f.png)

在相同的电压下，会有更小的电流和更大的电阻。电流(I)、电压(U)、电阻(R)之间的联系可以用公式表示：I=U/R。在下图中，假如电压为3V，则通过R1的电流:
I = U / R = 3 V / 10 KΩ= 0.0003A= 0.3mA。

![](media/b3eec552e4dfad361833730698621776.png)

不要把电阻值很低的电阻直接连接在电源两极，这样会使电流过高而损坏电子元件。电阻是没有正负极之分。

（3）面包板

面包板是实验室中用于搭接电路的重要工具。面包板上有许多孔，可以插入集成电路和电阻等电路元件。熟练掌握面包板的使用方法是提高实验效率，减少实验故障出现几率的重要基础之一。下面就面包板的结构和使用方法做简单介绍。一个典型的面包板如下所示：

![](media/837cd6ec4b1b09cc46340201a6425958.jpeg)

面包板的外观和内部结构如上图所示，常见的最小单元面包板分上、中、下三部分，上面和下面部分一般是由一行或两行的插孔构成的窄条，中间部分是由中间一条隔离凹槽和上下各5
行的插孔构成的条。

![](media/099510035abc223273495e042a7bd6b6.jpeg)

在面包板的两个窄条分别有两行插孔，两行之间是不连通的，一般是作为电源引入的通路。上方第一行标有“+”的一行有10组插孔（内部都是连通），均为正极；上方第二行标有“-”的一行有10组插孔，（内部都是连通），均为接地。面包板下方的第一行与第二行结构同上。如需用到整个面包板，通常将“+”与“+”用导线连接起来，“-”与“-”用导线连接起来。

　　中间部分宽条是由中间一条隔离凹槽和上下各5
行的插孔构成。在同一列中的5
个插孔是互相连通的，列和列之间以及凹槽上下部分则是不连通的。外观及结构如下图：

![](media/3fc9a04d9354e63ca0e89eb7ed627128.png)

中间部分宽条的连接孔分为上下两部分，是面包板的主工作区，用来插接原件和跳线。在同一列中的5个插孔（即a-b-c-d-e，f-g-h-i-j）是互相连通的；列和列之间以及凹槽上下部分是不连通的。在做实验的时候，通常是使用两窄一宽组成的小单元，在宽条部分搭接电路的主体部分，上面的窄条取一行做电源，下面的窄条取一行做接地。中间宽条用于连接电路，由于凹槽上下是不连通的，所以集成块一般跨插在凹槽上。

（4）keyes 树莓派Pico板的扩展板使用方法

将树莓派Pico板堆叠在扩展板上即可使用，如下图：

![](media/0161af1decdb4f2bcfffbe8601f80781.jpg)

（5）电源

在本项目中，用USB线将树莓派Pico板和电脑连起来。连接方法请参照文档：开发环境设置

![](media/bbebdf7f2c0f4c223b6f2548d7ff6607.png)![](media/ea4c22ac79b4e3cf9c6185c6ccf3717a.jpg)

项目电路图和接线图：

首先，切断树莓派Pico板的所有电源。然后根据电路图和接线图搭建电路。电路搭建好并验证无误后，用USB线将树莓派Pico板连接到电脑上。注意：避免任何可能的短路(特别是连接3.3V和GND)!

警告：短路可能导致电路中产生大电流，造成元件过热，并对硬件造成永久性损坏。

![](media/cb069d7553d861e3293d8bdbe85bbd05.png)

电路图

![](media/96800765a20d72653a8cd4a9ae12b636.png)

接线图

注意: 怎样连接LED

![](media/87561b920ab7897195297350ac3fc1dd.png)

怎样识别五色环220Ω电阻

![](media/c143fb8d355d4cb13056f3b2f15bd23c.png)

项目代码：

根据电路图，当树莓派Pico板的GP16输出高电平时，LED点亮；当输出低电平时，LED灯关闭。因此，我们可以通过控制GP16重复输出高低电平，使LED反复闪烁。

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

代码在线运行：

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
03：外接灯闪烁”。

![](media/9d3a70645a76662b9667ef20536921af.png)

展开文件夹“项目
03：外接灯闪烁”，鼠标左键双击“Project_03_External_LED_flashing.py”打开它。如下图所示：

![](media/3cdf5094b31e7d8d09960b1d4d9bd177.png)



确保树莓派Pico板已经连接到电脑上。单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”，然后去看看“Shell”窗口将显示什么界面。

![](media/2ee55bf99a6a6e568b84de55c4a7a336.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，电路中的LED开始闪烁。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/e01a5fdeb672bfa12f37846a772695ec.png)

![](media/29fb2d6a043a0e659a37634caeb89b28.png)
![](media/2dcc6a55b77b4175b5175f717eb196c3.png)

0.5秒

注意：这是在线运行的代码。如果断开USB线，重新启动“Raspberry Pi Pico”，LED停止闪烁。在Thonny软件的“Shell”窗口将显示如下信息：

![](media/30b7cb91252c3fef610e1d9571ab3b07.png)

代码离线运行（上传代码到Raspberry Pi Pico）：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/844129bbf71ada74f947158b3a6943ae.png)

如下图所示，鼠标右键单击文件“Project_03_External_LED_flashing.py”，选择“上载到/”上传代码到Raspberry Pi Pico。

![](media/b4421906fd3a96b7d87617ba4bc33056.png)

用同样的方法上传main.py

![](media/477bdd8f7454e18818560132cf562434.png)

![](media/a732db98c7fbda11457fb51d159d2012.png)

断开树莓派Pico板上的USB线并重新连接，电路中的LED会反复闪烁。

![](media/29fb2d6a043a0e659a37634caeb89b28.png)
![](media/2dcc6a55b77b4175b5175f717eb196c3.png)

0.5秒

注意：这里的代码是离线运行的。如果你想停止离线运行并且在“Shell”窗口显示对应信息，只需单击Thonny软件中的![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/3c11b930b665a45612460c314af455d8.png)





### 项目 04: 呼吸灯

项目介绍：

在之前的研究中，我们知道LED有亮/灭状态，那么如何进入中间状态呢?如何输出一个中间状态让LED“半亮”?这就是我们将要学习的。呼吸灯，即LED由灭到亮，再由亮到灭，就像“呼吸”一样。那么，如何控制LED的亮度呢?我们将使用树莓派Pico板的PWM来实现这个目标。

项目元件：










|![](media/c6e2dacdcbf063ed4ee92f619c6cb961.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|公对母杜邦线若干|USB 线*1|
|![](media/7eb361d680dfa351f07f8527aeb37abd.png)|![](media/f7784bea849600eb35d1a52730050dd2.png)|![](media/01e1718266f97a76fa59685d5d339430.png)||
|红色LED*1|220Ω电阻*1|面包板*1||




元件知识：

![](media/54b13e97b57933c968504eb0c3d732ce.png)

Analog & Digital

模拟信号在时间和数值上都是连续的信号。相反，数字信号或离散时间信号是由一系列数字组成的时间序列。生活中的大多数信号都是模拟信号。一个熟悉的模拟信号的例子是，全天的温度是如何不断变化的，而不是突然从0到10的瞬间变化。然而，数字信号的值可以瞬间改变。这个变化用数字表示为1和0(二进制代码的基础)。如下图所示，我们可以更容易地看出它们的差异。

![](media/4bdf6127e563b453a1fd8953b4ebb277.png)

在实际应用中，我们经常使用二进制作为数字信号，即一系列的0和1。由于二进制信号只有两个值(0或1)，因此具有很大的稳定性和可靠性。最后，可以将模拟信号和数字信号相互转换。

PWM：

脉宽调制(PWM)是一种利用数字信号控制模拟电路的有效方法。普通处理器不能直接输出模拟信号。PWM技术使这种转换(将数字信号转换为模拟信号)非常方便。PWM技术利用数字引脚发送一定频率的方波，即高电平和低电平的输出，交替持续一段时间。每一组高电平和低电平的总时间一般是固定的，称为周期(注:周期的倒数是频率)。高电平输出的时间通常称为脉宽，占空比是脉宽(PW)与波形总周期(T)之比的百分比。高电平输出持续时间越长，占空比越长，模拟信号中相应的电压也就越高。下图显示了对应于脉冲宽度0%-100%的模拟信号电压在0V-3.3V(高电平为3.3V)之间的变化情况.

![](media/07831c118a4ce895fb317a6fa7bbf553.jpg)

PWM占空比越长，输出功率越高。既然我们了解了这种关系，我们就可以用PWM来控制LED的亮度或直流电机的速度等等。从上面可以看出，PWM并不是真实的模拟信号，电压的有效值等于相应的模拟信号。因此，我们可以控制LED和其他输出模块的输出功率，以达到不同的效果

树莓派Pico与 PWM

树莓派Pico板有16个PWM通道，每个PWM通道可以独立控制频率和占空比，时钟频率范围为7Hz到125MHz。树莓派Pico板上的每个引脚都可以配置为PWM输出。

项目电路图和接线图：

![](media/88f88727dc4c0adca334b96206f91d63.png)

![](media/6f9b5d2444827aab124a64d3236a02a9.png)

项目代码：

本项目设计使GP16输出PWM，脉宽由0%逐渐增加到100%，再由100%逐渐减小到0%。

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
04：呼吸灯”。并鼠标左键双击“Project_04_Breathing_Led.py”。

![](media/43e7015571c8b27b1829a13d9e895484.png)


项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/10584950246b67907a0b42eaf8b80994.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：电路中的LED从暗逐渐变亮，再从亮逐渐变暗，就像呼吸一样。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/d200890651b074b1f92e1ce5f2ec9cec.png)

![](media/e4789bf063f7fdca158b7a87011a02de.png)
![](media/3673c95868f245ee28365de8e51d2ced.png)





### 项目 05：交通灯

项目介绍：

交通灯在我们的日常生活中很普遍。根据一定的时间规律，交通灯是由红、黄、绿三种颜色组成的。每个人都应该遵守交通规则，这可以避免许多交通事故。在这个项目中，我们将使用树莓派Pico板和一些led(红，黄，绿)来模拟交通灯。

项目元件：











|![](media/77aa25aef55c00fcf0cd12143e34c688.jpg)|![](media/22d4b5c6b3ac4aaca2b9754904170b28.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|![](media/afa6edd3ff90b027a6f43995a6fb15a2.png)|![](media/0c1b0f91b4e56bcbc235d06b48809ac9.png)|
|-|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|公对母杜邦线若干|红色LED*1|黄色 LED*1|
|![](media/6c688493b558ed5f3e90e7dab38cbd93.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|![](media/f7784bea849600eb35d1a52730050dd2.png)|![](media/afa78dcb54297dc7dcbf7f8eefcfe3c2.png)|![](media/58935b6f12b1ff3e3cadec37761e12eb.png)|
|绿色LED*1|USB 线*1|220Ω电阻*3|面包板*1|跳线若干|




项目电路图和接线图：

![](media/9c89c43f423eb6c23526e513b4844e29.png)![](media/8d0c6e62f1beff634ace981de3ecf978.png)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2.
项目课程”→“项目05：交通灯”。并鼠标左键双击“Project_05_Traffic_Lights.py”。

![](media/2ff1cf39ef03c7b40a274f9f7d4c2c71.png)




项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/919100defe4c66cb3862bcf823ddda6d.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：1.首先，绿灯会亮5秒，然后熄灭；2.其次，黄灯会闪烁3次，然后熄灭；3.然后，红灯会亮5秒，然后熄灭；4.继续运行上述1-3个步骤。

按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/f57e40631072956d0d30a0a1a09fabde.png)





### 项目 06: RGB LED

项目介绍：

![](media/86fcb962ea63074253e247ce6e5c6faa.png)

RGB led由三种颜色(红、绿、蓝)组成，通过混合这三种基本颜色可以发出不同的颜色。在这个项目中，我们将向你介绍RGB LED，并向你展示如何使用树莓派Pico板控制RGB LED发出不同的颜色光。即使RGB LED是非常基本的，但这也是一个介绍自己或他人电子和编码基础的伟大方式。

项目元件：










|![](media/b2da57191e34efe5321aeee41421236b.jpg)|![](media/ec7e0d114256da11649153c981ba3119.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|![](media/f1a86fc81ab4b043263ce7e01e14d470.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|公对母杜邦线若干|RGB LED*1|
|![](media/f7784bea849600eb35d1a52730050dd2.png)|![](media/01e1718266f97a76fa59685d5d339430.png)|![](media/b08ceab591a290805836f21bc11ab107.png)||
|220Ω电阻*3|面包板*1|USB 线*1||




元件知识：

显示器大多遵循RGB颜色标准，电脑屏幕上的所有颜色都是由红、绿、蓝三种颜色以不同比例混合而成。

![](media/32abd117bdfbba2f79a0e156048b9d22.png)![](media/fc3074fc228ac47de33661bf1fa20fd1.png)

这个RGB LED有4个引脚，每个颜色(红，绿，蓝)和一个共同的阴极。为了改变RGB led的亮度，我们可以使用树莓派Pico板的PWM引脚。PWM引脚会给RGB led不同占空比的信号以获得不同的颜色。

如果我们使用3个10位PWM来控制RGBLED，理论上我们可以通过不同的组合创建210\*210\*210=
1,073,741,824(10亿)种颜色。

项目电路图和接线图：

![](media/22244be631cf2dfd46536d12fd8734a5.png)

![](media/c18f869a9b18fc521c3d09be942efebd.png)

注意：

RGB LED最长引脚(共阴极)连接GND。

![](media/25e0b9003dda1fbdb2677491d8026d4e.png)

怎样识别五色环220Ω电阻

![](media/c143fb8d355d4cb13056f3b2f15bd23c.png)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2.
项目课程”→“项目06：RGB”。并鼠标左键双击“Project_06_RGB_LED.py”。

![](media/15f498a9ed2ee6dcb55a296af85debaf.png)


项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/1bab4eb686297714d2faac9c72715df6.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：RGB LED开始显示随机颜色。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/b3ea9f4d0acc08b2e7be885a4ab5e182.png)





### 项目 07: 流水灯

项目介绍：

在日常生活中，我们可以看到许多由不同颜色的led组成的广告牌。他们不断地改变灯光(像流水一样)来吸引顾客的注意。在这个项目中，我们将使用树莓派Pico板控制10个leds实现流水的效果。

项目元件：










|![](media/b2da57191e34efe5321aeee41421236b.jpg)|![](media/68aa11662f0455d6b5f1965a29336313.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|![](media/3ec5906fad2172708d449390140f55e6.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|公对母杜邦线若干|红色LED*10|
|![](media/f7784bea849600eb35d1a52730050dd2.png)|![](media/01e1718266f97a76fa59685d5d339430.png)|![](media/58935b6f12b1ff3e3cadec37761e12eb.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|
|220Ω电阻*10|面包板*1|跳线若干|USB 线*1|




项目电路图和接线图:

![](media/002ba2e2074ba78b72c43635a4233ddc.png)

![](media/e3d6a1880f61fdfaec74360190f5ed43.png)

注意:

怎样连接LED

![](media/ce890a8f5f0aed0d9c33c34f57563d80.png)

怎样识别五色环220Ω电阻

![](media/c143fb8d355d4cb13056f3b2f15bd23c.png)

项目代码：

本项目是设计制作一个流水灯。这是这些行动：首先打开LED
\#1，然后关闭它。然后打开LED
\#2，然后关闭…并对所有10个LED重复同样的操作，直到最后一个LED关闭。这一过程反复进行，以实现流水的“运动”。

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
07：流水灯”。并鼠标左键双击“Project_07_Flowing_Water_Light.py”。

![](media/819ba8a66513850eb1bf3eb3fb4ed80c.png)


项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/68d166d5aaf24fcb9aee94bd89e330fd.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：10个LED将从左到右点亮，然后从右到左返回。按“Ctrl+C”或点单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/cfb384869b2b5c3284ac41714a01e8f9.png)

![](media/244d04c89963cb8d07bcb09281a01529.png)





### 项目 08: 一位数码管

项目介绍：

七段数码管是一种显示十进制数字的电子显示设备，广泛应用于数字时钟、电子仪表、基本计算器和其他显示数字信息的电子设备。甚至我们在电影中看到的炸弹也有七段数码管。也许七段数码管看起来不够现代，但它们是更复杂的点阵显示器的替代品，在有限的光线条件下和强烈的阳光下都很容易使用。在这个项目中，我们将使用树莓派Pico板控制一位数码管显示数字。

项目元件：











|![](media/b2da57191e34efe5321aeee41421236b.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|![](media/75e38d601750a4707369bc73d8028063.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|公对母杜邦线若干|一位数码管*1|
|![](media/f7784bea849600eb35d1a52730050dd2.png)|![](media/01e1718266f97a76fa59685d5d339430.png)|![](media/b08ceab591a290805836f21bc11ab107.png)||
|220Ω电阻*8|面包板*1|USB 线*1||




元件知识：

![](media/bc9e0030625cf7cf0716f7bc7245c31e.png)

一位数码管显示原理：数码管显示是一种半导体发光器件。它的基本单元是一个发光二极管(LED)。数码管显示根据段数可分为7段数码管和8段数码管。8段数码管比7段多一个LED单元(用于小数点显示)。七段LED显示屏的每段是一个单独的LED。根据LED单元接线方式，数码管可分为共阳极数码管和共阴极书案管。

在共阴极7段数码管中，分段LED的所有阴极(或负极)都连接在一起，你应该把共阴极连接到GND，要点亮一个分段LED，你可以将其关联的引脚设置为HIGH。

在共阳极7段数码管中，所有段的LED阳极(正极)都连接在一起，你应该把共阳极连接到+5V。要点亮一个分段LED，你可以将其关联的引脚设置为LOW。

![](media/492e7a8ed89a429826537d5e01152269.png)

数码管的每个部分由一个LED组成。所以当你使用它的时候，你也需要使用一个限流电阻。否则，LED会被烧坏。在这个实验中，我们使用了一个普通的共阴极一位数码管。正如我们上面提到的，你应该将公共阴极连接到GND。要点亮一个分段LED，你可以将其关联的引脚设置为HIGH。

项目电路图和接线图：

![](media/cdecc109f3d703edb67b372d8c05a696.png)

注意：插入面包板的七段数码管方向与接线图一致，右下角多一个点。

![](media/36b442a8810bd88409f73d53aea2b937.png)

![](media/1240fb0c10e8e14cac1151158d7f313d.png)

项目代码：

数字显示分7段，小数点显示分1段。当显示某些数字时，相应的段将被点亮。例如，当显示数字1时，b和c段将被打开。

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
08：一位数码管”。并鼠标左键双击“Project_08_One_Digit_Digital_Tube.py”。

![](media/de7eb8990401903056e7be3b93829953.png)


项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/7c4e1fa234e47869e0b37a635ffbe2b5.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：一位数码管将显示从9到0的数字。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/2c59a0dff81ad02fc034b8e700c0e8ad.png)





### 项目 09：四位数码管

项目介绍：

四位数码管是一种非常实用的显示器件，电子时钟的显示，球场上的记分员，公园里的人数都是需要的。由于价格低廉，使用方便，越来越多的项目将使用4位数码管。在这个项目中，我们使用树莓派Pico板控制四位数码管来显示数字。

项目元件：










|![](media/41f6f78847bbb5deee1b222a1f724e43.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/ffbfbf739e60ed2c41ae74001f2edcb2.png)|![](media/45c3b47dd070ae518f1b488571e334bc.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|220Ω 电阻*8|四位数码管*1|
|![](media/01e1718266f97a76fa59685d5d339430.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|![](media/b08ceab591a290805836f21bc11ab107.png)||
|面包板*1|公对母杜邦线若干|USB 线*1||




元件知识：

![](media/e5052450f4e01e32cdffcdefb587e942.png)

四位数码管：四位数码管有共阳极和共阴极两种四位数码管，显示原理是和一位数码管是类似的，都是8个GPIO口控制数码管的显示段，就是8个led灯，不过，这里是4位的，所以就还需要4个GPIO口来控制位选择端，就是选择哪个单个数码管亮，位的切换很快，肉眼区分不出来，就能看起来是多个数码管同时显示的了。

我们的四位数码管是共阴极的。

下图为4位数码管的引脚图，G1、G2、G3、G4就是控制位的引脚。

![](media/37113fa53213973132086c285d67686b.png)

下图为4位数码管内部布线原理图

![](media/bd7d7e0511842fbe694102ab148ed344.png)![](media/b8d701fa4c7cdb20bace4b78748ee169.png)

项目电路图和接线图：

![](media/4f64b9bf6b74ab49584f69c7465efa73.png)

![](media/c4bb871135269a61e7341e7a5360b70d.png)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
09：四位数码管”。然后鼠标左键双击“Project_09_Four_Digit_Digital_Tube.py”。

![](media/227a42fa3ebd671ad1e52efa1d55c76f.png)



项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/e84ac104b68ac5dd326e9cb5a0867d52.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：四位数码管显示数字，并在一个无限循环中重复这些动作。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/cfaf004c08f0961f2994eca716bf1e4f.png)





### 项目 10：8×8 点阵显示

项目介绍：

点阵屏是一种电子数字显示设备，可以显示机器、钟表、公共交通离场指示器和许多其他设备上的信息。在这个项目中，我们将使用树莓派Pico板控制8x8 LED点阵来逐渐点亮点阵。

项目元件：










|![](media/b2da57191e34efe5321aeee41421236b.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/db70c7bb9ebde2f658f133cdeb1bb8bb.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|8*8点阵屏*1|USB 线*1|
|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|![](media/ffbfbf739e60ed2c41ae74001f2edcb2.png)|![](media/01e1718266f97a76fa59685d5d339430.png)||
|公对母杜邦线若干|220Ω 电阻*8|面包板*1||




元件知识：

8\*8LED Matrix：8\*8点阵，就是由64个led灯组成，有行共阳极和行共阴极两种，我们的模块是行共阳极的，也就是每一行有一条线将LED的正极连到一起，列就是将LED灯的负极连接到一起，看下图：

![](media/69c719a7898907ab32f089f0cbbaff13.png)

![](media/bcfa2498367eaf9c7733da15af32eae7.png)

项目电路图和接线图：

![](media/788c542587a59d3c635134a5ba594e8a.png)

![](media/bf2e99950c446188b5ae4c767f99b9d3.png)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目 10：8×8
点阵显示”。然后鼠标左键双击“Project_10_8×8_Dot_Matrix_Display.py”。

![](media/2166fab59da5d3f0430f89d9d9676bec.png)

项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/4bc6e9ddad47bf26f0351cc758336c08.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：8\*8点阵屏显示字符“A”1S、显示字符“B”1S、显示字符“C”1S，然后滚屏显示字符串“Hello World”，反复循环。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/d352d0700dcccf68273cd9229028a562.png)





### 项目 11：74HC595N 控制 8 个LED

项目介绍：

在之前的项目中，我们已经学过了怎样点亮一个LED。

树莓派Pico板上只有26个IO端口，我们如何点亮大量的led呢?
有时可能会耗尽树莓派Pico板上的所有引脚，这时候就需要用移位寄存器扩展它。你可以使用74HC595N芯片一次控制8个输出，而只占用你的微控制器上的几个引脚。你还可以将多个寄存器连接在一起，以进一步扩展输出，在这个项目中，我们将使用树莓派Pico板，74HC595芯片和LED制作一个流水灯来了解74HC595芯片的功能。

项目元件：









|![](media/b2da57191e34efe5321aeee41421236b.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/db62d11edebf8ad4e639bf00bb11aadb.png)|
|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|74HC595N芯片*1|
|![](media/f7784bea849600eb35d1a52730050dd2.png)|![](media/01e1718266f97a76fa59685d5d339430.png)|![](media/58935b6f12b1ff3e3cadec37761e12eb.png)|
|220Ω电阻*8|面包板*1|跳线若干|
|![](media/3ec5906fad2172708d449390140f55e6.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|
|红色LED*8|USB 线*1|公对母杜邦线若干|




元件知识：

![](media/90f37be5fdb5724ae94ff0e572920645.png)

74HC595N芯片：简单来说就是具有8
位移位寄存器和一个存储器，以及三态输出功能。移位寄存器和存储器同步于不同的时钟，数据在移位寄存器时钟SCK的上升沿输入，在存储寄存器时钟RCK的上升沿进入的存储寄存器中去。如果两个时钟连在一起，则移位寄存器总是比存储寄存器早一个脉冲。移位寄存器有一个串行移位输入端（SI）和一个用于级联的串行输出端（SQH）,8位移位寄存器可以异步复位（低电平复位），存储寄存器有一个8位三态并行的总线输出，当输出使能（OE）被使能（低电平有效）将存储寄存器中输出至74HC595N的引脚（总线）。

![](media/168550ee46e0145a786608b49db42e45.png)

引脚说明：








|13引脚OE|是一个输出使能引脚，用于确保锁存器的数据是否输入到Q0-Q7引脚。在低电平时，不输出高电平。在本实验中，我们直接连接GND，保持低电平输出数据。|
|-|-|
|14引脚SI|这是74HC595接收数据的引脚，即串行数据输入端，一次只能输入一位，那么连续输入8次，就可以组成一个字节了。|
|10引脚SCLR|一个初始化存储寄存器管脚的管脚。在低电平时初始化内部存储寄存器。在这个实验中，我们连接VCC以保持高水平。|
|11引脚SCK|移位寄存器的时钟引脚，上升沿时，移位寄存器中的数据整体后移，并接收新的数据输入|
|12引脚RCK|存储寄存器的时钟输入引脚。上升沿时，数据从移位寄存器转存到存储寄存器中。这时数据就从Q0~Q7端口并行输出。|
|9引脚SQH|引脚是一个串行输出引脚，专门用于芯片级联，接下一个74HC595的SI端|
|Q0--Q7(15引脚，1-7引脚)|八位<a href="https://baike.baidu.com/item/%E5%B9%B6%E8%A1%8C/5806759">并行</a>输出端，可以直接控制数码管的8个段|




项目电路图和接线图：

![](media/36ef4afa4292ce69cb0a3e88d8a9ae37.png)

注意：需要注意74HC595N芯片插入的方向

![](media/39d34b80af0487eef9d8c2f60c3fefb1.png)
![](media/5a0de137092d094f6007098ac141586a.png)

![](media/2e9119dc12901caa560012602adf907c.png)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目 11：74HC595N
控制 8 个LED”。选择“my74HC595.py”，鼠标右键单击选择
“上载到/”，等待“my74HC595.py”被上传到Raspberry Pi Pico，然后鼠标左键双击“Project_11_74HC595N_Controls_8_LEDs.py”。

![](media/81dbca345ecac9fff390331e5104e907.png)

![](media/54c0169964ad286501a9e1406c0f4d56.png)




项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/15546545cb95893a562d9c0841b4a1bb.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：8个LED开始以流水模式闪烁。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/d1774a5447844881fa30bca8ea3cf004.png)





### 项目 12：有源蜂鸣器

项目介绍：

有源蜂鸣器是一个发声组件。它被广泛用作电脑、打印机、报警器、电子玩具、电话、计时器等的发声元件。它有一个内在的振动源，只需连接5V电源，即可持续发出嗡嗡声。在这个项目中，我们将使用树莓派Pico板控制有源蜂鸣器发出“滴滴”声。

项目元件：









|![](media/ef1f2f540eb42af5263d59d1773d0085.jpg)|![](media/f39510c60d4c43dfca4e26b0bdb9aae7.png)|![](media/01e1718266f97a76fa59685d5d339430.png)|
|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|面包板*1|
|![](media/9ab8162cf6d998b145c6fdb31ee9733f.png)|![](media/ffbfbf739e60ed2c41ae74001f2edcb2.png)|![](media/58935b6f12b1ff3e3cadec37761e12eb.png)|
|NPN型晶体管(S8050)*1|1kΩ电阻*1|跳线若干|
|![](media/4b4f653a76a82a3b413855493cc58fba.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|
|有源蜂鸣器*1|USB 线*1|公对母杜邦线若干|




元件知识：

![](media/ce75e9ae9489ba74e9d6312f04f24c7a.png)

有源蜂鸣器内部有一个简单的振荡器电路，可以将恒定的直流电转换成特定频率的脉冲信号。一旦有源蜂鸣器收到一个高电平，它将产生声音。而无源蜂鸣器是一种内部没有振动源的集成电子蜂鸣器，它必须由2K-5K方波驱动，而不是直流信号。这两个蜂鸣器的外观非常相似，但是一个带有绿色电路板的蜂鸣器是无源蜂鸣器，而另一个带有黑色胶带的是有源蜂鸣器。无源蜂鸣器不能区分正极性而有源极性蜂鸣器是可以。如下所示：

![](media/da420ccf4f666bfe09855faf3f8d8a7e.png)

![](media/9ab8162cf6d998b145c6fdb31ee9733f.png)

晶体管:
由于蜂鸣器需要很大的电流，ESP32输出能力的GPIO不能满足要求，这里需要一个NPN型晶体管来放大电流。晶体管，全称:半导体晶体管，是一种控制电流的半导体器件。晶体管可以用来放大微弱信号，也可以用作开关。它有三个电极(pin)：基极(b)，集电极(c)和发射极(e)。当电流通过“be”之间时，“ce”将允许几倍的电流通过(晶体管放大)，此时，晶体管在放大区工作。当“be”之间的电流超过某个值时，“ce”将不再允许电流增加，此时晶体管工作在饱和区。晶体管有两种类型如下所示：PNP和NPN

![](media/631232f1c8b8cd8e1f2369acad5bbd12.png)

PNP晶体管 NPN晶体管

在我们的套件中，PNP晶体管标记为8550,NPN晶体管标记为8050。

基于晶体管的特性，它常被用作数字电路中的开关。由于单片机输出电流的能力很弱，我们将使用晶体管来放大电流和驱动大电流的元件。在使用NPN晶体管驱动蜂鸣器时，通常采用以下方法：如果GPIO输出高电平，电流将流过R1，晶体管将传导，蜂鸣器将发出声音。如果GPIO输出低电平，没有电流流过R1，晶体管就不会传导，蜂鸣器也不会响。在使用PNP晶体管驱动蜂鸣器时，通常采用以下方法：如果GPIO输出低电平，电流将流过R1，晶体管将传导，蜂鸣器将发出声音。如果GPIO输出高电平，没有电流流过R1，晶体管就不会传导，蜂鸣器也不会响。

![](media/a7df0918f741543d7867cb6ba5b19248.png)

项目电路图和接线图：

![](media/8b84654a0f04d7e4c5f9c2f2923e577b.png)

![](media/6e607b53416c90c3573d3f890f8a5ed0.png)

注意：
1.该电路中蜂鸣器的电源为5V。在3.3V的电源下，蜂鸣器可以工作，但会降低响度。

2.VUSB应连接到USB线的正极，如果它连接到GND，它可能烧坏电脑或树莓派Pico板。同样，树莓派Pico板的36-40引脚接线时也要小心，避免短路。

3.有源蜂鸣器正极(“+”/长引脚)接引脚16，负极（短引脚）接GND。

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
12：有源蜂鸣器”。并鼠标左键双击“Project_12_Active_Buzzer.py”。

![](media/8905da9a098e432d49e924ecab112e8b.png)



项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/c800e00a8cc2641431143c932393d0e0.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：有源蜂鸣器发出“滴滴”声。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/3b8b46682e1ff277e7436185ce7948aa.png)





### 项目 13：无源蜂鸣器

项目介绍：

在之前的项目中，我们研究了有源蜂鸣器，它只能发出一种声音，可能会让你觉得很单调。这个项目将学习另一种蜂鸣器，无源蜂鸣器。与有源蜂鸣器不同，无源蜂鸣器可以发出不同频率的声音。在这个项目中，你将使用树莓派Pico板控制无源蜂鸣器发出警报声。

项目元件：









|![](media/928cde1cf2e6bce9bc7e4985a5a443b6.jpg)|![](media/48434ce34b111ef48f78bd7f777dbcfd.png)|![](media/01e1718266f97a76fa59685d5d339430.png)|
|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|面包板*1|
|![](media/9ab8162cf6d998b145c6fdb31ee9733f.png)|![](media/ffbfbf739e60ed2c41ae74001f2edcb2.png)|![](media/932156ef5c19e881846fd586bfdf3e58.png)|
|NPN型晶体管(S8050)*1|1kΩ电阻*1|跳线若干|
|![](media/9f966837bb106e93ae9a364410cb30ab.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|
|无源蜂鸣器*1|USB 线*1|公对母杜邦线若干|




元件知识：

![](media/e297a76d0228458774850e94bc2d2d86.png)

无源蜂鸣器是一种内部没有振动源的集成电子蜂鸣器。它必须由2K-5K方波驱动，而不是直流信号。这两个蜂鸣器的外观非常相似，但是一个带有绿色电路板的蜂鸣器是无源蜂鸣器，而另一个带有黑色胶带的是有源蜂鸣器。无源蜂鸣器不能区分正极性而有源极性蜂鸣器是可以。

![](media/fc42c5ed014609ff0b290ee5361bb2fd.png)

晶体管: 请参考项目12.

项目电路图和接线图:

![](media/0275036a6d6598f9b07a12dd928b1f4c.png)

![](media/0257f2526dcedd215a11ccbce45ded51.png)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
13：无源蜂鸣器”。并鼠标左键双击“Project_13_Passive_Buzzer.py”。

![](media/bf0f4bef7cd674d3c035ecb9453613fb.png)



项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/764558cc13ae07a2f1bbaaf7f48e4aa9.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：无源蜂鸣器发出警报声。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/e90d5ab4007cc82739cdcbc1768b5c7b.png)





### 项目 14: 小台灯

项目介绍：

你知道树莓派Pico可以在你按下按键的时候点亮LED吗?
在这个项目中，我们将使用树莓派Pico板，一个按键开关和一个LED来制作一个迷你台灯。

项目代码：











|![](media/ed6fb89a25714bda39c633feeff29f14.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/cb888dcfe9d95402f816d2f9d1553b82.png)|![](media/ef77f5a64c382157fc2dea21ec373fef.png)|![](media/c53059c29050b6fd9b35b88a0321b73f.png)|
|-|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|按键*1|红色 LED*1|10KΩ电阻*1|
|![](media/01e1718266f97a76fa59685d5d339430.png)|![](media/6ded325b684d7ce7ad4dc8667e55faf4.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|![](media/cd1926020a53e5ce90c7245e98f169e0.png)|![](media/24e2b42fd9706305d00da9337334c6ab.png)|
|面包板*1|220Ω电阻*1|USB 线*1|公对母杜邦线若干|按键帽*1|




元件知识：

![](media/20cd3dedd36a18709f7351e71aa06891.png)

按键：按键可以控制电路的通断，把按键接入电路中，不按下按键的时候电路是断开的，

一按下按键电路就通啦，但是松开之后就又断了。可是为什么按下才通电呢？这得从按键的内部构造说起。没按下之前，电流从按键的一端过不去另一端；按下的时候，按键内部的金属片把两边连接起来让电流通过。

按键内部结构如图：![](media/d2a204e61c768f18924150db58aee093.png)，未按下按键之前，1、2就是导通的，3、4也是导通的，但是1、3或1、4或2、3或2、4是断开（不通）的；只有按下按键时，1、3或1、4或2、3或2、4才是导通的。

在设计电路时，按键开关是最常用的一种元件。

按键的原理图:     
![](media/5bf7d624c266be0eb08ad0af3d9423d0.png)
![](media/f3b2e8858dc7fe21f2b14fa7c8e2318f.png)  
什么是按键抖动？

我们想象的开关电路是“按下按键-立刻导通”“再次按下-立刻断开”，而实际上并非如此。

按键通常采用机械弹性开关，而机械弹性开关在机械触点断开闭合的瞬间（通常
10ms左右），会由于弹性作用产生一系列的抖动，造成按键开关在闭合时不会立刻稳定的接通电路，在断开时也不会瞬时彻底断开。

![](media/0bfac90a1cbf919df0c91cfcb554725e.jpg)

那又如何消除按键抖动呢？

常用除抖动方法有两种：软件方法和硬件方法。这里重点讲讲方便简单的软件方法。

我们已经知道弹性惯性产生的抖动时间为10ms
左右，用延时命令推迟命令执行的时间就可以达到除抖动的效果。

所以我们在代码中加入了0.02秒的延时以实现按键防抖的功能。

![](media/033037b46dccc3e71c323fd5b85a5523.jpg)

项目电路图和接线图：

![](media/19f9dcfaacc32a6bc8ae16e362aa3122.png)

![](media/1c75a05a53faacfca9592631619909b0.png)

注意:

怎样连接LED

![](media/ce890a8f5f0aed0d9c33c34f57563d80.png)

怎样识别五色环220Ω电阻和五色环10KΩ电阻

![](media/c143fb8d355d4cb13056f3b2f15bd23c.png)

![](media/90cd61a4e564a3d40a6dbc8a84c85caf.png)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
14：小台灯”。并鼠标左键双击“Project_14_Mini_Table_Lamp.py”。

![](media/badb69d959c63987e4bd30e573a114aa.png)



项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/df5cc72623a1478af0c0ac7cf0653c5f.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：按下按钮，LED亮起；当按钮松开时，LED仍亮着。再次按下按钮，LED熄灭；当按钮释放时，LED保持关闭。是不是很像个小台灯？按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/1f40aa790525c5927c057cf108c865df.png)





### 项目 15：模拟沙漏

项目介绍：

古代人没有电子时钟，就发明了沙漏来测时间，沙漏两边的容量比较大，在一边装了细沙，中间有个很小的通道，将沙漏直立，有细沙的一边在上方，由于重力的作用，细沙就会往下流通过通道到沙漏的另一边，当细沙都流到下边了，就倒过来，把一天反复的次数记录下来，第二天就可以通过沙漏反复流动的次数而知道这一天大概的时间了。这一课我们将利用树莓派Pico板控制倾斜开关和LED灯来模拟沙漏，制作一个电子沙漏。

项目元件：










|![](media/c734b603b25d941a4cd40331d09cdadd.jpg)|![](media/a148c40620767714cde78f41a4822528.png)|![](media/cc0cc1152ecce1bf3966843884df0feb.png)|![](media/ef77f5a64c382157fc2dea21ec373fef.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|倾斜开关*1|红色 LED*4|
|![](media/01e1718266f97a76fa59685d5d339430.png)|![](media/6ded325b684d7ce7ad4dc8667e55faf4.png)|![](media/b08ceab591a290805836f21bc11ab107.png)||
|面包板*1|220Ω电阻*4|USB 线*1||
|![](media/c53059c29050b6fd9b35b88a0321b73f.png)|![](media/4569c99dc435bb87a0105c0c59865b14.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)||
|10KΩ电阻*1|跳线若干|公对母杜邦线若干||




元件知识：

![](media/5d86192d9250610d059178115cc9908d.png)

倾斜开关也叫数字开关。里面有一个可以滚动的金属球。采用金属球滚动与底部导电板接触的原理来控制电路的通断。当倾斜开关是滚珠型倾斜感应单方向性触发开关，当倾斜传感器向触发端（两根金属脚端）倾斜时，倾斜开关处于闭路状态，模拟端口的电压约为5V(二进制数为1023)。这样，LED会亮起。当倾斜开关在水平位置或向另一端倾斜时，倾斜开关处于开路状态，模拟端口的电压约为0V(0二进制)。LED将会关闭。在程序中，我们根据模拟端口的电压值，是否大于2.5V(512二进制)来判断开关是开还是关。

这里用倾斜开关的内部结构来说明它是如何工作的，显示如下图：

![](media/40bc569b295c4656bd973da4ad8734e2.png)

项目电路图和接线图：

![](media/033b2d8368f73658fff3b00d8508e4f3.png)

![](media/157dda6c8dad94ceddcb2cea06f69f03.png)

注意: 怎样连接LED

![](media/ce890a8f5f0aed0d9c33c34f57563d80.png)

怎样识别五色环220Ω电阻和五色环10KΩ电阻

![](media/f2bfc6ab06a23f63f34c568c6e81bae6.png)

![](media/94a604b7703f1dbf8a9602281dced30a.png)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
15：模拟沙漏”。并鼠标左键双击“Project_15_Tilt_And_LED.py”。

![](media/ee2caa6b9c4390f34f8253e7f89d3e8d.png)



项目结果：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/9dbc51566b432d6b567e65fbacd48719.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：将面包板倾斜到一定角度，led就会一个一个地亮起来。当回到上一个角度时，led会一个一个关闭。就像沙漏一样，随着时间的推移，沙子漏了出来。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/e4ca0baf42928596704cf6749f267797.png)





### 项目 16： I2C 128×32 LCD

项目介绍：

在生活中，我们可以利用显示器等模块来做各种实验。你也可以DIY各种各样的小物件。例如，用一个温度传感器和显示器做一个温度测试仪，或者用一个超声波模块和显示器做一个距离测试仪。下面，我们将使用LCD_128X32_DOT模块作为显示器，将其连接到树莓派Pico板上。将使用树莓派Pico板控制LCD_128X32_DOT显示屏显示各种英文文字、常用符号和数字。

项目元件： 









|![](media/9e2519c3369fb0dce36a3f781a74d854.jpg)|![](media/7b6eee3c5a625e147ac57dc985541456.png)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|
|-|-|-|
|树莓派Pico板*1|LCD_128X32_DOT*1|树莓派Pico板的扩展板*1|
|![](media/bb2e8f8e67a0a368fc2e88bc70aa676e.png)|![](media/d10037500a471b569ef04e12563197b7.png)||
|4P 转杜邦线母单*1|USB 线*1||




元件知识：

![](media/655fcd0c190a8d9a2ecebaee5409a684.png)

LCD_128X32_DOT：一个像素为128\*32的液晶屏模块，它的驱动芯片为ST7567A。模块使用IIC通信方式，同时，代码中包含所有英文字母和常用符号的库，可以直接调用。使用时，我们还可以在代码中设置，让英文字母和符号显示不同文字大小。为了方便设置图案显示，我们还提供一个取模软件，可将特定的图案转化成控制代码，然后直接复制到测试代码中使用的。

LCD_128X32_DOT原理图：

![](media/3e711eec526dd1118efdf03e72a4ebd4.png)

LCD_128X32_DOT技术参数：

显示像素：128\*32 字符

芯片工作电压：4.5 ~ 5.5V

工作电流：100mA (5.0V)

模块最佳工作电压：5.0V

项目接线图：

![](media/b3820b1176c13ba40651f654686a783f.png)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目 16： I2C 128×32 LCD”。分别选择“lcd128_32.py”和 “lcd128_32_fonts.py”，右键单击鼠标选择
“上载到/”，等待“lcd128_32.py”和 “lcd128_32_fonts.py”被上传到Raspberry Pi Pico，并鼠标左键双击“Project_16_I2C_128_32_LCD.py”。

![](media/e22f6cc9236fef66d5ab5fa62eb9c734.png)

![](media/852e0a450da11832e034e5edf0c5d4f3.png)

![](media/9befda999acc6ca4b261ba0a31c98847.png)



项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/f700aaa4fe8618b36365bf734eb09652.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：128X32LCD模块显示屏第一行显示“keyes”、第二行显示“ABCDEFGHIJKLMNOPQR”、第三行显示“123456789+-\*/\<\>=$@”、第四行显示“%^&(){}:;'|?,.~\\\[\]”。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/1d2902e2a5ed5138dc103c372887927c.png)





### 项目 17：小风扇

项目介绍：

在炎热的夏季，需要电扇来给我们降温，那么在这个项目中，我们将使用树莓派Pico板控制直流电机模块和小扇叶来制作一个小电扇。

项目元件：










|![](media/572d1cc8d97416a7e6d6988426d233a8.jpg)|![](media/a148c40620767714cde78f41a4822528.png)|![](media/81a0bb00979d34381e5b70be7da3cd32.png)|![](media/9ab8162cf6d998b145c6fdb31ee9733f.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|跳线若干|S8050三极管*1|
|![](media/d02ed1417ee96d7a269a4bbd2f1a50e0.png)|![](media/f294b98cdf203f94dccd13e8dfb4254a.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|![](media/9ab8162cf6d998b145c6fdb31ee9733f.png)|
|二极管*1|面包板*1|USB 线*1|S8550三极管*1|
|![](media/172a77f56de41c440855ba2e8b135b7f.jpg)|![](media/655e6c465cb423279e0908513a983711.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)||
|直流电机*1|风扇片*1|公对母杜邦线若干||




项目电路图和接线图1：

（这个实验是使用S8050（NPN型三极管）控制电机）

![](media/46c58d08b620affe397434e091ebec92.png)

![](media/fc2855b59124fbfa71a6d4ba96869034.png)

项目代码1：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
17：小风扇”。并鼠标左键双击“Project_17.1\_ Small_Fan.py”。

![](media/e79f6a35371fd34ae3847e68f741b460.png)



项目现象1：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/e1b16a88a67b2088dfc4d041d41a086d.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：将小风扇片安装到直流电机上，上电后，可以看到电机转动4秒，停止2秒，以此规律重复执行。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/3b957dff9489a761e91992a550d1eb59.png)

项目电路图和接线图2：

（这个实验是使用S8550（PNP型三极管）控制电机）

![](media/d33d94a0e05ebd3fb986d07f540588c7.png)

![](media/a13d2691755474c34753ac38e8d00479.png)

项目代码2：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
17：小风扇”。并鼠标左键双击“Project_17.2\_ Small_Fan.py”。

![](media/292967edd58598a3b27981722881536b.png)


项目现象2：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/15c277d57c3c44c6044a4e5e95fcc801.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：将小风扇片安装到直流电机上，上电后，可以看到电机转动4秒，停止2秒，以此规律重复执行。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/470f30c191d3bb008876acb7c31d58f6.png)





### 项目 18：调光灯

项目介绍：

电位器是一个带有滑动或旋转触点的三端电阻器，它形成一个可调的分压器。它的工作原理是在均匀电阻上改变滑动触点的位置。在电位器中，整个输入电压被施加到电阻的整个长度上，输出电压是固定触点和滑动触点之间的电压值。在这个项目中，我们将学习使用树莓派Pico板读取电位器的值，并结合LED制作一个调光灯。

项目元件：










|![](media/9e2519c3369fb0dce36a3f781a74d854.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/122b9239c3eb6fb99e2e10037d649e01.png)|![](media/ef77f5a64c382157fc2dea21ec373fef.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|可调电位器*1|红色 LED*1|
|![](media/01e1718266f97a76fa59685d5d339430.png)|![](media/6ded325b684d7ce7ad4dc8667e55faf4.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|
|面包板*1|220Ω电阻*1|公对母杜邦线若干|USB 线*1|




元件知识：

![](media/122b9239c3eb6fb99e2e10037d649e01.png)

可调电位器：可调电位器是电阻和模拟电子元件的一种，具有0和1两种状态(高电平和低电平)。模拟值不同，其数据状态呈现为1
~ 1024等线性状态。

读取电位器的ADC值和电压值：

我们将电位器连接到树莓派Pico板的模拟IO口上来读取电位器的ADC值和电压值。接线请参照以下接线图：

![](media/fb36b9b05a5082fe9255b42eb90cf330.png)

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
18：调光灯”。并鼠标左键双击“Project_18.1_Read_Potentiometer_Analog_Value.py”。

![](media/ec493694352ceb9709dde555b8730249.png)



确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/6e0a45421aa94ddc73e4315e708f30a1.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：Thonny IDE下的“Shell”窗口将打印出电位器的ADC值和电压值，转动电位器手柄时，ADC值和电压值发生变化。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/f92286fc3a434c99701725313e5adb2d.png)

![](media/da8d3d6726ec47a3d6bb527752309158.png)

调光灯的电路图和接线图：

在前面一步，我们读取了电位器的ADC值和电压值，现在我们需要将电位器的ADC值转换成LED的亮度，来做成一个亮度可调的灯。见如下所示接线图：

![](media/efd7dd23c296c8f8ca18771bb2f1a89c.png)

![](media/b08506476d0321b6040e38ce2992f775.png)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
18：调光灯”。并鼠标左键双击“Project_18.2_Dimming_Light.py”。

![](media/c1256e9803ba96c598a4eed06a109163.png)



项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/c1ae8b710cbc66a555d446b336879540.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：转动电位器手柄，LED的亮度会相应地改变。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/8bb2c8090d4d263cd6d8f8a6ad4fc590.png)

![](media/2211121ed8269149f09a3eda2ea90b88.jpg)





### 项目 23：火焰警报器

项目介绍：

火灾是一种可怕的灾害，火灾报警系统在房屋，商业建筑和工厂中是非常有用的。在本项目中，我们将使用树莓派Pico板控制火焰传感器，蜂鸣器和LED来模拟火灾报警装置。这是一个有意义的创客活动。

项目元件：











|![](media/11b9006b78651dcc1dcb4bf970c250ee.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/3aa16b28e1970e2aa3ce9a38fd1442e6.png)|![](media/ef77f5a64c382157fc2dea21ec373fef.png)|![](media/4b4f653a76a82a3b413855493cc58fba.png)|
|-|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|火焰传感器*1|红色 LED*1|有源蜂鸣器*1|
|![](media/f07338d72477c14b6c1ceccb43c575de.png)|![](media/f6b5bab63b7f305f238771e844d808f6.png)|![](media/892254c94308d032ecdad65b888557a0.png)|![](media/bbb9bbd7cfe4da1b1ae6d69f0946d920.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|
|面包板*1|220Ω电阻*1|10KΩ电阻*1|跳线若干|USB 线*1|
|![](media/9ab8162cf6d998b145c6fdb31ee9733f.png)|![](media/65f8db274ab3e56cbb2c434b89f6f4f7.png)|![](media/79c373b80745929aeea14eac48e52fb4.png)|||
|NPN型晶体管(S8050)*1|1kΩ电阻*1|公对母杜邦线若干|||




元件知识：

![](media/b393eb939bcbc888da7a345cc9702157.png)

火焰会发出一定程度的IR光，这种光人眼是看不到的，但我们的火焰传感器可以检测到它，并提醒微控制器（如树莓派Pico板）已经检测到火灾。它有一个专门设计的红外接收管来探测火焰，然后将火焰亮度转换为波动水平信号。接收三极管的短引脚是负极，另一个长引脚是正极。我们应该连接短引脚（负极)到5V，连接长引脚(正极)到模拟引脚，一个电阻和GND。如下图所示：

![](media/c0a5ada5a6b624a0f0445f2c46c86839.jpg)

注意：火焰传感器应避开日光、汽车头灯、白炽灯直接照射，也不能对着热源(如暖气片、加热器)或空调，以避免环境温度较大的变化而造成误报。同时还易受射频辐射的干扰。

读取火焰传感器模拟值：

我们首先用一个简单的代码来读取火焰传感器的模拟值，并将其打印出来。接线请参照以下接线图：

![](media/2b4e0cf420a0a94d6dfdd184f06fae33.png)

![](media/01e87dc7a2a23c003484d6f6ab2c8773.png)

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
19：火焰警报器”。并鼠标左键双击“Project_19.1_Read_Analog_Value.py”。

![](media/85a2ed91a58f2731cfd30409d5b67ee9.png)




确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/5e856b2164104ef6274446d1e11ef8eb.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：Thonny IDE下的”Shell”窗口将打印火焰传感器读取的模拟值，当火焰靠近火焰传感器时，模拟值增大；反之，模拟值减小。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/f12780af147d70793dca3b445acf3d4c.png)

![](media/f0bb1750676a3226f103c71efa82a7d7.png)

火焰报警的电路图和接线图：

接下来，我们将使用火焰传感器和蜂鸣器、LED制作一个有趣的项目——火灾报警装置。当火焰传感器检测到火焰时，LED闪烁，蜂鸣器报警。

![](media/2f4b0e24a35b7e5b90e7577bd4fa13b5.png)

![](media/897914ede2a0a221bff1da80d7ead221.png)

项目代码：（注意：![](media/ae89b4a3402bbbe24daf933b675bb69e.png)代码中的阀值500可以根据实际情况自己重新设置）

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
19：火焰警报器”。并鼠标左键双击“Project_19.2_Flame_Alarm.py”。

![](media/dc0a6bc13dd8ea851fbe069d5faa522d.png)



项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/85c5aa458d7102c0e3f723d79f59a635.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：当火焰传感器检测到火焰时，LED闪烁，蜂鸣器报警；否则，LED不亮，蜂鸣器不响。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/c8020cec98e9bda2cef8adc5c9e480d2.png)





### 项目 20：小夜灯

项目介绍：

传感器或元件在我们的日常生活中是无处不在的。例如，一些公共路灯在晚上会自动亮起，而在白天会自动熄灭。为什么呢?
事实上，这些都是利用了一种光敏元件，可以感应外部环境光强度的元件。晚上，当室外亮度降低时，路灯会自动打开；到了白天，路灯会自动关闭。这其中的原理是很简单的，在本实验中我们使用树莓派Pico板控制LED就来实现这个路灯的效果。

项目元件：











|![](media/ee7e8566bc7c7b0d39df0d5cee4cf468.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/3ab022b34dfb14b2cce66bfac3bd15b4.png)|![](media/ef77f5a64c382157fc2dea21ec373fef.png)|![](media/698d84e9dc3b34fd6be7c7d21a51c80d.png)|
|-|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|光敏电阻*1|红色 LED*1|10KΩ电阻*1|
|![](media/01e1718266f97a76fa59685d5d339430.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|![](media/0bf747dcc565c53ac29e4709f7d486d8.png)|![](media/87d80ddcedd37fc51c4300e3feda80db.png)|![](media/6ded325b684d7ce7ad4dc8667e55faf4.png)|
|面包板*1|公对母杜邦线若干|跳线若干|USB 线*1|220Ω电阻*1|




元件知识：

![](media/b69142448f92d1941c6fd33b0132ce7b.png)

光敏电阻：是一种感光电阻，其原理是光敏电阻表面上接收亮度(光)降低电阻，光敏电阻的电阻值会随着被探测到的环境光的强弱而变化。有了这个特性，我们可以使用光敏电阻来检测光强。光敏电阻及其电子符号如下：

![](media/7d575da675a2f6cb511d28b801e2abaa.png)

下面的电路是用来检测光敏电阻电阻值的变化：

![](media/764b1be2b594898743043fc409eefe91.png)

在上述电路中，当光敏电阻的电阻因光强的变化而改变时，光敏电阻与电阻R2之间的电压也会发生变化。因此，通过测量这个电压就可以得到光的强度。

读取光敏电阻的模拟值：

我们首先用一个简单的代码来读取光敏电阻模拟值，并将其打印出来。接线请参照以下接线图：

![](media/68337a2b734098f3bf0ad3fe5409dd2c.png)

![](media/a12cd4a08876876ff91108f77830049c.png)

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
20：小夜灯”。并鼠标左键双击“Project_20.1_Read_Photosensitive_Analog_Value.py”。

![](media/a941f847de4f971784e029da50bcb26c.png)




确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/0b603933247b962602ff2a14b6dfe945.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：Thonny IDE下的”Shell”窗口将打印光敏电阻读取的模拟值，当逐渐减弱光敏电阻所处环境中的光线强度时，模拟值逐渐增大；反之，模拟值逐渐减小。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/7ea93bb5931f4e9fb4421a47089768a4.png)

![](media/bd033f8067d0a1039cad35538eeb2824.png)

光控灯的电路图和接线图：

我们在前面做了一个小小的调光灯，现在我们来做一个光控灯。它们的原理是相同的，即通过Raspberry Pi Pico获取传感器的模拟值，然后调节LED的亮度。

![](media/aa30cb49386538a6ff5e5cd12a8383cd.png)

![](media/d34c5f9f70d90d560be98038169c270d.png)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
20：小夜灯”。并鼠标左键双击“Project_20.2_Night_Lamp.py”。

![](media/3db8996e3a0233eb6f24e5392da4cfe5.png)



项目结果：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/6d3e757b0db82dea6973684073c9e07f.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：当减弱光敏电阻所处环境中的光线强度时，LED变亮，反之，LED变暗。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/079ad99176610af54922b431b5f8b96f.png)





### 项目 21：温度仪表

项目介绍：

热敏电阻是一种电阻，其阻值取决于温度和温度的变化，广泛应用于园艺、家庭警报系统等装置中。因此，我们可以利用这一特性来制作温度计。

项目元件：









|![](media/08f762db18e5fd42f163740d4c2ce4fd.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|
|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|公对母杜邦线若干|
|![](media/06b78e3697de1bb564b007ebdcf0581b.png)|![](media/01e1718266f97a76fa59685d5d339430.png)|![](media/f83602237e22f7841b3f4388955c57d3.png)|
|LCD_128X32_DOT*1|面包板*1|热敏电阻*1|
|![](media/bb2e8f8e67a0a368fc2e88bc70aa676e.png)|![](media/87d80ddcedd37fc51c4300e3feda80db.png)|![](media/698d84e9dc3b34fd6be7c7d21a51c80d.png)|
|4P 转杜邦线母单*1|USB 线*1|10KΩ电阻*1|




元件知识：

热敏电阻：热敏电阻是一种温度敏感电阻。当热敏电阻感应到温度的变化时，它的电阻就会发生变化。我们可以利用热敏电阻的这种特性来检测温度强度。热敏电阻及其电子符号如下所示。

![](media/809b8634747fb295021f12e3b92b7894.png)

热敏电阻的电阻值与温度的关系为：

![](media/04312ac83502354f253ae6cba9f005dd.wmf)

式中：

Rt为热敏电阻在T2温度下的电阻；

R为热敏电阻在T1温度下的标称阻值；

EXP\[n\]是e的n次幂；

B为温度指数；

T1，T2是开尔文温度(绝对温度)，开尔文温度=273.15
+摄氏温度。对于热敏电阻的参数，我们使用：B=3950, R=10KΩ，T1=25℃。热敏电阻的电路连接方法与光敏电阻类似，如下所示：

![](media/ac0d68aac58bffa5c99e1d0ed3a8bc37.jpeg)

我们可以利用ADC转换器测得的值来得到热敏电阻的电阻值，然后利用公式来得到温度值。因此，温度公式可以推导为：

![](media/7d6cc89970b6158b40707eb7b5d3b0d5.wmf)

读取热敏电阻的值：

首先我们学习热敏电阻读取当前的ADC值、电压值和温度值，并将其打印出来。请按下面的接线图接好线：

![](media/d1cc8f28e153531547d11ea977c37eca.png)

![](media/934f77b466c3f5391233dbbe62afecd6.png)

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
21：温度仪表”。并鼠标左键双击“Project_21.1_Read_the_thermistor_analog_value.py”。

![](media/305569855834fb51a46ed7a65c0928d6.png)


确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/95391fd4ce686d5b23635ddd303ea183.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：Thonny IDE下的”Shell”窗口将不断显示热敏电阻当前的ADC值、电压值和温度值。试着用食指和拇指捏一下热敏电阻(不要碰触导线)一小段时间，你应该会看到温度值增加。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/554eb515f1d2466925ab364cd98a22eb.png)

![](media/0a035900fbc73a112eced64a926872ad.png)

温度仪表电路图和接线图：

![](media/458af2aaa2a441e37e460179529084f7.png)

![](media/6972a3f15894404f7b6c13aa3ab45517.png)

项目代码：

本项目中使用的代码保存在文件夹“3. Python 教程\1. Windows 系统\2.
项目课程”中。你可以把代码移到任何地方。例如，我们将“2.
项目课程”文件夹保存在Disk(D)中，路径为D:\2. 项目课程。

打开“Thonny”软件，点击“此电脑”→“D:”→“2. 项目课程”→“项目
21：温度仪表”。分别选择“lcd128_32.py”和
“lcd128_32_fonts.py”，右键单击鼠标选择 “上载到 /”，等待“lcd128_32.py”和
“lcd128_32_fonts.py”被上传到Raspberry Pi Pico。并鼠标左键双击“Project_21.2_Temperature_Instrument.py”。

![](media/2870f1a49a3140c42fd4e12817aa9a06.png)

![](media/6462b7a342bc70d32a2c96ec0c668e35.png)

![](media/037d40db3e8ac545caa7027bbf813337.png)




项目现象：

确保树莓派Pico板已经连接到电脑上，单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”。

![](media/df99f41849032538c937c36d7e52b164.png)

单击![](media/da852227207616ccd9aff28f19e02690.png)“运行当前脚本”，代码开始执行，你会看到的现象是：LCD 128X32 DOT的屏幕上显示热敏电阻的电压值和当前环境中的温度值。按“Ctrl+C”或单击![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“停止/重启后端进程”退出程序。

![](media/172a15ed122fa918c41d09425eb15333.png)





