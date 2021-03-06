# -- coding: utf-8 --


#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

g = (x * x for x in range(20))

print g #输出的并不是每一项数据，而是生成器对象，如何打印每一项数据呢

print g.next()

print '11111'

for x in g:
    print x

#generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

#比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

#1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fib(max):

    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a+b
        n = n+1

print fib(15)

#仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

#也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print b改为yield b就可以了：

def fibGen(max):
    n, a, b = 0, 0, 1

    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1

fibGen = fibGen(6)
print fibGen

#<generator object fibGen at 0x10acd1320>

#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

#这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5


o = odd()

print o.next()

#>> step 1
#>> 1


print o.next()
#>> step 2
#>> 3


print o.next()
#>> step 3
#>> 5

#可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next()就报错。

#回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。

#同样的，把函数改成generator后，我们基本上从来不会用next()来调用它，而是直接使用for循环来迭代




