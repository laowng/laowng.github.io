---
layout:     post
title:      Docker笔记
subtitle:   Docker笔记
date:       2020-12-02
author:     AnAn
header-img: https://dss2.bdstatic.com/kfoZeXSm1A5BphGlnYG/skin/113.jpg
catalog: true
tags:
    - 运维
---
#### Docker载入载出    - Docker 镜像导入导出
  - 导出
  ```bash
    docker save -o 路径/目标名.tar 镜像名[如 nginx:latest] 
  ```
    - 导入
  ```bash
    docker load -i 路径/目标名.tar
  ```
- Docker 容器导入导出
  - 导出
  ```bash
    docker export -o 路径/目标名.tar 容器名[如 abc123]  
  ```
    - 导入
  ```bash
    docker import 路径/目标名.tar [nginx:imp] 
  ```
- 上述import或者load方法载入后都会以镜像的形式展示在Docker中,使用时需要重新实例化。
区别是export方法存储的图像没有layer层,即只有第一层FROM层和系统包含的用户文件。而save会将所有的layer
保存,并保留用户文件，所以后者对于程序更友好，程序运行一般也不会出错，但是保存的文件也更大。
  - 例如Dockerfile文件如下,export命令将会丢失让所有RUN命令。
    ```
    FROM centos
    RUN yum install wget
    RUN wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz"
    RUN tar -xvf redis.tar.gz  
    ```
#### docker 网络模式
- docker使用 --net=“mode” 的方式进行指定容器的网络模式。

  - 需要明确的是 docker—daemon（docker守护进程，可理解为Docker服务）和container的网络模式是相互独立的，一般
  docker-daemon与主机共享同一个网卡(host模式)，即也共享同一个ip地址。

  - 也有例外情况，比如在宿主机为windows系统非hyper-v模式下，那么Docker将依赖于Virtualbox（oracle虚拟机）,
  该虚拟机默认的网络模式为新建一块虚拟网卡，并于主机网卡桥接。此时可以认为Docker-daemon采用了桥接的网络模式（bridge模式）。

  - docker-container的四种网络模式
    - bridge 该模式为缺省网络模式，在这种模式下 容器会虚拟一个新网卡，并与docker—daemon的网卡建立桥接。
    使用这种模式不同的容器之间可以直接使用容器内部ip 进行通信。
    - host 该模式，container和docker-daemon共享一个网卡，也即共享一个ip地址。所以这种情况下不同容器具有相同的ip，
    只能相同的ip，不同的端口（使用端口映射）进行通信。
    - None 该模式，Docker会关闭容器的网络，适用于不需要网络的容器
    - container 使用 " --net=container:container_id(容器名也可以) "进行设置，该模式下新容器与已存在容器共享一个网卡，共享一个ip。
#### 记一次Docker tomcat自动运行
1. 使用 docker run --name ssq -P -it tomcat:latest /bin/bash 安装了tomcat容器
2. ssq 容器重启后 发现tomcat服务不会自动重启 3.为images信息
3.  REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
    tomcat       latest    feba8d001e3f   5 days ago     649MB
4. tomcat容器的系统信息：Linux version 4.19.130-boot2docker (root@3e8c56dabc1e) (gcc version 8.3.0 (Debian 8.3.0-6)) #1 SMP Mon Jun 29 23:52:55 UTC 2020
5. 在/etc/profile和/root/profile中添加tomcat启动命令均不能随开机运行命令
6. 无奈，尝试在/etc/bash.bashrc中添加tomcat启动命令，生效。缺点是，每次打开shell都会运行一遍tomcat启动命令，好在该命令会先检测一遍tomcat是否启动，然后进行服务启动动作，不会引起tomcat服务错误。
7. 后续找到解决方案再更新

