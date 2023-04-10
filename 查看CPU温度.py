import time
from time import sleep
import clr
import GPUtil


clr.AddReference(r"D:\Pycharm\PyCharm_Community_Edition_2022.2.3\projects_code\工作项目\OpenHardwareMonitor\OpenHardwareMonitorLib")
from OpenHardwareMonitor.Hardware import Computer

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
    time.sleep(1)


