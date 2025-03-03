from machine import Pin
import time

led = Pin(19, Pin.OUT) # 从引脚19创建LED对象，设置引脚19为输出                   
button = Pin(22, Pin.IN, Pin.PULL_UP) #从引脚22创建按钮对象，设置GP22为输入

#自定义一个函数并将其命名为reverseGPIO()，用于反转LED的输出电平
def reverseGPIO():
    if led.value():
        led.value(0)     #设置led关闭
    else:
        led.value(1)     #设置led开启

try:
    while True:
        if not button.value():
            time.sleep_ms(20)
            if not button.value():
                reverseGPIO()
                while not button.value():
                    time.sleep_ms(20)
except:
    pass
