"""
存储方式,文件类型
#文件操作读写常用方法
1.打开
2.读写操作
    (r模式 只读,w模式 写入,a模式 追加)
3.关闭

    #打开已存在的文件或创建新文件
        open( name ,  mode ,  encoding=)
             "文件路径", 打开方式, 编码格式
            name:要打开的目标文件的字符串(路径)
            mode:设置打开的模式(访问模式),只读,写入,追加
                r模式只读   #默认只读
                w模式写入   #不存在新建,存在则删除原内容后写入
                a模式追加   #不存在新建,存在则保留原有之后追加
                b模式二进制处理    #非文本文件必须二进制模式(读取0与1)
            encoding:编码格式(基本使用encoding="UTF-8")

    #读取方法
        read[num]
            num:文件中读取的长度(单位是字节,默认是全部)
            readlines() #相当于read().split("\n"),且一次只读一行
            #readlines可以按照行的方式把整个文件内容进行一次性读取,并且返回值是列表,每一行为一个元素
            #readlines每一行换行不会清除
            readline()#一次只读一行,搭配.strip()使用,readline().strip()
        #用for循环操作读
            for line in open():
            print(line)
            #每一个line临时变量,就记录一个文件的一行数据,自行处理空回撤.strip()
            #语法糖写法
                for line in open():
                print(line.strip()) #同时进行打开open,for循环读取行,循环结束自动close关闭
        #用with open()写法
        with open() as f:
        #这种写法会自动close(在pythen中任何with xxx as xxx写法都可以不需要close
    #写入方法
        f.write()#f.writerows(),列表存储
        #write函数表示将内容写入缓冲区
    #内容刷新
        f.flush()
        #flish函数表示将缓冲区内容写到硬盘(文件)中
    #非文本内容处理
        open("位置","rb")#在模式后加b:"rb","wb","ab"

        dumps:字典转换字符串
        dump:字典写入json文件

ensure_ascii =false#转换成加引号的方式,解决中文乱码
读取时, json.load
#ctrl+alt+l可以自动整理json数据
#excl表格存储
    #1.将数据转换成像表格一样的数据,Dataframe #固定格式,列表中套字典[{},{},{}]
    x=i.DataFrame(data)
    x.to_excl()
#读取:
    a=名字.read_excle()
    print(a)
#csvwenjian,用逗号隔开,数据集,可以用文档显示,也可以用表格打开
    a=csv.writer(f)
    a.writerow(data)    #一行写入,
    data = [            #多行写入
        []
        []
        []
    ]
    a.writerow(data)
    f.close()
    for line in#从什么里遍历获取
"""

