---
layout:     post
title:      ubuntu实现远程桌面
subtitle:   ubuntu实现远程桌面
date:       2020-12-02
author:     AnAn
header-img: /img/post-bg-article.jpg
catalog: true
tags:
    - 运维
---


### 使用vnc-any
- 截图工具flameshot挺好用
- 环境
  - ubuntu=18.04，支持ubuntu16.xx
1. 在设置中找到“共享”

    ![共享设置1](/img/post/yunwei-ubuntu/desktop-share.png)
    
    ![共享设置2](/img/post/yunwei-ubuntu/desktop-share1.png)

2. 安装xrdp vnc4server xbase-clients dconf-editor
    ```sh
    sudo apt-get install xrdp vnc4server xbase-clients
    sudo apt-get install dconf-editor
    ```
3. 使用dconf-editor 取消加密

    ![搜索](/img/post/yunwei-ubuntu/dconf-config0.png)
    
    ![取消加密](/img/post/yunwei-ubuntu/dconf-config.png)
    
4. 使用RDP软件进行与远程连接，默认端口号位3389，进入界面后选择vnc-any

    ![vnc-any](/img/post/yunwei-ubuntu/rdp-vnc-any.png)


### 使用xorg/xface4实现远程桌面

- 概述
    ```
    ubuntu实现远程桌面
    ```
    - 环境
    - ubuntu=16.04 xrdr=0.6.01

1. 安装xfce4卓面 
    ```sh
    sudo apt-get install xfce4 #安装xfce4卓面
    echo xfce4-session >~.xsession #指定xfce4为远程桌面
    ```
2. 安装xrdp服务
    ```sh
    sudo apt-get install xrdp #安装xrdp服务
    sudo systemctl enable xrdp #将xrdp服务设为开机启动
    ```
3. 端口号
    - xrdp服务的端口默认认为3389 在/etc/xrdp/seeman.ini中修改
4. 备注
    - 对于ubuntu16需要在/etc/xrdp/startwm.sh中  /etc/X11/Xsession  前加xfce4-session(ubuntu18.04不需要)，登陆时选择xvnc
    - 对于ubuntu18.04 需要使用dconf-editor工具将  org/gnome/desktop/remote-access/ 下的require-encryption关闭，登陆时选择xorg
    - 对于ubuntu18.04 远程时终端无法打开，需要用   sudo update-alternatives --config x-terminal-emulator  命令切换一个默认终端

