---
layout:     post
title:      Docker笔记
subtitle:   Docker笔记
date:       2020-12-02
author:     AnAn
header-img: /img/post-bg-article.jpg
catalog: true
tags:
    - Linux
---
##目录
- [Docker载入载出](#id001)
  - [镜像导入导出](#id001)
  - [容器导入导出](#id002)
  - [容器提交为镜像](#id003)
  - [容器或镜像加载](#id004)
- [Docker网络模式](#id005)
  - [4种网络模式](#id005)
  - [创建一个新的网桥](#create-brige)
  - [将容器运行在新的网桥上](#id007)

## Docker载入载出
<a name="id001"></a>
#### 镜像导入导出
  - 导出
    ```shell script
      docker save -o 路径/目标名.tar 镜像名[如 nginx:latest] 
    ```
  - 导入
    ```shell script
      docker load -i 路径/目标名.tar
    ```
<a name="id002"></a>
#### 容器导入导出
  - 导出
    ```shell script
      docker export -o 路径/目标名.tar 容器名[如 abc123]  
    ```
  - 导入
    ```shell script
      docker import 路径/目标名.tar [nginx:imp] 
    ```
  <a name="id003"></a>
#### 容器提交为镜像
  ```shell script
  docker commit [OPTITIONS] CONTAINER [REPOSITORY[:TAG]]]
      -a:提交作者
      -c:使用DockerFile指令创建新的镜像
      -m:提交时的文字说明
      -p:提交时把容器暂停
  #example:
  docker commit -a "laowng" -m "for example" 容器ID myimage:v1
  ```
  <a name="id004"></a>
#### 容器或镜像加载
- 上述import或者load方法载入后都会以镜像的形式展示在Docker中,使用时需要重新实例化。
区别是export方法存储的图像没有layer层,即只有第一层FROM层和系统包含的用户文件。而save会将所有的layer
保存,并保留用户文件，所以后者对于程序更友好，程序运行一般也不会出错，但是保存的文件也更大。
- 例如Dockerfile文件如下,export命令将会丢失让所有RUN命令。
  ```sh
  FROM centos
  RUN yum install wget
  RUN wget -O redis.tar.gz "http://download.redis.io/releases/redis-5.0.3.tar.gz"
  RUN tar -xvf redis.tar.gz  
  ```  
  
<a name="id005"></a>
## Docker网络模式
#### 4种网络模式
- docker使用 --net=“mode” 的方式进行指定容器的网络模式。

  - 需要明确的是 docker—daemon（docker守护进程，可理解为Docker服务）和container的网络模式是相互独立的，一般
  docker-daemon与主机共享同一个网卡(host模式)，即也共享同一个ip地址。
  
  - 也有例外情况，比如在宿主机为windows系统非hyper-v模式下，那么Docker将依赖于Virtualbox（oracle虚拟机）,
  该虚拟机默认的网络模式为新建一块虚拟网卡，并于主机网卡桥接。此时可以认为Docker-daemon采用了桥接的网络模式（bridge模式）。
  
  - docker-container的四种网络模式
    - bridge 该模式为缺省网络模式([也可以新建一个](#create-brige)，在这种模式下 容器会虚拟一个新网卡，并与docker—daemon的网卡建立桥接。
    使用这种模式不同的容器之间可以直接使用容器内部ip 进行通信。
    - host 该模式，container和docker-daemon共享一个网卡，也即共享一个ip地址。所以这种情况下不同容器具有相同的ip，
    只能相同的ip，不同的端口（使用端口映射）进行通信。
    - None 该模式，Docker会关闭容器的网络，适用于不需要网络的容器
    - container 使用 " --net=container:container_id(容器名也可以) "进行设置，该模式下新容器与已存在容器共享一个网卡，共享一个ip。

<a name="create-brige"></a>
#### 创建一个新的网桥
  
  ```
  sudo docker network create --subnet=172.18.0.0/16 fixbridge
  ```
<a name="id007"></a>
#### 将容器运行在新的网桥上
  ```sh
  sudo docker run --name redis_101 -itd --net fixbridge --ip 172.18.0.101 --restart always
  --volume /volume1/docker/redis/data:/var/lib/redis
  --volume /volume1/docker/redis/log:/var/log/redis
  --env 'PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
  --env 'REDIS_VERSION=4.0.9'
  --env 'REDIS_USER=redis'
  --env 'REDIS_DATA_DIR=/var/lib/redis'
  --env 'REDIS_LOG_DIR=/var/log/redis'
  sameersbn/redis:latest
  
  --name 容器的名称， 我起的名字里面带ip，方便查看
  
  --net 我们创建的网络名称，写你的网络名字哦
  
  --ip 指定的ip。除了该参数界面无法配置外，其他参数界面均可配置。
  
  --restart always 不当关机时，会尝试重启
  
  --volume 指定路径映射， :前面是宿主的路径，该路径你需要在群辉里面创建的。 ：后面是映射到容器内部的路径。
  
  --env 环境变量
  ```

