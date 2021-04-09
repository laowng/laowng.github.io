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
### 定时运行-crontab
- crontab \[-u username]　　　　//省略用户表表示操作当前用户的crontab  
    -e      (编辑工作表)  
    -l      (列出工作表里的命令)  
    -r      (删除工作作)
  - 格式:

          minute   hour  day   month   week   command  
          # For details see man 4 crontabs  
          # Example of job definition:  
          .---------------------------------- minute (0 - 59) 表示分钟  
          |  .------------------------------- hour (0 - 23)   表示小时  
          |  |  .---------------------------- day of month (1 - 31)   表示日期  
          |  |  |  .------------------------- month (1 - 12) OR jan,feb,mar,apr ... 表示月份  
          |  |  |  |  .---------------------- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat  表示星期（0 或 7 表示星期天）  
          |  |  |  |  |  .------------------- username  以哪个用户来执行  
          |  |  |  |  |  |            .------ command  要执行的命令，可以是系统命令，也可以是自己编写的脚本文件  
          |  |  |  |  |  |            |  
          *  *  *  *  * user-name  command to be executed

- 格式实例：

    |命令|说明|
    |:---|:---|
    | */1 * * * * service httpd restart 每一分钟 重启httpd服务 |  每一分钟 重启httpd服务   |
    |*/1 * * * * service httpd restart|每一分钟 重启httpd服务|
    |0 */1 * * * service httpd restart|每一小时 重启httpd服务|
    |30 21 * * * service httpd restart|每天 21：30 分 重启httpd服务|
    |26 4 1,5,23,28 * * service httpd restart|每月的1号，5号 23 号 28 号 的4点26分，重启httpd服务|
    |26 4 1-21 * * service httpd restart|每月的1号到21号 的4点26分，重启httpd服务|
    |*/2 * * * * service httpd restart|每隔两分钟 执行，偶数分钟 重启httpd服务|
    |1-59/2 * * * * service httpd restart|每隔两分钟 执行，奇数 重启httpd服务|
    |0 23-7/1 * * * service httpd restart|每天的晚上11点到早上7点 每隔一个小时 重启httpd服务|
    |0,30 18-23 * * * service httpd restart|每天18点到23点 每隔30分钟 重启httpd服务|
    |0-59/30 18-23 * * * service httpd restart|每天18点到23点 每隔30分钟 重启httpd服务|
    |59 1 1-7 4 * test 'date +\\%w' -eq 0 && /root/a.sh|四月的第一个星期日 01:59 分运行脚本 /root/a.sh ，命令中的 test是判断，%w是数字的星期几|


