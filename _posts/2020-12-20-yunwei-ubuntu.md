---
layout:     post
title:      Ubuntu笔记
subtitle:   Ubuntu笔记
date:       2020-12-02
author:     AnAn
header-img: https://dss2.bdstatic.com/kfoZeXSm1A5BphGlnYG/skin/113.jpg
catalog: true
tags:
    - 运维
---

### ubuntu环境配置文件
- /etc/profile
  - 此文件为系统的每个用户设置环境信息,当用户第一次登录时,该文件被执行.并从/etc/profile.d目录的配置文件中搜集shell的设置.
  所以如果你有对/etc/profile有修改的话必须得重启你的修改才会生效，此修改对每个用户都生效。
- /etc/bashrc或/etc/bash.bashrc
  - :为每一个运行bash shell的用户执行此文件.当bash shell被打开时,该文件被读取.如果你想对所有的使用bash的用户修改某个配置并
  在以后打开的bash都生效的话可以修改这个文件，修改这个文件不用重启，重新打开一个bash即可生效。
- ~/.bash_profile或～/.profile
  - 每个用户都可使用该文件输入专用于当前用户使用的shell信息,当用户登录时,该文件仅仅执行一次!默认情况下,他设置一些环境变量,执行用户的.bashrc文件.
- ~/.bashrc
  - 该文件包含专用于你的bash shell的bash信息,当登录时以及每次打开新的shell时,该文件被读取.

### 终端标准输出和错误输出
- command 1 > fielname 把把标准输出重定向到一个文件中
- command > filename 2>&1 把把标准输出和标准错误一起重定向到一个文件中