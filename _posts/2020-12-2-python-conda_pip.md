---
layout:     post
title:      conda
subtitle:   conda pip 一些常用命令
date:       2020-12-02
author:     AnAn
header-img: https://dss2.bdstatic.com/kfoZeXSm1A5BphGlnYG/skin/113.jpg
catalog: true
tags:
    - python
---

### conda
1. 环境输出
    ```bash
    conda env export > envName.yaml
    ```
2. 环境安装
    ```bash
    conda env create -f envName.yaml
    ```
### pip
1. 环境输出
    ```bash
    pip freeze > requirements.txt      
    ```
2. 环境安装
    ```bash
    pip install -r requirements.txt
    ```
