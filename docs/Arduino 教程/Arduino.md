# Arduino

## Arduino软件

1.安装Windows驱动程序

![](media/6cf6312dc7c7db27794b54d58a8bf80c.png)

### 1.1.下载安装arduino软件： 

（1）首先，进入arduino官方网站：[<u>https://www.arduino.cc/</u>](https://www.arduino.cc/)
，点击“SOFTWARE”进入下载页面，如下图所示：

![](media/e5f2b2b7d63ae674b2ddce5abc4eebf8.png)

![](media/e74472bf31c762e0c38db3cbae7640f2.png)

（2）然后，根据你的操作系统选择并下载相应的安装程序。如果你是Windows用户，请选择“Windows安装程序”下载正确的安装驱动程序。

![](media/6aae01e362ce3b059be463f5561d52ee.png)

选择点击Windows Win7 and newer下载Arduino 1.8.16版本的安装程序，需要手动安装。而当点击Windows ZIP file时，Arduino 1.8.16版本的zip文件将被直接下载，只需要解压缩它就可以完成安装。

![](media/a983a2f2eceb968afbff8ba0f0376240.png)

一般情况下，点击JUST DOWNLOAD就可以下载了，当然如果你愿意，你可以选择小小的赞助，以帮助伟大的Arduino开源事业。

（3）Arduino软件下载完成后，继续安装，当你收到操作系统的警告时，请允许驱动程序安装。首先点击I Agree, 然后选择好要安装的组件后再点击Next。

![](media/00e334d3c756a2495da6f0d1b2db680a.png)

![](media/de541d90a1cda992ad8e3f0cbaf95f94.png)

（4）选择安装目录(我们建议保持默认目录)，然后点击Install。

![](media/7da9aca1e8432c59372e7c7ab2574bd9.png)

（5）如果出现以下界面，则应选择Install。

![](media/7ed9e80a34185295e438910c641d8b1c.png)

该过程将提取并安装所有必需的文件，以正确执行Arduino软件(IDE)。

![](media/739c41701fbcab202f0e587f534bad30.png)

安装完成后，会在桌面上生成一个Arduino 软件快捷方式。

![](media/d28223c55a30f949760779720fe4ec24.png)

在电脑桌面上点击Arduino 软件快捷方式打开Arduino IDE.

![](media/47de9686901274baacefd7638a8469dd.png)

点击“File”→“Preferences”，选择“简体中文”之后点击“好”。这样就对语言进行设置好了。

![](media/b762984b211060a12c205d34f40e4757.png)

关掉Arduino IDE，重新点击Arduino 软件快捷方式打开Arduino IDE。这样，英文页面就转化成中文页面。

![](media/d9b99e7211a4e1c89a0fb1e3f76ae7f1.png)

![](media/a87643ad6add031d88bd02c89e3979f6.png)

A - 用于检查是否存在任何编译错误。

B - 用于将程序上传到Arduino控制板。

C - 用于创建新草图的快捷方式。

D - 用于直接打开示例草图之一。

E - 用于保存草图。

F - 用于从板接收串行数据并将串行数据发送到板的串行监视器。

### 1.2.安装开发板Pico 

（1）网络连接良好的情况下，打开Arduino IDE，单击“工具”→“开发板”→“开发板管理器...”。

![](media/5a3dfef428f88c534008d399872452fd.png)

2.  在搜索框中输入Pico，选择Arduino Mbed OS RP2040     Boards，点击安装或更新。

![](media/74cd23192bb1a69c6546e520322e51db.png)

（3）安装过程中，当你收到操作系统的安全警告时，请单击安装允许设备软件安装。

![](media/2da765cc4a6170158eb111fa216968d0.png)

（4）安装完成后，单击关闭就可以了。

![](media/65ca81ebf2e5f43a778bbbc0f6507fdd.png)

### 1.3.上传Arduino兼容的Pico固件 

如果你的树莓派Pico板是新的，想使用Arduino学习和开发，则需要上传一个Adruino兼容的Pico固件。请参考以下步骤配置:

（1）断开树莓派Pico板与电脑的连接。继续按树莓派Pico板上的白色按钮(BOOTSEL)，并在松开按钮前将树莓派Pico板连接到电脑。(注意：MicroUSB线连接到树莓派Pico板前一定要一直按住按钮，否则固件下载不会成功)

![](media/33c91d51b2aeb2c943691706354aaad1.png)

（2）打开Arduino IDE，单击 文件→示例→01.Basics→Blink。

![](media/7e167543e6b11be5d3b09650ee45aa4a.png)

（3）单击工具→开发板:→Arduino Mbed OS RP2040 Boards→Raspberry Pi Pico。

![](media/b69e30d6dba33777ce9c336cb59616dd.png)

（4）上传草图（Blink）到 Raspberry Pi Pico。

![](media/ea5d8185fa6662a1eb3564a8da01f743.png)

当草图完成上传时，可以看到以下提示。

![](media/5497cc6362c67b70c57d02fd64566aa6.png)

树莓派Pico板上的指示灯开始闪烁。

![](media/8d5c1a4fe5c7e88ff85a0f9ea5f81195.png)
![](media/e4f6aebf04026ffc3d4b4f0e71938454.png)

1秒

单击工具→端口→COMx(Raspberry Pi Pico)。COMx的X在不同的电脑上是不同的。请在你的电脑上选择正确的COM口。在这个的例子中，它是COM15。

![](media/4ab732d138b2b9453c07df3ff6be2e4d.png)

注意:

1.  第一次使用Arduino上传Raspberry Pi     Pico的草图时，不需要选择端口。之后，每次上传草图前，请检查端口是否已选择;否则可能导致代码上传失败。

2.  有时在使用时，Raspberry Pi     Pico可能会由于代码丢失固件而无法工作。此时，你可以如上所述步骤上传Raspberry     Pi Pico的固件。

2.  安装MAC驱动程序

![](media/14306877671603761f7451ae0b2dc951.png)

### 2.1.下载安装Arduino IDE: 

![](media/5d58d3cf67b308423ddb9f286f6cb697.png)

接下来的操作类似于Windows系统，可以参考上面的Windows系统操作过程。





## 项目教程

### 项目 01: Hello World

项目介绍：

对于树莓派Pico初学者，我们将从一些简单的东西开始。在这个项目中，您只需要一个树莓派Pico板和USB线来完成“Hello World!”项目。它不仅是树莓派Pico板和PC的通信测试，也是树莓派Pico板的初级项目。

项目元件：

|![](media/ea4c22ac79b4e3cf9c6185c6ccf3717a.jpg)|![](media/3bdcc62cfa661d2b860a76e28537e21e.png)|
|-|-|
|树莓派Pico板*1|USB 线*1|

项目接线：

在本项目中，我们通过USB线将树莓派Pico板和电脑连接起来。

![](media/bbebdf7f2c0f4c223b6f2548d7ff6607.png)![](media/ea4c22ac79b4e3cf9c6185c6ccf3717a.jpg)

在上传项目代码到树莓派Pico板之前，请检查Arduino IDE的配置。

单击“工具”，确认板型和端口如下所示：

![](media/4984d5958eb182fabaa9927a95e77b24.png)

单击![](media/b0d41283bf5ae66d2d5ab45db15331ba.png)将项目代码上传到树莓派Pico板。

![](media/7553cbc6e5cf1a09daa27a89a801265e.png)

项目代码上传成功！

![](media/b242b0f515977611a11a0dbf7c2b45b9.png)

项目结果：

项目代码上传成功后，单击![](media/2f6bca56f724e45a855335cb53ae9b4e.png)图标进入串行监视器，设置波特率为115200，在文本框输入字母“R”，单击“Send”，这样串口监视器打印“Hello World!”。

![](media/911fa67e44930f0adef01356c7bc0bb9.png)

### 项目 02：板载灯闪烁

项目介绍： 

树莓派Pico板上有个板载LED，这个LED是固定接在树莓派Pico板上的GP25引脚，在这个项目中，我们将来学习使板载LED闪烁。

项目元件：

|![](media/ea4c22ac79b4e3cf9c6185c6ccf3717a.jpg)|![](media/3bdcc62cfa661d2b860a76e28537e21e.png)|
|-|-|
|树莓派Pico板*1|USB 线*1|

项目接线：

在本项目中，我们通过USB线将树莓派Pico板和电脑连接起来

![](media/bbebdf7f2c0f4c223b6f2548d7ff6607.png)![](media/ea4c22ac79b4e3cf9c6185c6ccf3717a.jpg)

树莓派Pico板上的板载LED是由GP25控制，当GP25输出高电平时，LED点亮;当输出低时，LED灯关闭。

在上传项目代码到树莓派Pico板之前，请检查Arduino IDE的配置。

单击“工具”，确认板型和端口如下所示：

![](media/7c55e85a695889210190733fe4d24666.png)

单击![](media/b0d41283bf5ae66d2d5ab45db15331ba.png)将项目代码上传到树莓派Pico板。

![](media/f8e0b27ed60d19ef44857a62644220c6.png)

项目代码上传成功！

![](media/51caf4d91a0ba29cb9c5f78575db7f1b.png)

项目结果：

项目代码上传成功后，利用USB线上电，可以看到的现象是：树莓派Pico板的LED开始闪烁，循环进行。

![](media/e12ecf9006915a143134d18d53643ee4.png)
![](media/6f49241878e04e8ba4edd30fb2714249.png)

1秒

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

![](media/793740d0b936e516ca354111e2d0eb79.png)

10KΩ 电阻*10

![](media/18484e5d16b6d89c63825cc2efa6a543.png)

1KΩ 电阻*10

![](media/8088ed382616afb346d44f5aacfb52d1.png)

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

在本项目中，我们用USB线将Raspberry Pi Pico和电脑连起来。连接方法请参照文档：开发环境设置

![](media/ed39dbeb566aab6ef635a02e55e19b19.jpg)
![](media/3b51ec821e42538c66dd6d659fa2e996.png)

项目电路图和接线图：

首先，切断树莓派Pico板的所有电源。然后根据电路图和接线图搭建电路。电路搭建好并验证无误后，用USB线将树莓派Pico板连接到电脑上。注意：避免任何可能的短路(特别是连接3.3V和GND)!

警告：短路可能导致电路中产生大电流，造成元件过热，并对硬件造成永久性损坏。

![](media/cb069d7553d861e3293d8bdbe85bbd05.png)

电路图

![](media/96800765a20d72653a8cd4a9ae12b636.png)

接线图

注意:

怎样连接LED

![](media/ce890a8f5f0aed0d9c33c34f57563d80.png)

怎样识别五色环220Ω电阻

![](media/c143fb8d355d4cb13056f3b2f15bd23c.png)

项目代码：

根据电路图，当树莓派Pico板的GP16输出高电平时，LED点亮；当输出低电平时，LED灯关闭。因此，我们可以通过控制GP16重复输出高低电平，使LED反复闪烁。

在上传项目代码到树莓派Pico板之前，请检查Arduino IDE的配置。

单击“工具”，确认板型和端口如下所示：

![](media/00cb510e12256d8cbbf96ffeb133d297.png)

单击![](media/b0d41283bf5ae66d2d5ab45db15331ba.png)将项目代码上传到树莓派Pico板。

![](media/35ab4cd24eb4f4d961355e5fc5622421.png)

项目代码上传成功！

![](media/918c8a394cbaab8879a4ab0954442611.png)

项目结果：

项目代码上传成功后，利用USB线上电，可以看到的现象是：电路中的LED开始闪烁，循环进行。

![](media/00af5f354f2083cdc6386ffd974cde89.png)
![](media/a6f2b10679e762080f2bac97dec380aa.png)

0.5秒

### 项目 04：呼吸灯

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

模拟信号在时间和数值上都是连续的信号。相反，数字信号或离散时间信号是由一系列数字组成的时间序列。生活中的大多数信号都是模拟信号。一个熟悉的模拟信号的例子是，全天的温度是如何不断变化的，而不是突然从0到10的瞬间变化。然而，数字信号的值可以瞬间改变，这个变化用数字表示为1和0(二进制代码的基础)。如下图所示，我们可以更容易地看出它们的差异。

![](media/4bdf6127e563b453a1fd8953b4ebb277.png)

在实际应用中，我们经常使用二进制作为数字信号，即一系列的0和1。由于二进制信号只有两个值(0或1)，因此具有很大的稳定性和可靠性。最后，可以将模拟信号和数字信号相互转换。

PWM：

脉宽调制(PWM)是一种利用数字信号控制模拟电路的有效方法。普通处理器不能直接输出模拟信号。PWM技术使这种转换(将数字信号转换为模拟信号)非常方便。PWM技术利用数字引脚发送一定频率的方波，即高电平和低电平的输出，交替持续一段时间。每一组高电平和低电平的总时间一般是固定的，称为周期(注:周期的倒数是频率)。高电平输出的时间通常称为脉宽，占空比是脉宽(PW)与波形总周期(T)之比的百分比。高电平输出持续时间越长，占空比越长，模拟信号中相应的电压也就越高。下图显示了对应于脉冲宽度0%-100的模拟信号电压在0V-3.3V(高电平为3.3V)之间的变化情况.

![](media/07831c118a4ce895fb317a6fa7bbf553.jpg)

PWM占空比越长，输出功率越高。既然我们了解了这种关系，我们就可以用PWM来控制LED的亮度或直流电机的速度等等。从上面可以看出，PWM并不是真实的模拟信号，电压的有效值等于相应的模拟信号。因此，我们可以控制LED和其他输出模块的输出功率，以达到不同的效果

树莓派Pico板与 PWM

树莓派Pico板有16个PWM通道，每个PWM通道可以独立控制频率和占空比，时钟频率范围为7Hz到125MHz。树莓派Pico板上的每个引脚都可以配置为PWM输出。

项目电路图和接线图：

![](media/88f88727dc4c0adca334b96206f91d63.png)

![](media/6f9b5d2444827aab124a64d3236a02a9.png)

项目代码：

本项目设计使GP16输出PWM，脉宽由0%逐渐增加到100%，再由100%逐渐减小到0%。

在上传项目代码到树莓派Pico板之前，请检查Arduino IDE的配置。

单击“工具”，确认板型和端口如下所示：

![](media/b110280fc60554d048620586f785186e.png)

单击![](media/b0d41283bf5ae66d2d5ab45db15331ba.png)将项目代码上传到树莓派Pico板。

![](media/8fccaff28e5cc2d55449fc34fbc25fec.png)

项目代码上传成功！

![](media/33844df20470b80212151b967885a586.png)

项目现象：

项目代码上传成功后，利用USB线上电，可以看到的现象是：电路中的LED从暗逐渐变亮，再从亮逐渐变暗，就像呼吸一样，循环进行。

![](media/e4789bf063f7fdca158b7a87011a02de.png)
![](media/3673c95868f245ee28365de8e51d2ced.png)

### 项目 05：交通灯

项目介绍：

交通灯在我们的日常生活中很普遍。根据一定的时间规律，交通灯是由红、黄、绿三种颜色组成的。每个人都应该遵守交通规则，这可以避免许多交通事故。在这个项目中，我们将使用树莓派Pico板和一些led(红，黄，绿)来模拟交通灯。

项目元件：

|![](media/77aa25aef55c00fcf0cd12143e34c688.jpg)|![](media/fccf6ad22d4013279f27b3923d0b87fd.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|![](media/afa6edd3ff90b027a6f43995a6fb15a2.png)|![](media/0c1b0f91b4e56bcbc235d06b48809ac9.png)|
|-|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|公对母杜邦线若干|红色LED*1|黄色 LED*1|
|![](media/6c688493b558ed5f3e90e7dab38cbd93.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|![](media/f7784bea849600eb35d1a52730050dd2.png)|![](media/afa78dcb54297dc7dcbf7f8eefcfe3c2.png)|![](media/58935b6f12b1ff3e3cadec37761e12eb.png)|
|绿色LED*1|USB 线*1|220Ω电阻*3|面包板*1|跳线若干|

项目电路图和接线图：

![](media/9c89c43f423eb6c23526e513b4844e29.png)![](media/8d0c6e62f1beff634ace981de3ecf978.png)

项目现象：

项目代码上传成功后，利用USB线上电，可以看到的现象是：1.首先，绿灯会亮5秒，然后熄灭；2.其次，黄灯会闪烁3次，然后熄灭；3.然后，红灯会亮5秒，然后熄灭；4.继续运行上述1-3个步骤。

### 项目 06：RGB

项目介绍：

![](media/3f08ddafb8c3a5d1754d36c33061cd86.png)

RGB led由三种颜色(红、绿、蓝)组成，通过混合这三种基本颜色可以发出不同的颜色。在这个项目中，我们将向你介绍RGB LED，并向你展示如何使用树莓派Pico板控制RGB LED发出不同的颜色光。即使RGB LED是非常基本的，但这也是一个介绍自己或他人电子和编码基础的伟大方式。

项目元件：

|![](media/b24a6b05d15c784b09c302e5c4bb7c61.jpg)|![](media/6092b6a258930909aa3e098283b36c87.png)|![](media/79c373b80745929aeea14eac48e52fb4.png)|![](media/f1a86fc81ab4b043263ce7e01e14d470.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|公对母杜邦线若干|RGB LED*1|
|![](media/f7784bea849600eb35d1a52730050dd2.png)|![](media/939747ba0b82ccdcbe289028356a7635.png)|![](media/b08ceab591a290805836f21bc11ab107.png)||
|220Ω电阻*3|面包板*1|USB 线*1||

元件知识：

显示器大多遵循RGB颜色标准，电脑屏幕上的所有颜色都是由红、绿、蓝三种颜色以不同比例混合而成。

![](media/32abd117bdfbba2f79a0e156048b9d22.png)![](media/aeade15279d7ab40d2a4797ef5983718.png)

这个RGB LED有4个引脚，每个颜色(红，绿，蓝)和一个共同的阴极。为了改变RGB led的亮度，我们可以使用树莓派Pico板的PWM引脚。PWM引脚会给RGB led不同占空比的信号以获得不同的颜色。

如果我们使用3个10位PWM来控制RGBLED，理论上我们可以通过不同的组合创建210\*210\*210=
1,073,741,824(10亿)种颜色。

项目电路图和接线图：

![](media/22244be631cf2dfd46536d12fd8734a5.png)

![](media/c18f869a9b18fc521c3d09be942efebd.png)

项目代码：

我们需要创建三个PWM通道，并使用随机占空比来使RGB LED亮随机颜色灯。

项目现象：

项目代码上传成功后，利用USB线上电，可以看到的现象是：RGB LED开始显示随机颜色。

### 项目 07：流水灯

项目介绍：

在日常生活中，我们可以看到许多由不同颜色的led组成的广告牌。他们不断地改变灯光(像流水一样)来吸引顾客的注意。在这个项目中，我们将使用树莓派Pico板控制10个leds实现流水的效果。

项目元件：

|![](media/b486a7424a885deec89a73a55b6ef7c9.jpg)|![](media/68aa11662f0455d6b5f1965a29336313.png)|![](media/79c373b80745929aeea14eac48e52fb4.png)|![](media/3ec5906fad2172708d449390140f55e6.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|公对母杜邦线若干|红色LED*10|
|![](media/f7784bea849600eb35d1a52730050dd2.png)|![](media/939747ba0b82ccdcbe289028356a7635.png)|![](media/6c56589d11fbdb64482a0c350cf86546.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|
|220Ω电阻*10|面包板*1|跳线若干|USB 线*1|

项目电路图和接线图:

![](media/002ba2e2074ba78b72c43635a4233ddc.png)

![](media/e3d6a1880f61fdfaec74360190f5ed43.png)

项目代码：

本项目是设计制作一个流水灯。这是这些行动：首先打开LED
\#1，然后关闭它。然后打开LED
\#2，然后关闭…并对所有10个LED重复同样的操作，直到最后一个LED关闭。这一过程反复进行，以实现流水的“运动”。

项目现象：

项目代码上传成功后，利用USB线上电，可以看到的现象是：10个LED将从左到右点亮，然后从右到左返回。

![](media/244d04c89963cb8d07bcb09281a01529.png)

### 项目 08：一位数码管

项目介绍：

七段数码管是一种显示十进制数字的电子显示设备，广泛应用于数字时钟、电子仪表、基本计算器和其他显示数字信息的电子设备。甚至我们在电影中看到的炸弹也有七段数码管。也许七段数码管看起来不够现代，但它们是更复杂的点阵显示器的替代品，在有限的光线条件下和强烈的阳光下都很容易使用。在这个项目中，我们将使用树莓派Pico板控制一位数码管显示数字。

项目元件：

|![](media/b2da57191e34efe5321aeee41421236b.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|![](media/75e38d601750a4707369bc73d8028063.png)|
|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|公对母杜邦线若干|一位数码管*1|
|![](media/f7784bea849600eb35d1a52730050dd2.png)|![](media/01e1718266f97a76fa59685d5d339430.png)|![](media/b08ceab591a290805836f21bc11ab107.png)||
|220Ω电阻*8|面包板*1|USB 线*1||

元件知识：

![](media/f638b9e28a1a47f9778804869c3d007f.png)

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

项目现象：

项目代码上传成功后，利用USB线上电，可以看到的现象是：一位数码管将显示从9到0的数字。

### 项目 09：四位数码管

项目介绍：

四位数码管是一种非常实用的显示器件。电子时钟的显示，球场上的记分员，公园里的人数都是需要的。由于价格低廉，使用方便，越来越多的项目将使用4位数码管。在这个项目中，我们使用树莓派Pico板控制四位数码管来显示数字。

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

项目现象：

项目代码上传成功后，利用USB线上电，你会看到的现象是：四位数码管显示数字，并在一个无限循环中重复这些动作。

### 项目 10：8×8 点阵显示

项目介绍： 

点阵屏是一种电子数字显示设备，可以显示机器、钟表、公共交通离场指示器和许多其他设备上的信息。在这个项目中，我们将使用树莓派Pico板控制8x8 LED点阵来显示数字0-9。

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

项目现象：

项目代码上传成功后，利用USB线上电，你会看到的现象是：8\*8点阵屏显示数字0-9。

### 项目 11：74HC595N 控制 8 个灯 

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

项目现象：

项目代码上传成功后，利用USB线上电，可以看到的现象是：8个LED开始以流水模式闪烁。

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

注意：1.该电路中蜂鸣器的电源为5V。在3.3V的电源下，蜂鸣器可以工作，但会降低响度。

2.VUSB应连接到USB线的正极，如果它连接到GND，它可能烧坏电脑或树莓派Pico板。同样，树莓派Pico板的36-40引脚接线时也要小心，避免短路。

3.有源蜂鸣器正极(“+”/长引脚)接引脚16，负极（短引脚）接GND。

项目现象：

项目代码上传成功后，利用USB线上电，可以看到的现象是：有源蜂鸣器发出“滴滴”声。

### 项目 13：无源蜂鸣器

项目介绍

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

![](media/01f4b56464e1de8313d340235c831b97.png)

无源蜂鸣器是一种内部没有振动源的集成电子蜂鸣器。它必须由2K-5K方波驱动，而不是直流信号。这两个蜂鸣器的外观非常相似，但是一个带有绿色电路板的蜂鸣器是无源蜂鸣器，而另一个带有黑色胶带的是有源蜂鸣器。无源蜂鸣器不能区分正极性而有源极性蜂鸣器是可以。

![](media/fc42c5ed014609ff0b290ee5361bb2fd.png)

晶体管: 请参考项目12.

项目电路图和接线图:

![](media/0275036a6d6598f9b07a12dd928b1f4c.png)

![](media/0257f2526dcedd215a11ccbce45ded51.png)

项目现象：

项目代码上传成功后，利用USB线上电，可以看到的现象是：无源蜂鸣器发出警报声。

### 项目 14：小台灯

项目介绍： 

你知道树莓派Pico板可以在你按下按键的时候点亮LED吗?
在这个项目中，我们将使用树莓派Pico板，一个按键开关和一个LED来制作一个迷你台灯。

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

![](media/6e4e0dbd8f9b5ec188b69697bee9a9d4.png)

项目现象：

项目代码上传成功后，利用USB线上电，可以看到的现象是：按下按钮，LED亮起；当按钮松开时，LED仍亮着。再次按下按钮，LED熄灭；当按钮释放时，LED保持关闭。是不是很像个小台灯？

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

注意:

怎样连接LED

![](media/ce890a8f5f0aed0d9c33c34f57563d80.png)

怎样识别五色环220Ω电阻和五色环10KΩ电阻

![](media/c143fb8d355d4cb13056f3b2f15bd23c.png)

![](media/f687e2dae7286f30c53b80e0170c7325.png)

项目结果：

项目代码上传成功后，利用USB线上电，可以看到的现象是：将面包板倾斜到一定角度，led就会一个一个地亮起来。当回到上一个角度时，led会一个一个关闭。就像沙漏一样，随着时间的推移，沙子漏了出来。

### 项目 16： I2C 128×32 LCD

项目介绍：

在生活中，我们可以利用显示器等模块来做各种实验。你也可以DIY各种各样的小物件。例如，用一个温度传感器和显示器做一个温度测试仪，或者用一个超声波模块和显示器做一个距离测试仪。下面，我们将使用LCD_128X32_DOT模块作为显示器，将其连接到树莓派Pico控制板上。将使用树莓派Pico主板控制LCD_128X32_DOT显示屏显示各种英文文字、常用符号和数字。

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

添加lcd128_32_io库：

本项目代码使用了一个名为“lcd128_32_io”库。如果你还没有添加，请在学习之前添加它。添加第三方库的步骤如下:

打开Arduino IDE，单击“项目”→“加载库”→“添加 .ZIP
库...”。在弹出窗口中找到该目录下名为：4. Arduino 教程\1. Windows 系统\3.
库文件\LCD_128X32.ZIP的文件，先选中LCD_128X32.ZIP文件，再单击“打开”。

![](media/aed61bbdd6e97b3bc4daa7c0da757e29.png)

![](media/1a7dcd52408d3cb879b85c09df0e2d32.png)

项目现象：

项目代码上传成功后，利用USB线上电，你会看到的现象是：128X32LCD模块显示屏第一行显示“keyes”、第二行显示“ABCDEFGHIJKLMNOPQR”、第三行显示“123456789+-\*/\<\>=$@”、第四行显示“%^&(){}:;'|?,.~\\\[\]”。

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

项目现象1：

项目代码上传成功后，利用USB线上电，你会看到的现象是：将小风扇片安装到直流电机上，上电后，可以看到电机转动4秒，停止2秒，以此规律重复执行。

项目电路图和接线图2：

（这个实验是使用S8550（PNP型三极管）控制电机）

![](media/d33d94a0e05ebd3fb986d07f540588c7.png)

![](media/a13d2691755474c34753ac38e8d00479.png)

项目现象2：

项目代码上传成功后，利用USB线上电，你会看到的现象是：将小风扇片安装到直流电机上，上电后，可以看到电机转动4秒，停止2秒，以此规律重复执行。

### 项目18：调光灯

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

上传代码成功之后，利用USB线上电，打开串口监视器，设置波特率为115200。可以看到的现象是：串口监视器窗口将打印出电位器的ADC值和电压值，转动电位器手柄时，ADC值和电压值发生变化。如下图所示：

![](media/0d9212c335a998d6783758f40f6095bc.png)

调光灯的电路图和接线图：

在前面一步，我们读取了电位器的ADC值和电压值，现在我们需要将电位器的ADC值转换成LED的亮度，来做成一个亮度可调的灯。见如下所示接线图：

![](media/efe066c44d7e97f9b9565cb9e09f7f81.png)

![](media/b08506476d0321b6040e38ce2992f775.png)

项目现象：

下载项目代码到树莓派Pico板，通过转动电位器手柄改变GP26的输入电压，树莓派Pico板根据这个电压值改变GP16的输出电压，从而改变LED的亮度。

![](media/2211121ed8269149f09a3eda2ea90b88.jpg)

### 项目 19：火焰警报器

项目介绍：

火灾是一种可怕的灾害，火灾报警系统在房屋，商业建筑和工厂中是非常有用的。在本项目中，我们将使用树莓派Pico板控制火焰传感器，蜂鸣器和LED来模拟火灾报警装置。这是一个有意义的创客活动。

项目元件：

|![](media/ee7e8566bc7c7b0d39df0d5cee4cf468.jpg)|![](media/2762753d227ba94de9f6e5c9ff79fe53.png)|![](media/8a09c36c5168c60d800736a9a7f1c200.png)|![](media/ef77f5a64c382157fc2dea21ec373fef.png)|![](media/4b4f653a76a82a3b413855493cc58fba.png)|
|-|-|-|-|-|
|树莓派Pico板*1|树莓派Pico板的扩展板*1|火焰传感器*1|红色 LED*1|有源蜂鸣器*1|
|![](media/01e1718266f97a76fa59685d5d339430.png)|![](media/6ded325b684d7ce7ad4dc8667e55faf4.png)|![](media/698d84e9dc3b34fd6be7c7d21a51c80d.png)|![](media/0bf747dcc565c53ac29e4709f7d486d8.png)|![](media/b08ceab591a290805836f21bc11ab107.png)|
|面包板*1|220Ω电阻*1|10KΩ电阻*1|跳线若干|USB 线*1|
|![](media/9ab8162cf6d998b145c6fdb31ee9733f.png)|![](media/ffbfbf739e60ed2c41ae74001f2edcb2.png)|![](media/dd891933d3bc5d4ba7be86a428e82108.png)|||
|NPN型晶体管(S8050)*1|1kΩ电阻*1|公对母杜邦线若干|||

元件知识：

![](media/182548dc26a4665628cfec50682ae31c.png)

火焰会发出一定程度的IR光，这种光人眼是看不到的，但我们的火焰传感器可以检测到它，并提醒微控制器（如树莓派Pico板）已经检测到火灾。它有一个专门设计的红外接收管来探测火焰，然后将火焰亮度转换为波动水平信号。接收三极管的短引脚是负极，另一个长引脚是正极。我们应该连接短引脚（负极)到5V，连接长
引脚(正极)到模拟引脚，一个电阻和GND。如下图所示：

![](media/c0a5ada5a6b624a0f0445f2c46c86839.jpg)

注意：火焰传感器应避开日光、汽车头灯、白炽灯直接照射，也不能对着热源(如暖气片、加热器)或空调，以避免环境温度较大的变化而造成误报。同时还易受射频辐射的干扰。

读取火焰传感器的ADC值和电压值：

我们首先用一个简单的代码来读取火焰传感器的模拟值，并将其打印出来。接线请参照以下接线图：

![](media/2b4e0cf420a0a94d6dfdd184f06fae33.png)

![](media/01e87dc7a2a23c003484d6f6ab2c8773.png)

上传代码成功之后，利用USB线上电，打开串口监视器，设置波特率为115200。可以看到的现象是：串口监视器窗口将打印出火焰传感器读取的模拟值，当火焰靠近火焰传感器时，模拟值增大；反之，模拟值减小。

![](media/c9783eb837b702694dffa8562e93d178.png)

火焰报警的电路图和接线图：

接下来，我们将使用火焰传感器和蜂鸣器、LED制作一个有趣的项目——火灾报警装置。当火焰传感器检测到火焰时，LED闪烁，蜂鸣器报警。

![](media/2f4b0e24a35b7e5b90e7577bd4fa13b5.png)

![](media/897914ede2a0a221bff1da80d7ead221.png)

项目代码：（注意：![](media/4b3a41657bb185bc081cc3768c117634.png)代码中的阀值500可以根据实际情况自己重新设置）

项目现象：

项目代码上传成功后，利用USB线上电，可以看到的现象是：当火焰传感器检测到火焰时，LED闪烁，蜂鸣器报警；否则，LED不亮，蜂鸣器不响。

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

光敏电阻：是一种感光电阻，其原理是光敏电阻表面上接收亮度(光)降低电阻，光敏电阻的电阻值会随着被探测到的环境光的强弱而变化。有了这个特性，我们可以使用光敏电阻来检测光强。光敏电阻及其电子符号如下

![](media/7d575da675a2f6cb511d28b801e2abaa.png)

下面的电路是用来检测光敏电阻电阻值的变化：

![](media/0f8e1b77a791cd804cbf8d7ab4abad70.png)

在上述电路中，当光敏电阻的电阻因光强的变化而改变时，光敏电阻与电阻R2之间的电压也会发生变化。因此，通过测量这个电压就可以得到光的强度。

读取光敏电阻的ADC值和电压值：

我们首先用一个简单的代码来读取光敏电阻模拟值，并将其打印出来。接线请参照以下接线图：

![](media/68337a2b734098f3bf0ad3fe5409dd2c.png)

![](media/a12cd4a08876876ff91108f77830049c.png)

上传代码成功之后，利用USB线上电，打开串口监视器，设置波特率为115200。可以看到的现象是：串口监视器窗口将打印光敏电阻读取的模拟值，当逐渐减弱光敏电阻所处环境中的光线强度时，模拟值逐渐增大；反之，模拟值逐渐减小。

![](media/c9783eb837b702694dffa8562e93d178.png)

光控灯的电路图和接线图：

我们在前面做了一个小小的调光灯，现在我们来做一个光控灯。它们的原理是相同的，即通过树莓派Pico板获取传感器的模拟值，然后调节LED的亮度。

![](media/aa30cb49386538a6ff5e5cd12a8383cd.png)

![](media/d34c5f9f70d90d560be98038169c270d.png)

项目结果：

项目代码上传成功后，利用USB线上电，可以看到的现象是：当减弱光敏电阻所处环境中的光线强度时，LED变亮，反之，LED变暗。

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

首先我们学习了热敏电阻读取当前的ADC值、电压值和温度值，并将其打印出来。请按下面的接线图接好线：

![](media/d1cc8f28e153531547d11ea977c37eca.png)

![](media/934f77b466c3f5391233dbbe62afecd6.png)

代码上传到树莓派Pico板成功之后，利用USB线上电，打开串口监视器，设置波特率为115200。你会看到的现象是：串口监视器窗口将不断显示热敏电阻当前的电压值和温度值。试着用食指和拇指捏一下热敏电阻(不要碰触导线)一小段时间，你应该会看到温度值增加。

![](media/378f1de2388faafdfb1e7750d78c80d9.png)

温度仪表电路图和接线图：

![](media/458af2aaa2a441e37e460179529084f7.png)

![](media/6972a3f15894404f7b6c13aa3ab45517.png)

添加lcd128_32_io库：

前面已经添加过lcd128_32_io库，可以不用重复添加。如果没有添加，就需要添加lcd128_32_io库，添加第三方库的步骤如下:

打开Arduino IDE，单击“项目”→“加载库”→“添加 .ZIP
库...”。在弹出窗口中找到该目录下名为：4. Arduino 教程\1. Windows 系统\3.
库文件\LCD_128X32.ZIP的文件，先选中LCD_128X32.ZIP文件，再单击“打开”。

![](media/770b59ac43f9d78c0a79e8562a63109a.png)

![](media/1a7dcd52408d3cb879b85c09df0e2d32.png)

项目现象：

项目代码上传成功后，利用USB线上电，你会看到的现象是：LCD 128X32 DOT的屏幕上显示热敏电阻的电压值和当前环境中的温度值。
