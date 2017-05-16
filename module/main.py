#!/usr/bin/python3.5

import dirfunc

print(dirfunc.add(2,4));
print(dirfunc.sub(2,4));
print(dirfunc.mul(2,4));
print(dirfunc.div(2,4));


#一个模块被另一个程序第一次引入时，其主程序将运行。
#如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。

if __name__ == '__main__':
   print('程序自身在运行');
else:
   print('我来自另一模块');