# This Program by m.mahadi 
import math


def lcm_calculation(first, secend):
    cal = math.lcm(first, secend)
    print(cal)


first, secend = map(int, input().split())
lcm_calculation(first, secend)
