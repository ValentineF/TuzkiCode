# 阴阳师PC端自动刷御魂
参考[zydarChen](https://github.com/zydarChen)，写的一个阴阳师御魂自动挂机脚本。   
使用了WIN32库模拟鼠标操作，以及PIL库的实时截图分析。   
主要思路为：   
1. 预先准备御魂层数选择界面图的哈希值，以及准备按钮的坐标
2. 隔一定时间进行截图分析，判断实时图片与准备界面的流明距离。
3. 模拟鼠标操作（1000体力就这样肝完了）