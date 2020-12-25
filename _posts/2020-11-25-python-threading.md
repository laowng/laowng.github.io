---
layout:     post
title:      python多线程调试笔记
subtitle:   GISR调试
date:       2020-11-03
author:     AnAn
header-img: https://dss2.bdstatic.com/kfoZeXSm1A5BphGlnYG/skin/113.jpg
catalog: true
tags:
    - python
---

- [GISR项目地址](https://github.com/laowng/GISR)

- 环境
    ```
    os:Windows Server2016
    python 3.8.5 pytorch 1.7.0
    ```

- 问题
    ```
    torch.utils.data.dataloader.DataLoader(num_workers=0)
    
    在num_workers=0的情况下将不启用多线程进行数据载入
    在numwork=n(n!=0)的情况下会将主函数外的资源，即主函数文件外的部分 如 import xx ,a=5等 在启用线程的时候重新执行一边，用于拷贝资源
    这可能导致tqdm等进度条显示模块出错，或者资源不同步
    ```
- 解决方法
    ```
    将需要同步的资源放在主函数内，如果程序没有主函数，建议创建一个主函数，然后使用 if \__name\__=="__mian__":main() 语法调用
    ```


