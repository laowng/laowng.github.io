---
layout:     post
title:      引用传递和值传递
subtitle:   引用,值
date:       2020-12-02
author:     AnAn
header-img: https://dss2.bdstatic.com/kfoZeXSm1A5BphGlnYG/skin/113.jpg
catalog: true
tags:
    - java
---

- 概述
  - 引用传递和值传递是程序在函数的入口处或者对于参数传递的两种方式
- 引用传递
  - 引用传递指的是传递给函数入口的是参数的指针(内存地址)，所以对于函数对于参数的操作效果会在函数结束后仍然保留。
  - 对于java python 这些没有指针概念的语言，对于指针的操作对程序员是透明的。而对于C++或者C，对于指针的操作是透明的

- 值传递
  - 值传递指的是传递给函数入口的是参数的一个副本，或者说至少在效果上是这样的（python实现机制不同）。
- python java c++ 差异

    - 对于java，其数据类型分为基本类型（boolean char byte short int long float double void ）和非基本类型。对于基本类型，jvm会使用值传递，方法为对参数复制一份
    而对于非基本类型，jvm会选择引用传递，即传递指针，因为该操作是由jvm决定的。
    - 对于C++，其所有的数据类型，传递方式由程序员是否使用 & *决定
    对于python，其数据分可变(自定义类 list dict )和不可变类型（bool int float char str  tuble）。对于不可变类型，python解释器采用值传递，对于可变类型，反之。
    数据的引用传递，python解释器会对原参数取一个别名，对于该别名的操作会影响到原参数。
    - 对于值传递，效果上与java相同，但是python解释器不会去拷贝参数，而是新建一个变量名，并让该变量名和原参数指向同一个值，所以，对参数的操作实际是让新建的变量名指向新的操作结果。
    这样对于新变量名的操作不会影响到原参数，起到与java值传递相同的效果。

