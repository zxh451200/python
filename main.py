# 这是一个示例 Python 脚本。
import time


# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

class test():
    @classmethod
    def print_hi(name):
        # 在下面的代码行中使用断点来调试脚本。
        with open("新建文本文档 (2).txt", "r") as fg:
            print(11)


def timer(params: int):
    def outer(f):
        def inner(*args, **kwargs):
            start = time.time()
            print("c")
            res = f(*args, **kwargs)
            print("c")
            end = time.time()
            print("耗时{}".format(end - start))
            return res;

        return inner

    return outer


@timer(params=3)
def a():
    time.sleep(1)
    print("a")
    return "aaaaaaaaaaa"


@timer(333333333333333)
def b():
    print("b")


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print(a())
