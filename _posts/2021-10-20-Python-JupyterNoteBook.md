---
layout:     post   
title:      JupyterNotebook   
subtitle:   Python JupyterNotebook   
date:       2021-10-20   
author:     AnAn   
header-img: /img/life-bg/nature1.jpeg   
catalog: true   
tags:   
    - Python
---   

## 介绍   
- Jupyter（聆听i/ˈdʒuːpɪtər/）是一个非营利组织，旨在“为数十种编程语言的交互式计算开发开源软件，
  开放标准和服务”。2014年由Fernando Pérez从IPython中衍生出来，Jupyter支持几十种语言的执行环境。
  Jupyter Project的名称是对Jupyter支持的三种内核编程语言的引用，这三种语言是Julia、Python和R，
  也是对伽利略记录发现木星的卫星的笔记本的致敬。Jupyter项目开发并支持交互式计算产品Jupyter Notebook、JupyterHub和JupyterLab，
  这是Jupyter Notebook的下一代版本。
- Jupyter Notebook（前身是IPython Notebook）是一个基于Web的交互式计算环境，用于创建Jupyter Notebook文档。
  Notebook一词可以通俗地引用许多不同的实体，主要是Jupyter Web应用程序、Jupyter Python Web服务器或Jupyter文档格式
  （取决于上下文）。Jupyter Notebook文档是一个JSON文档，遵循版本化模式，包含一个有序的输入/输出单元格列表，
  这些单元格可以包含代码、文本（使用Markdown语言）、数学、图表和富媒体 (Rich media)，通常以“.ipynb”结尾扩展。
  Jupyter Notebook文档可以通过Web界面中的“Download As”，通过nbconvert库或shell中的“jupyter nbconvert”命令行界面，
  转换为许多的开源标准输出格式（HTML、演示幻灯片、LaTeX、PDF、reStructuredText、Markdown、Python)。
  为了简化Jupyter Notebook文档在Web上的可视化，nbconvert库是通过nbviewer提供的一项服务，它可以获取任何公开可用的Notebook文档的URL，
  将其动态转换为 HTML 并显示给用户。


### 目录
- [jupyerNotebook安装](#jupyerNotebook安装)
- [](#)



<a name="jupyerNotebook安装"></a>
###jupyerNotebook安装，及升级服务 
- jupyter notebook 是一个交互式的python编辑器，一般用于程序远程执行，调试。多用于服务器
- 如果使用conda环境安装jupyter 建议使用
 ```sh
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
- 将jupyter升级为系统服务（ubuntu systemd）
- jupyter-start.sh  
  ```sh
  #!/bin/bash
  ### su snnu -c "" 不能这样写，systemd会跟踪不到子进程
  sudo -u snnu nohup /home/snnu/anaconda3/bin/python -m jupyter notebook --port 8888 --no-browser --notebook-dir '~/' 1>>/dev/null 2>> /home/snnu/jupyter.service/error.log & 
  ```  
- /lib/systemd/system/autojupyter.service 
  ```sh
  [Unit]
  Description=jupyter notebook service
  After=network.target
          
  [Service]
  ExecStart=/home/snnu/jupyter.service/jupyter-start.sh
  ExecReload=/bin/kill -HUP $MAINPID
  KillMode=control-group
  Restart=on-failure
  Type=forking
          
  [Install]
  WantedBy=multi-user.target
  Alias=jupyter.service
  ```  

<a name=""></a>
### 

