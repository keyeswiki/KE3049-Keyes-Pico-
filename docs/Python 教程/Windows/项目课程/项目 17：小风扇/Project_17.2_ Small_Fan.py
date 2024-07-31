from machine import Pin
import time

motor = Pin(22, Pin.OUT)   # 从引脚22创建S8550对象，设置引脚22输出

try:
    while True:
        motor.value(0)    # 启动电机
        time.sleep(4) # 延时4秒
        motor.value(1)    # 关闭电机
        time.sleep(2) # 延时2秒
except:
    pass
