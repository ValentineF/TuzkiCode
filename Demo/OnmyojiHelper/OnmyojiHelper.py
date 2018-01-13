import win32api
import win32con
import win32gui
import time
import PIL
from PIL import ImageGrab
from PIL import Image

#鼠标点击
def mouse_click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    return 0

# 获取窗口信息
def get_window_info():  
    windowName = u'阴阳师-网易游戏'
    handle = win32gui.FindWindow(0, windowName)  # 获取窗口句柄
    if handle == 0:
        return None
    else:
        return win32gui.GetWindowRect(handle)

# 获取游戏截图
def get_image(windowPos):
    image = ImageGrab.grab((windowPos[0]+7,windowPos[1],windowPos[2]-7,windowPos[3]-7))
    return image

# 计算图片的哈希值
def get_hash(img):
    img = img.resize((16, 16), Image.ANTIALIAS).convert('L')  # 抗锯齿 灰度
    avg = sum(list(img.getdata())) / 256  # 计算像素平均值
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))  # 每个像素进行比对,大于avg为1,反之为0
    return ''.join(map(lambda j: '%x' % int(s[j:j+4], 2), range(0, 256, 4)))

# 根据汉明距离判断图片是否相似
def judge_img(hash1, hash2, n=20):
    if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
        return True
    else:
        return False

#准备页面HASH值：ffff000200001ff81ff81ffc1ff81ff81ff81f181f981f98000007f007f00000
#挑战鼠标坐标：1240，666
#准备坐标：1422，666
#窗体坐标：（384，189），（1536，868）
#挑战的相对位置：（x1+856,y1+477）|gameWindow[0]+856,gameWindow[1]+477
#准备的相对位置：（x1+1038,y1+477）|gameWindow[0]+1038,gameWindow[1]+477
if __name__ == "__main__":
    readHash = 'ffff000200001ff81ff81ffc1ff81ff81ff81f181f981f98000007f007f00000'
    gameWindow = get_window_info()    
    while True:
        time.sleep(5)
        img = get_image(gameWindow)        
        if(judge_img(readHash,get_hash(img))):
            mouse_click(gameWindow[0]+856,gameWindow[1]+477)
            print("相似，开始挑战")
        else:
            print("点击准备")
            mouse_click(gameWindow[0]+1038,gameWindow[1]+477)
    #print(get_hash(img))


