看着书大致了解了Arduino的基本情况，然后开始上网搜资料，完成了一个功能（更具实际骑行速度自动实现山地车换挡）
首先由霍尔传感器监测磁力变化，连续出现两次变化，则意味着完成一圈
其次根据车轮直径，与完成一圈的时间计算当前速度
得到速度后控制步进电机完成降升挡

实验工具:霍尔传感器，Arduino开发板，步进电机