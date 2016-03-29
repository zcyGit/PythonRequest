#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from PIL import ImageGrab

pic_name = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
#将用户屏幕截图，保存到本地某个目录下
pic = ImageGrab.grab()
pic.save('Image/屏幕截图_%s.png' % pic_name)