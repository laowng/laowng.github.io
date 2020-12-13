---
layout:     post
title:      ubuntu实现远程桌面
subtitle:   ubuntu实现远程桌面
date:       2020-12-02
author:     AnAn
header-img: https://dss2.bdstatic.com/kfoZeXSm1A5BphGlnYG/skin/113.jpg
catalog: true
tags:
    - 运维
---

- 概述

    ```
    ubuntu实现远程桌面
    ```
- 环境
  - ubuntu=16.04 xrdr=0.6.01
- 1
    ```bash
    sudo apt-get install xfce4 #安装xfce4卓面
    echo xfce4-session >~.xsession #指定xfce4为远程桌面
    ```

- 2
    ```bash
    sudo apt-get install xrdp #安装xrdp服务
    sudo systemctl enable xrdp #将xrdp服务设为开机启动
    ```
- 3
    - xrdp服务的端口默认认为3389 在/etc/xrdp/seeman.ini中修改
- 4
    - 对于ubuntu16需要在/etc/xrdp/startwm.sh中  /etc/X11/Xsession  前加xfce4-session(ubuntu18.04不需要)，登陆时选择xvnc
    - 对于ubuntu18.04 需要使用dconf-editor工具将  org/gnome/desktop/remote-access/ 下的require-encryption关闭，登陆时选择xorg
    - 对于ubuntu18.04 远程时终端无法打开，需要用   sudo update-alternatives --config x-terminal-emulator  命令切换一个默认终端

