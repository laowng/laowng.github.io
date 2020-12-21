---
layout:     post
title:      三种经典的java设计模式
subtitle:   笔记。
date:       2020-11-03
author:     AnAn
header-img: https://dss2.bdstatic.com/kfoZeXSm1A5BphGlnYG/skin/113.jpg
catalog: true
tags:
    - 设计模式，Design_Pattern
---
### Design Pattern
- 简介
    - 在 1994 年，由 Erich Gamma、Richard Helm、Ralph Johnson 和 John Vlissides 四人合著出版了一本名为
    Design Patterns - Elements of Reusable Object-Oriented Software（中文译名：设计模式 - 可复用的面向对象软件元素)的书，
    该书首次提到了软件开发中设计模式的概念。
    四位作者合称 GOF（四人帮，全拼 Gang of Four）。他们所提出的设计模式主要是基于以下的面向对象设计原则。
      - 对接口编程而不是对实现编程。
      - 优先使用对象组合而不是继承。
#### 以下列举3种常见的设计模式
1. 策略模式:

    - 体现java面向抽象，对扩展开放，对修改封闭的原则
    - 策略与问题分：策略为一类，问题为一类
    - 例如，一些函数的参数（sort python,java,c++均有）会在形参处保留一个function指针，该function指定了父函数进行一些操作的策略，这便是典型的策略模式

2. 中介者模式

    - 体现java多用组合少用继承的，低耦合的设计思想
    - 将具有类似属性的若干类对象之间的关系交由中介者类去维护，免去直接修改多个类的内部，以达到更新类之间关系的目的。
   - 例如，Dijkstra算法和Floyd算法中用第三方对象去维护各结点之间的距离关系，这便是典型的中介者模式

3. 模板方法模式

    - 体现java高内聚的设计思想
    - 面向算法，在抽象类中搭建算法的骨架，该抽象类中使用内部抽象成员完成了**模板方法**的实现细节，
#### 正文
- 根据GOF，设计模式总共有23种，并且他们可以分为3大类，分别为:
  - 创建型模式
    - [工厂模式(Factory Pattern)](#工厂模式)
    - 抽象工厂模式(Abstract Factory Pattern)
    - 单列模式(Singleton Pattern)
    - 建造者模式(Builder Pattern)
    - 模型模式(Prototype Pattern)
  - 结构性模式
    - 适配器模式(Adapter Pattern)
    - 桥接模式(Bridge Pattern)
    - 过滤模式(Filter、Criteria Pattern)
    - 组合模式(Composite Pattern)
    - 装饰器模式(Decorator Pattern)
    - 外观模式(Facade Pattern)
    - 享元模式(Flyweight Pattern)
    - 代理模式(Proxy Pattern)
  - 行为型模式
    - 责任连模式(Chain of Responsibility Pattern)
    - 命令模式(Command Pattern)
    - 解释器模式(Interpreter Pattern)
    - 迭代器模式(Iterator Pattern)
    - 中介者模式(Mediator Pattern)
    - 备忘录模式(Memento Pattern)
    - 观察者模式(Observer Pattern)
    - 状态模式(State Pattern)
    - 空对象模式(Null Object Pattern)
    - 策略模式(Strategy Pattern)
    - 模板模式(Template Pattern)
    - 访问者模式(Visitor Pattern)
- 另外J2EE模式(Sun提供)
  - J2EE模式
    - MVC模式(MVC Pattern)
    - 业务代表模式(Business Delegate Pattern)
    - 组合实体模式(Composite Entity Pattern)
    - 数据访问对象模式(Data Access Object Pattern)
    - 前端控制器模式(Front Controller Pattern)
    - 拦截过滤器模式(Intercepting Filter Pattern)
    - 服务定位器模式(Service Locator Pattern)
    - 传输对象模式(Transfer Object Pattern)
- 设计模式的六大基本原则
  - 开闭原则
    - 对扩展开放，对修改关闭
    - 即提倡用增加代码的方式扩展程序功能，而不是用修改代码的方式
  - 里氏代换原则
    - 任何基类能出现的地方，子类也一定能出现，
    - 即程序应该向后兼容，或者向子代兼容
  - 依赖倒转原则
    - #？？？？？？？？依赖抽象而不依赖具体
  - 接口隔离原则
    - 要求程序低耦合，要求接口功能不要相互依赖（从软件架构出发）
  - 迪米特法则，最少知道原则
    - 要求一个实体尽量少的与其他实体发生关系，使之实现高内聚（从实体程序出发）
  - 合成复原原则
    - 尽量使用合成或者聚合的方法编成，而不使用继承。
#### 工厂模式
- 比如一个画图程序中可以绘制 正方形 长方形 圆形 三角形 梯形 ...等 图形，他们均实现了接口 Shape{+draw():void}
如此多，具有共性使用场景（绘制时）的类，如果直接暴露给使用者，将变得难以管理
所以这里使用一个工厂类，去创建正方形 长方形等类的实例，是一个非常便于管理的方法，如果后续需要扩充类型，只需要对工厂类进行扩充即可
- 在比如，在汽车工厂中有很多型号的汽车，他们都是汽车的子类，对于获取对象可以使用工厂类的的方法，返回给定信息的汽车对象的实例。
- 程序如下：
  - Shape.java 创建绘图接口
    ```java
    public interface Shape {
       void draw();
    }
    ```
    - Rectangle.java 创建绘图接口实现类 长方形
    ```java
    public class Rectangle implements Shape {
    
    @Override
    public void draw() {
      System.out.println("Inside Rectangle::draw() method.");
    }
    }
    ```
    - Square.java 创建绘图接口实现类 正方向
    ```java
    public class Square implements Shape {
    @Override
    public void draw() {
      System.out.println("Inside Square::draw() method.");
    }
    }
    ```
    - ShapeFactory.java 创建工厂类，返回给定信息的实体类
    ```java
    public class ShapeFactory {
    
    //使用 getShape 方法获取形状类型的对象
    public Shape getShape(String shapeType){
      if(shapeType == null){
         return null;
      }  
      if(shapeType.equalsIgnoreCase("CIRCLE")){
         return new Circle();
      } else if(shapeType.equalsIgnoreCase("RECTANGLE")){
         return new Rectangle();
      } else if(shapeType.equalsIgnoreCase("SQUARE")){
         return new Square();
      }
      return null;
    }
    }
    ```
