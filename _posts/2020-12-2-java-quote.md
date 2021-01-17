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
#### 引用传递和值传递
- 概述
  - 引用传递和值传递是程序在函数的入口处或者对于参数传递的两种方式
- 引用传递
  - 引用传递指的是传递给函数入口的是参数的指针(内存地址)，所以对于函数对于参数的操作效果会在函数结束后仍然保留。
  - 对于java python 这些没有指针概念的语言，对于指针的操作对程序员是透明的。而对于C++或者C，对于指针的操作是透明的
- 值传递
  - 值传递指的是传递给函数入口的是参数的一个副本，或者说至少在效果上是这样的（python实现机制不同）。
- python java c++ 差异
    - 对于java，所有的形参的传递均是新建一个引用(指针)，然后将这个引用指向形参的指。这造成对于基本类型（boolean char byte short int long float double ）这些基本类型，形式上是值传递，对于非基本类型
    表现为引用传递。但是这种引用传递无法影响到外部指针的指向，C++是可以改变这种指向的。如下，changeValue1改变var外部指向失败，changeValue2改变var内部属性成功。
    ```java
    //Var.java
    package com.wangwen;
    public class Var {
    public int value;
    }
    //Test.java
    package com.wangwen;
    
    public class Test {
    public void changeValue1(Var var){
        Var var1 = new Var();
        var1.value=20;
        var=var1;
    }
    public void changeValue2(Var var){
        var.value=20;
    }
    @org.junit.Test
    public void test() throws InterruptedException {
        Var var = new Var();
        var.value=10;
        System.out.println(var.value);
        changeValue1(var);//更改外部引用指向
        System.out.println(var.value);
        changeValue2(var);//更改实列内部属性
        System.out.println(var.value);
    }
    }
    /*OUTPUT
    10
    10
    20
    */
    ```
    - 对于C++，其所有的数据类型，传递方式由程序员是否使用 & *决定
    - 对于python，其效果于java相同，解释上存在差异。其数据分可变(自定义类 list dict )和不可变类型（bool int float char str  tuble）。对于不可变类型，python解释器采用值传递，对于可变类型，反之。
    数据的引用传递，python解释器会对原参数取一个别名，对于该别名的操作会影响到原参数。
    对于值传递，效果上与java相同，但是python解释器不会去拷贝参数，而是新建一个引用，并让该引用和原参数指向同一个值，所以，对参数的操作实际是让新建的变量名指向新的操作结果。
    这样对于新变量名的操作不会影响到原参数，起到与java值传递相同的效果。
    之所以要与java区分解释，是因为python不存在基本类型的概念，java中的节本类型外暴露任何方法，这种类型与被编译后类型一一对应。仍然而python，其不可变类型仍然对外暴露一些方法(如hex,real)，可见这种类型解释运行时会被拆分成其他类型,
    但是不可变类型的内部值是不可被写的（比如 a=1; a.real=2; 会报 AttributeError: attribute 'real' of 'int' objects is not writable）。所以只能说效果上一致，原理上不同。

#### java中“=="与"equals"
- ==用于判定两个对象内存地址是否相等 euqals用于判定两个相同对象值是否相等
- 对于java，基本类型 long int short byte char boolean 这6中类型 外加 不使用new String类型均实现了常量池技术，即相同值的引用指向相同地址，float和double没有实现常量池技术。
所以多个声明的double或者float内存地址永远不相等，但是对于这两两种类型的==，jvm默认比较的是值，而不是内存地址，所以有如下OUTPUT输出，在a，b两个变量内存地址不同的情况下a==b输出true
- 对于Long Integer Short Byte Char Boolean的运算操作（+，-，*，/，//，%）默认会使用拆箱操作，将他们转换为基本类型，然后运算。
```java
@Test
public void test() throws InterruptedException {
    double a= 1.;
    double b= 1.;
    System.out.println(a==b);
    System.out.println(System.identityHashCode(a));
    System.out.println(System.identityHashCode(b));

}
/*OUTPUT
true
729864207
984849465
*/
```
- 如下，虽然equals看起来仍然调用的是“==”，但是在调用”==“调用之前，程序段先将装饰类型通过intValue()，floatToIntBits(value)等方法
将比较对象转换成了基本类型，由于常量池技术的的存在（float类除外，folat类和double类==在底层比较的便是值，jvm1.8验证），这些变量实际的内存地址也相同。
```java
//复制于Integer类
    public boolean equals(Object obj) {
        if (obj instanceof Integer) {
            return value == ((Integer)obj).intValue();
        }
        return false;
    }
//复制于Float类
    public boolean equals(Object obj) {
        return (obj instanceof Float)
               && (floatToIntBits(((Float)obj).value) == floatToIntBits(value));
    }
//复制于String类
    public boolean equals(Object anObject) {
        if (this == anObject) {
            return true;
        }
        if (anObject instanceof String) {
            String aString = (String)anObject;
            if (!COMPACT_STRINGS || this.coder == aString.coder) {
                return StringLatin1.equals(value, aString.value);
            }
        }
        return false;
    }
```
