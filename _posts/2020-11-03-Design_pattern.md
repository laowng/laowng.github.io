---
layout:     post
title:      设计模式学习心得
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
#### 抽象工厂模式
- 抽象工厂模式是工厂模式的一种扩展，即将工厂抽象化，实现生产工厂的“超级工厂”
- 在这里可以进一步理解接口和抽象类的精髓：
  - 使用接口或者抽象类可以经不同的类型进行共性化，这样作的好处是对于函数，允许其返回的对象类型不再单一。
  比如将工厂模式例子中的形状使用接口的方法抽象化后，便可以使用接口类型 “Shape” 去声明函数getShape，这样，getShape
  函数将允许返回多种实现于 ”Shape“ 的类的对象。
  同样的好处还见于形参，如果没有类的继承或者接口实现的策略，那么对应不同类型的形参的同功能方法只能使用重载的方法去实现内部函数。
  相反，使用抽象类的方法去声明形参，便可以将同一个功能聚集在一个函数里，体现高内聚的思想。
  - 接口是对行为的抽象，抽象类是对事物的抽象。抽象类和普通类的区别是，普通类内部不允许有抽象方法，允许实例化。而抽象类必须由子类将其抽象大方全部实现后
  才能实例化。在语法层面上，他们的区别有：
    1. 抽象类可以提供成员方法的实现细节，而接口中只能存在public abstract 方法；
    2. 抽象类中的成员变量可以是各种类型的，而接口中的成员变量只能是public static final类型的；
    3. 接口中不能含有静态代码块以及静态方法，而抽象类可以有静态代码块和静态方法；
    4. 一个类只能继承一个抽象类，而一个类却可以实现多个接口。
  - 这里列举一个抽象类和接口使用场景的例子
    ```java
    //Door.java
    public abstract class Door{//普通门
        public void open(){//开门
        System.out.println("Door open");
        }
        public void close(){//关门
        System.out.println("Door close");
        }
    }
    //Alarm.java
    public interface Alarm{//报警方法集合
        public abstract void alarm();
    }
    //Bell.java
    public interface Bell{//门铃方法集合
        public abstract void bell();
    }
    //SuperDoor.java
    public class SuperDoor extends Door implements Alarm,Bell{//有报警功能和门铃的高档防盗门
        ...
    }
    public abstract class AbstractFactory{
        public abstract Door getDoor {//获取门工厂
        }
        public abstract Door getGlass {//获取玻璃工厂
        }
    }
    public class DoorFactory extends AbstractFactory{
        public Door getDoor(String kind){//实现玻璃工厂
        if(kind.equalsIgnoreCase("superDoor")){
            return new SuperDoor();
        }
        if...;
        ...
        }
        public  Door getGlass {//因为这里是门工厂 所以玻璃工厂可以不实现
            return null;
        }
        
    }

    ```
    - 从以上了例子可以看出，用接口修饰行为 Alarm(报警) Bell(门铃)比较合理，因为接口支持多继承，适合扩展，而对于门这类事物，用抽象类封装可以对其内部进行描述(门的开闭)。
    - 反过来看，如果将Door(门)声明为接口，则给门添加报警，门铃等功能就成为了与门同代的功能，这会让关系混乱
    - 抽象工厂的出现将门 玻璃等工厂进一步继承，是对工厂的进一步抽象化，对于造房子即需要门工厂又需要玻璃工厂这样的使用场景，这种超级工厂的应用使得代码进一步高内聚，低耦合。
#### 单例模式
- 注意：
  1. 单例类只能有一个实例。
  2. 单例类必须自己创建自己的唯一实例。
  3. 单例类必须给所有其他对象提供这一实例。
  4. 应把构造函数私有化
- 应对一个全局使用，却需要频繁创建实列的类
- 列举四种经典解决方案：
  - 懒汉式：使用时再初始化实列，节省内存，但需要在初始函数处加锁，因为多线程下有可能出现多列，但是加锁后会造成效率低下，所以仅适用于无并发不加锁使用。
```java
public class Lazy{
    private Lazy(){}
    private static Lazy instance;
    public static synchronized Lazy getInstance(){
        if(instance ==null){
            instance= new Lazy();
            return instance;
        }else{
            return instance；
        }
    }
}
```
  - 饿汉式：直接在声明时初始化，虽然浪费内存，但是线程安全，适合并发情景下使用。
```java
public class Hungry{
    private Hungry(){}
    private static final Hungry instance=new Hungry();
    public static  Hungry getInstance(){
        return instance；
    }
}
```
  - 双检锁/双重校验锁
```java
public class Lazy{
    private Lazy(){}
    private volatile static Lazy instance;
    public static Lazy getInstance(){
        if(instance ==null){
            synchronized(this){
                if(instance ==null){
                    instance= new Lazy();
                    return instance;
                }else{
                    return instance;
                }
            }    
        }else{
            return instance；
        }
    }
}
```
  - 登记式/静态内部类 对静态域使用延迟初始化，比双检锁方式优秀
```java
public class Register{
    private static class RegisterHandle{
        private static final Register instance = new Register();
    }
    private Register(){}
    public static final Register getInstance{
        return RegisterHandle.instance;
    }
}
```
#### 建造者模式
- 使用多个简单的对象一步一步构建成一个完整的对象，这些简单对象需要提取公共部分。
- 比如，对于一个外卖套餐而言，构成该套餐的各个事物应该是具有不同属性值的相同类别。在建造者模式中会将各种食物分类，比如肉类和蔬菜类。然后进一步对这两种分类
做进一步细节化分类，比如肉类可分为猪肉类和鸡肉类，蔬菜类可分为有机蔬菜和非有机蔬菜。如此自上往下的分类，用接口和继承的方法抽象处新的细化类。
- 最后在建造者类中可以直接调用最底层的细化类，去建造需求对象。在上边例子中的表现是使用套餐制造者类，去直接调用猪肉和有机蔬菜这种细化类去返回食物组合对象。
- **这种模式我认为，相当于在工厂模式的基础上，创建一个建造者的角色，是的该角色能返回不同的对象组合，而这些对象来源于工厂角色。上边举例中，将细化食物封装成工厂，只差一步。**


