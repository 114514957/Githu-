"""
##运算符
    #算数运算符
        +   加法
        -   减法
        *   乘法
        /   除法
        //  整除
        %   取余\求模
        **  幂指数\次方
    #赋值运算符
        =   赋值  将=右边的赋予左边
        +=  加法赋值    等效于x=x+x
        -=  减法赋值
        *=  乘法赋值
        /=  除法赋值
        %=  取模赋值
        //= 取整除赋值
        **= 幂赋值
    #比较运算符
        ==  等于  a == b  判断a是否等于b
        !=  不等于
        >   大于
        >=  大于等于
        <   小于
        <=  小于等于
    #逻辑运算符
        and 与\并且    同时成立才能符合
        or  或\或者    只要有一个成立则符合
        not 非\取反    取反操作,True变为false false变True
        in  是否在容器中    判断一个元素是否在容器中,返回值为True或False
            not in  是否不在容器中    判断一个元素是否不在容器中,返回值为True或False
        None  空值    表示没有值,或未知的值
            not None  是否不是空值    判断一个变量是否不是空值,返回值为True或False
##流程控制语句
        if  条件成立时执行
        elif    否则
        else    前面条件都不成立,则
        match...case   条件匹配    match指定表达式,从上到下依次和case的值进行匹配,匹配成功则执行如果前面所有case都没匹配上,则执行默认的case_
    #循环
        while   通过条件表达式循环,如果循环体为True,则循环,如果为false则结束,如果之后有else则结束循环后执行else
        for 元素 in 待处理的数据集:  for循环本质是一种循环遍历,
    #for循环数据集函数
        range() 生成整数序列
        enumerate()    在循环中同时获取元素的索引和值
        zip()   需要同时遍历两个以上的序列时
    #循环体    循环里套循环
##数据类型：字符串str，整数int，浮点数float，布尔类型bool 复数类型complex
##数据容器
    字符串    "123"   "abc"
    列表list     [中括号]   i=[1,2,3,a,b,c,True,"asd"[4,5]]    可以增删查改
    元组tuple    (小括号)   i=(1,2,3,4)   不可修改 提取时用[]取下标 #如果定义单元素的元组需要加上逗号(100,)
    字典dict     {花括号}   i={"name":名,"age":18}   由键值对组成，前叫键，后叫值，一一对应,通过键可以找值,值可以有多个，每对间用逗号分割,不可用列表集合等可变类型做键,可以增删查改
    集合set      {花括号}   i={1，2，3，4，5，6}   无序，不重复
    import random#生成随机数random,随机变量 = random.randint(a,b)
##字符串常用方法
    #转换
        join()   将列表转换为字符串,默认用空格分隔,也可以指定分隔符
        s="".join(["a","b","c"])/s="-".join(["1","2","3"])
    #批量输出
        print("# " *10)
##列表常用方法：
    #添加
        append()    在列表尾部追加元素   s.append(114514)
        insert()    在指定元素之前加入该元素    s.insert(0,114514)
    #删除
        remove()    移除列表中匹配到的第一个元素  s.remove(114514)
        pop()   删除列表中指定索引位置的元素(默认删除最后一个)    s.pop(2)/s.pop()
    #排序
        sort()  对列表进行排序    s.sort()#默认升序
        sort()  对列表进行排序    s.sort(reverse=True)#降序
        sorted()  对列表进行排序    sorted(s)#返回一个新的列表,不会改变原列表
    #反转
        reverse()   反转列表元素     S.sort(reverse=True)
    #列表去重复
        if a in b 则添加不存在于a的元素
    #列表解包
        *i *符号为解包
    #列表推导式
        [要插入的值 for i in 列表\序列 if 条件]
    #转换
        int()   将列表转换为整数    s=int([1,2,3])
        float() 将列表转换为浮点数    s=float([1,2,3])
        str()   将其他类型转换为字符串    s=str(123)
        s = list(s) 将列表转换为列表
##元组常用方法：
    #查找
        find()  在元组中查找子串，返回第一次出现的索引位置，找不到返回-1    s.find("hello")
        count() 统计子串在元组中出现的次数   s.count("hello")
    #转换大小写
        s = tuple(s) 将列表转换为元组
        upper() 将元组中所有字母转换为大写   s.upper()
        lower() 将元组中所有字母转换为小写   s.lower()
        split() 将元组按指定分隔符分隔成列表  s.split('  ')
        strip() 去除元组两端的空白字符或指定字符    s.strip()/s.strip("*")
        replace()   将元组中指定的子串替换为新的子串  s.replace("hello","world")
        startswith()    检查元组是否以指定子串开头，返回布尔值    s.startswith("hello")
    #转换
        list()    将元组转换为列表
        count() 统计某个元素在元组中出现的次数
        index() 查找某个元素在元组中的索引位置(第一次出现的位置)
    #组包与解包
        Packing():  组包,将多个值合并到一个容器(元组,列表)
        t1=(1,2,3,4,5)
        t2=1,2,3,4,5
        Unpacking():    将容器(元组,列表)解开成独立的元素,分别赋值给多个变量
        a,s,b,c,d,e,f,g=t1(基础解包,要求变量与元素数量相同)
        first,second,*other,last=t1(扩展解包,在变量前加*可以让变量收集剩余的元素并封装)
##集合常用方法
    #添加
        add()   添加元素到集合中   s1.add("t")
    #删除
        remove()    移除集合中的指定元素(指定元素不存在将报错)  s1.remove("t")
        pop()   随机删除集合中的元素并返回  e=s1.pop()
        clear() 清空集合  s1.clear()
    #运算
        difference()     或 .- 求取两个集合的差集(包含第一个集合但不包含第二个)  s1.difference()
        union() 求两个集合的并集  或 .| s1.union(s2)
        intersection()  求两个集合的交集  或 .& s1.intersection(s2)
    #集合推导式
        变量名称=(i表达式 for i in 列表)
        变量名称=(i表达式 for i in 列表 if 条件)
##字典常用方法
        字典名称[key] = value   在指定字典中添加key-value键值对
        字典名称.pop(key)   删除字典中指定的键,并返回key对应的value
        del 字典名称[key]   删除字典中的指定键值对
        字典名称[key] = value   修改字典中key对应的值value
        字典名称[key]   根据key获取value的值
        字典名称.get(key)   根据key获取value的值
        字典名称.keys()    获取所有的key\键
        字典名称.values()   获取所有的value
        字典名称.items()    获取所有的键值对
        字典名称.update()   用另一个字典或键值对更新当前字典  d.update({"age":19})
        字典名称.setdefault(key, default)   获取键对应的值，若键不存在则设置默认值并返回  d.setdefault("name", "未知")
    #字典推导式
        {key: value for key, value in 序列 if 条件}
##函数    组织好的,可重复使用的,实现指定功能的片段
    #内置函数
        sum()   列表求和
        print() 打印
        len()   总结列表\元组\字符串中元素数量  需要变量存储，有返回值
        type()  检查对象类型
        min()   最小值
        max()   最大值
        round()   四舍五入
        pow()   指数
        abs()   绝对值
        isinstance()    判断对象是否是某个类型的实例
        dir()   查看对象的所有属性和方法
        help()  查看对象的文档字符串
        eval()  评估字符串表达式,返回表达式的值
        exec()  执行字符串代码,返回None
    #random模块
        import random
        random.randint(a,b)    生成[a,b]之间的随机整数
        random.choice(序列)    从序列中随机选择一个元素
        random.shuffle(序列)    随机打乱序列中的元素
    #字符串方法
        strip() 去除字符串首尾指定字符(默认是空格,换行)
        replace()   替换
        find()  查找指定元素,找不到返回-1
        count() 计算某个元素出现次数,作用于字符串,列表,元组
    #列表方法
        sort()    排序  不需要变量存储，没有返回值
        append()   在列表尾部追加元素  不需要变量存储，没有返回值
        insert()    在指定位置插入元素
        index() 查找指定元素位置,找不到报错
    #删除操作
        del 变量   删除变量或元素
#函数
    #定义函数   名称取法和变量名取法一致
        1.数字。字母。下划线
        2.数字不能开头
        3.区分大小写
        4.不能是系统关键字
        5.见名知意
        6.不使用内置函数
        global可以让局部变量变成全局变量
    #形式参数,需要几个加几个
        def 函数名(形式参数1,形式参数2):   #定义函数时括号里的参数时局部变量,只能在本函数内使用
            函数体
    #调取函数方法
        函数名()   #调用返回值时用变量接受然后打印,也可以直接打印函数加实参

    #实际参数
        函数名(实际参数1,实际参数2)#在括号里加
    #形式参数和实际参数,需要一一对应
    #参数类型
        位置参数
        关键字参数  (a=实际1,b=实际2,c=实际3)
        默认值参数  默认写好,不改不加
        可变参数    *args(接收任意数量的位置参数), **kwargs(接收任意数量的关键字参数)
    #print函数参数
        print(形式1,形式2,形式3=某某某, sep="间隔内容", end="\n")  # sep表示分隔符, end表示结束符
    #返回值
        return值
        def 函数名():
            return要返回的参数
    #Lambda函数(匿名函数)
        lambda 参数: 表达式  # 如 lambda x: x*2

    #函数传参
        def 函数名(形式参数1,形式参数2):
        #关键字传参   以键=值的形式传参
        def 函数名(name1,name2,name3,name4)
           调用函数
            函数名(name1="张三",name2="李四",name3="王五",name4="赵六")
        #位置参数传参   以顺序传参
        def 函数名(name1,name2,name3,name4)
           调用函数
            函数名("张三","李四","王五","赵六")
        #混合传参   先位置参数,再关键字参数
        def 函数名(name1,name2,name3,name4)
           调用函数
            函数名("张三","李四",name4="赵六",name3="王五")
    #默认值参数   默认写好,不改不加
    #参数类型
        #普通参数:数字,字符串,列表,元组,字典,集合字典
        #特殊参数:函数,类,模块
    def 函数名(形式参数1,形式参数2=默认值2):#默认值参数,默认值必须是不可变类型,否则会报错
        函数体
        return值
    #不定长参数   接收任意数量的位置参数或关键字参数
    def 函数名(*形式参数1,**形式参数2):#*args接收任意数量的位置参数(元组),**kwargs接收任意数量的关键字参数(字典)#*args和**kwargs必须在形式参数的最后面
        函数体
        return值
    #匿名函数 没有名称的参数,通过lambda表达式定义(单行表达式)
        lambda 参数列表 : 表达式
        lambda : print("----------")
        lambda x,y:x-y
        #匿名函数不可直接调用,需要赋值给变量
        out_line = lambda : print("----------")
        sub=lambda x,y:x-y
        调用
        out_line()
        print(sub(10,5))
        #注意:匿名函数比较简单,且只在当前区域有效,
            匿名函数可以返回结果,也可以不返回结果,返回时不需要return,直接写表达式即可
    #sort函数
        sort(序列,key=函数,reverse=布尔值)
        sort(序列,key=lambda x:x[0],reverse=False)
        #key函数  用于指定排序的依据
        #reverse布尔值  是否反向排序
        #默认是升序排序
    #类型注解
        def 函数名(形式参数1:类型,形式参数2:类型)->返回值类型:
        变量: 类型 = 值(记得空格)
        变量: 容器 [类型] =值 以这种形式注解,可以提高代码的可读性和可维护性
        变量: 字典 [键:类型,值:类型] =值 可以分别对键和值注释
        变量: 元组 [类型,类型,类型] =值 可以对元组中的每个元素注释
        在类型注释时容器可以存在多种类型,用 | 分隔,pycharm会自动判断类型
        函数的参数和返回值也可以进行类型注释
        def 函数名(形式参数1:类型,形式参数2:类型)->返回值类型:
        返回值用->进行注释
        多个值返回时,用元组包裹 tuple(int,str,bool)分别注释每个值的类型
    #装饰器
        @decorator  # 用于修改函数行为
模块和包
    #模块
        每一个.py文件就是一个模块,可以包含多个函数,类,变量等
        自己写的时自定义模块,python也自带模块
    #常量
        不会发生变化的量,常量名用大写

    #导入模块
        import module  # 调用方式,模块名 功能名
        import 模块名 as 别名 # 调用方式 别名
        from 模块名 import 功能名 # 调用方式 功能名
        from 模块名 import 功能名 as 别名 # 调用方式 别名
        from 模块名 import * # 调用方式 所有功能名
    #包
        包含__init__.py文件的目录，用于组织模块
##面向对象思想
    #类:描述的时一组具有相同属性和方法的模板
    #对象时由类创建出来的,创建对象的过程也称为对象的实例化,一个类可以有无数个对象
##类
    #类的定义
    # 动态添加 #类名命名会犯遵循每个单词首字母大写,单词间不分隔
        # class 类名:
        #     pass  #暂停
        # 对象名 = 类名()
        # 对象名.属性名 = 属性值
        #__dict__是pythen中自定义实例的特殊属性,用于以字典形式存储对象的属性
        #class Car:
        # pass
        # c1 = car()
        #ci.name = "111"
        #c1.x = 114514
        #print(c1)#只会输出内存地址
        #print(ci.__dict__)#以字典的形式输出
    #指定添加
        #class 类名:
            # def__init__(self.#参数列表,参数1,参数2,参数3) #__init__方法是初始化对象的方法对象创建后自动调用
            #     self.属性名 = 参数值 #self方法的第一个参数,表示当前的实例对象
#                                       #定义在类外面的叫函数,在里面的叫方法
        #c1 = Car(实参1,实参2,实参3):
        # print(c1.__dict__)
    #实例方法
        #对象名 = 类名
        #对象名.方法名(实参)
    #魔法方法:以双下划线开头和结尾的特殊方法,用于定义类的特殊行为,不需要主动调用
        #魔法方法常用方法
            __init__    初始化方法
            __str__ 字符串表示方法
            __eq__  比较两个对象是否相等(equal)
            __lt__,__le__,__gt__,__ge__ 支持比较两个对象大小(小于(less,than),小于等于(less 听哈
             or equal),大于等于(greater than),大于等于(great than or equal)
        #使用方法:
            def __init__(self,*args,**kwargs):
            def __str__(self):
            def __eq__(self,other):
            return self.对象名1 == other.对象名2
    #属性
        #实例属性:属于每个具体对象,每个对象都是独立的,放在def __init__(self,*args,**kwargs):下
        #类属性:属于类型本身,所有实例共享,放在class 类名:下
"""
# class Cat:
#     def __init__(self,name):
#         self.name = name #具体名字   我的属性=具体的属性值
#         self.age=2
#         print(f"我叫:{self.name},今年{self.age}")
#     def eat(self):
#         print(f"{self.name}可以吃")
# #def 行为函数(self):
#
# #A=Person(\
# A=Cat("c1")
# B=Cat("c2")
# B.eat()
# C=Cat("c3")
"""
##异常处理
    #try-except语句
    try:
        可能异常代码
    except 异常类型 as 变量:
        异常处理代码
    else:
        没有异常的处理代码
    finally:
        有没有异常都会处理的代码
        #try:
            # 可能引发异常的代码,只有在try内部的代码,才会被捕获
        #except  #匹配机制,用来匹配特定异常
            # 如果出现BUG异常处理代码
        #Exception
            #特殊异常类型:Exception所有的异常的父类(顶级异常),任何异常都可抓取
        #else
            #没有异常时会执行的语句段
        #finally:
            # 无论是否发生异常都会执行的代码
    #异常传递:
    异常具有传递性,可以利用这个特性在最终捕获
       
       
解决方法





##文件操作
    #打开文件
        file = open('file.txt', 'r')  # 模式: r(读), w(写), a(追加)
    #读取文件
        content = file.read()  # 读取整个文件
        line = file.readline()  # 读取一行
        lines = file.readlines()  # 读取所有行到列表
    #写入文件
        file.write('content')  # 写入内容
    #关闭文件
        file.close()
    #上下文管理器(自动关闭文件)
        with open('file.txt', 'r') as f:
            content = f.read()

##生成器和迭代器
    #生成器
        def gen():
            yield 1  # 用yield创建生成器
    #迭代器
        class MyIterator:
            def __iter__(self):
                return self
            def __next__(self):
                # 返回下一个元素，没有则 raise StopIteration
"""


