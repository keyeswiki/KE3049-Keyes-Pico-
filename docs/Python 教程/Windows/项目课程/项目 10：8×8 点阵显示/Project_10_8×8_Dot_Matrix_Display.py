from machine import Pin
import time

#定义该行的引脚，并设置为输出
row1 = machine.Pin(18, machine.Pin.OUT)
row2 = machine.Pin(26, machine.Pin.OUT)
row3 = machine.Pin(17, machine.Pin.OUT)
row4 = machine.Pin(21, machine.Pin.OUT)
row5 = machine.Pin(10, machine.Pin.OUT)
row6 = machine.Pin(16, machine.Pin.OUT)
row7 = machine.Pin(11, machine.Pin.OUT)
row8 = machine.Pin(14, machine.Pin.OUT)
#定义列的引脚，并设置为输出
col1 = machine.Pin(22, machine.Pin.OUT)
col2 = machine.Pin(12, machine.Pin.OUT)
col3 = machine.Pin(13, machine.Pin.OUT)
col4 = machine.Pin(19, machine.Pin.OUT)
col5 = machine.Pin(15, machine.Pin.OUT)
col6 = machine.Pin(20, machine.Pin.OUT)
col7 = machine.Pin(27, machine.Pin.OUT)
col8 = machine.Pin(28, machine.Pin.OUT)

#将列的引脚设置为低电平
col1.value(0)
col2.value(0)
col3.value(0)
col4.value(0)
col5.value(0)
col6.value(0)
col7.value(0)
col8.value(0)

#由于点阵屏中的列被设置为低电平，当该行的引脚处于高电平时，相应的点阵屏行将点亮
def Row(d):
    if(d ==1):
        row1.value(1)  #点亮第一行
    if(d ==2):
        row2.value(1)  #点亮第二行
    if(d ==3):
        row3.value(1)
    if(d ==4):
        row4.value(1)
    if(d ==5):
        row5.value(1)
    if(d ==6):
        row6.value(1)
    if(d ==7):
        row7.value(1)
    if(d ==8):
        row8.value(1)
    
#关闭点阵屏
def off():
    row1.value(0)
    row2.value(0)
    row3.value(0)
    row4.value(0)
    row5.value(0)
    row6.value(0)
    row7.value(0)
    row8.value(0) 

try:
    print("test...")
    while True:
         for num in range(1,10):  #逐行点亮点阵屏
             Row(num)
             if(num == 9):  #因为点阵屏只有8行，我在这里限制一下，等于9
                off()      #关闭点阵屏
             time.sleep(0.2)

except:
    pass