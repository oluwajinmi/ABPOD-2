from LidarX2 import LidarX2
from time import sleep, time
import math
import matplotlib.pyplot as plt
import numpy as np

lidar = LidarX2("COM14")

if not lidar.open():
    print("Cannot open lidar")
    exit(1)

t = time()
while time() - t < 20:  # Run for 20 seconds
    measures = lidar.getMeasures()  # Get latest lidar measures
    print(measures)
    sleep(0.01)


lidar.close()
