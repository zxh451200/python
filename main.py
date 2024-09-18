# 这是一个示例 Python 脚本。
import time


# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

class test():
    @classmethod
    def print_hi(name):
        # 在下面的代码行中使用断点来调试脚本。
        with open("新建文本文档 (2).txt","r") as fg:
            print(11)


def c(f):
    def c2(*args,**kwargs):
        start=time.time()
        print("c")
        f(*args,**kwargs)
        print("c")
        end=time.time()
        print("耗时{}".format(end-start))
    return c2;
@c
def a():
    time.sleep(1)
    print("a")

@c
def b():
    print("b")



a()

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    c(a)
