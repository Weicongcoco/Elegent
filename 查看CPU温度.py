import time
import clr
import GPUtil
from OpenHardwareMonitor.Hardware import Computer
from gpiozero import CPUTemperature
# clrAddReferrnce中需要使用下载OpenHardwareMonitor并解压，该函数里输入的是OpenHardwareMonitor里面的OpenHardwareMonitorLib地址
clr.AddReference(r"./OpenHardwareMonitor\OpenHardwareMonitorLib")

c = Computer()

c.CPUEnabled = True
c.GPUEnalbed = True
c.Open()

while True:
    for a in range(0, len(c.Hardware[0].Sensors)):
        if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
            print(f"CPU温度：{c.Hardware[0].Sensors[a].get_Value()}")
            c.Hardware[0].Update()
            gpu = GPUtil.getGPUs()[0]
            print("GPU温度", gpu.temperature)
            print()
            break
    time.sleep(0.5)

