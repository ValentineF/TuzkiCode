# 依赖倒置原则
- SOLID的原则之一：传统的依赖关系是高层依赖于底层，以此种解耦形式使得高层次的模块不依赖于低层次模块的实现细节，依赖关系颠倒，从而使得低层次模块依赖于高层次模块的需求抽象（*抽象类或者接口*）
# IOC(Inversion of Control,控制反转)
- 定义：OOP的一种设计原则，用来降低耦合度
- 方式：A.依赖注入（被动） B.依赖查找（主动）
- 流程：通过IOC，对象在被创建时，由一个调控系统（**即IOC容器**）内所有对象的外界实体，将其所依赖的对象的引用传递给他
- 实现了将控制权交由第三方容器即IOC容器，此后对象的维护就交与容器
- 举例：
    - 甲方要达成某种目的不需要直接依赖乙方，它只需要达到的目的告诉第三方机构就可以了，比如甲方需要一双袜子，而乙方它卖一双袜子，它要把袜子卖出去，并不需要自己去直接找到一个卖家来完成袜子的卖出。它也只需要找第三方，告诉别人我要卖一双袜子。这下好了，甲乙双方进行交易活动，都不需要自己直接去找卖家，相当于程序内部开放接口，卖家由第三方作为参数传入。甲乙互相不依赖，而且只有在进行交易活动的时候，甲才和乙产生联系

    - 支付宝在整个淘宝体系里就是庞大的ioc容器，交易双方之外的第三方，提供可靠性可依赖可灵活变更交易方的资源管理中心。另外人事代理也是，雇佣机构和个人之外的第三方
- 依赖：即当A类在初始化或运行到某一点必须去创建使用类B，这个时候称为A依赖B，控制权在B

- 优点: 
    - 甲乙可以在对方不真实存在的情况下独立存在，而且保证不交易时候无联系，想交易的时候可以很容易的产生联系。甲乙交易活动不需要双方见面，避免了双方的互不信任造成交易失败的问题。因为交易由第三方来负责联系，而且甲乙都认为第三方可靠。那么交易就能很可靠很灵活的产生和进行了。

    - 资源不由使用资源的双方管理，而由不使用资源的第三方管理，这可以带来很多好处。第一，资源集中管理，实现资源的可配置和易管理。第二，降低了使用资源双方的依赖程度，也就是我们说的耦合度。

- IOC容器：拥有控制权，实现申请，初始化，管理，销毁对象等等复杂的过程

# 依赖注入（Dependency Injection）
- 与IOC不同的是，它是一种设计模式
### 具体实现有如下：
 - 基于接口： 实现特定接口（*规定标准*）以供外部容器注入所依赖类型的对象(*即相当于把接口作为**参数**注入到了容器之中*)
 ```
    Class Car
    {
        private FrameWork framework;
        Car(FrameWork framework)
        {
            this.framework = framework;
        }
    }

    Interface FramrWork
    {
        ...
    }

    Class BMWFrameWork implemnts FrameWork
    {
        ...
    }
 ```
 - 基于构造函数： 实现特定参数的构造函数，在新建对象时传入所依赖类型的对象（*把类作为参数送入了构造函数*）
 ```
    //难于初始化，应为外部传入的Father容易变化比如Father(string name)
    public class Human {
        ...
        Father father;
        ...
        public Human() {
            father = new Father();
        }
    }

    //将fater对象作为构造函数的一个参数传入
    public class Human {
        ...
        Father father;
        ...
        public Human(Father father) {
            this.father = father;
        }
    }
```
# Reference
1. [IOC/DIP其实是一种管理思想](http://coolshell.cn/articles/9949.html)

2. [控制反转（IoC）与依赖注入（DI）](http://blog.xiaohansong.com/2015/10/21/IoC-and-DI/)

3. [Spring IoC有什么好处呢？](https://www.zhihu.com/question/23277575)

4. [控制反转--WIKI](https://zh.wikipedia.org/wiki/%E6%8E%A7%E5%88%B6%E5%8F%8D%E8%BD%AC)
