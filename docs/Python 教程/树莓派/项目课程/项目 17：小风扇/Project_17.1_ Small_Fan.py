from machine import Pin
import time

motor = Pin(22, Pin.OUT)   # 从引脚22创建S8050对象，设置引脚22输出

try:
    while True:
        motor.value(1)    # 启动电机
        time.sleep(4) # 延时4秒
        motor.value(0)    # 关闭电机
        time.sleep(2) # 延时2秒
except:
    pass
