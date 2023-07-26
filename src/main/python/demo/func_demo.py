def function_name(data):
    res = data + 1
    return res
# 循环 for while
# 没有return的就会默认返回0

a=function_name(100)
print(a)

# 匿名函数 通过lambda定义，定义时不用指定函数名, data就是接收参数，冒号后是data的计算逻辑 计算后会自动将结果返回
lambda data:data+1
lambda data1,data2:data1+1+data2
# 使用时，用变量接收lambda

lf=lambda data:data+1
lfres=lf(333)
print("data:{0}".format(lfres))


def fun2():
    print("zhixingfun2")

def fun1(f):
    # 匿名函数调用
    f()
    print("执行fun1")

fun1(fun2)


def fun3(f):
    res = f(10)
    print("res = {0}".format(res))

fun3(lambda x:x+2)



