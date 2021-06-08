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
3. jupyer
   - jupyter notebook 是一个交互式的python编辑器，一般用于程序远程执行，调试。多用于服务器
   - 如果使用conda环境安装jupyter 建议使用
     ```bash
     conda install nb_conda 
     ```
   - 使用这个命令会自动安装jupyter notebook等依赖，并且在web端可灵活切换管理conda环境（直接使用pip安装jupyter 还需要安装ipykernel 才能管理环境）
   - 对于jupyer notebook 修改密码，网上教程较为复杂，以下为笔记：
     ```bash
     jupyter notebook --generate-config #生成jupyter notebook 配置文件
        #配置文件的位置会显示在终端，一般位于/home/uesername/.jupyter/jupyter_notebook_config.py
     jupyter notebook password #该命令将生成用户输入密码的sha256密钥
        #密钥一般存放于 /home/uesername/.jupyter/jupyter_notebook_config.json 文件
        #文件内p="密钥"
        #将密钥复制，粘贴于jupyter_notebook_config.py，使c.NotebookApp.password='密钥'
        #如果需要监听全局ip，需要使c.NotebookApp.ip='0.0.0.0' c.NotebookApp.allow_remote_access = True
        

        #记得将修改处变量前的“#”删去，使更改生效
     ```
4. conda更改清华源或者其他源
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
    pip list --format=freeze > requirements.txt     
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
















