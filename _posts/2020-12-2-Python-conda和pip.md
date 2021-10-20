---
layout:     post
title:      conda
subtitle:   conda pip 一些常用命令
date:       2020-12-02
author:     AnAn
header-img: /img/post-bg-article.jpg
catalog: true
tags:
    - Python
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
3. conda更改清华源或者其他源
 - conda config --set show_channel_urls yes #使用该命令生成.condarc文件 一般位于"/home/username/"文件夹下
 - 将以下清华源索引复制到.condarc文件内，覆盖即可
    ```yaml
    channels:
    - defaults
        show_channel_urls: true
        channel_alias: https://mirrors.tuna.tsinghua.edu.cn/anaconda
    default_channels:
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
        - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
    custom_channels:
    conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
    simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
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
3. pip更换清华源
  - 临时使用
    ```bash
    pip install PakageName-i https://pypi.tuna.tsinghua.edu.cn/simple some-package
    ```
  - 永久使用
    ```bash
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    ```
















