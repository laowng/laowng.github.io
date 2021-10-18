---
layout:     post
title:      灰度图转热力图
subtitle:   灰度图转热力图
date:       2020-12-06
author:     AnAn
header-img: /img/post-bg-article.jpg
catalog: true
tags:
    - Python
---

###  灰度图转热力图python
- 该方法需要依赖numpy，cv2
  ```python
  import cv2
  import numpy as np
  import os
  dirpath="/home/wangwen/pic"
  outpath="/home/wangwen/picout"
  def getfile(path, is_path=True, type="dir"):
      filelist = []
      filelist_ = os.listdir(path)
      if is_path:
          for i in range(len(filelist_)):
              filelist_[i] = os.path.join(path, filelist_[i])
      if type == "dir":
          for p in filelist_:
              if "." not in os.path.splitext(p)[1]:
                  filelist.append(p)
      elif type == "pic":
          for p in filelist_:
              if os.path.splitext(p)[1] in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ]:
                  filelist.append(p)
  
      return filelist
  if __name__ == '__main__':
      pic_path_list=getfile(dirpath,type="pic")
      for pic_path in pic_path_list:
          image=cv2.imread(pic_path,2)
          #下边注释的两步为16位深度图转8位深度图的两种方法，如果输入本身为8位深度,则注释状态无需更改
          #image=image/(image.max()-image.min())*256
          # image=image/256
          image8=image.astype(np.uint8)
          imagejet=cv2.applyColorMap(image8,cv2.COLORMAP_JET)
          picn=os.path.splitext(os.path.split(pic_path)[1])[0]
          cv2.imwrite(os.path.join(outpath,picn+"-jet"+".png"),imagejet)
          #以下位hot模式
          # imagehot=cv2.applyColorMap(image8,cv2.COLORMAP_HOT)
          # cv2.imwrite(os.path.join(outpath,picn+"-hot"+".png"),imagehot)
  
  ```
