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

- Docker 镜像导入导出
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

