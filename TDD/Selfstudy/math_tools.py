def add(a, b):
    return a + b

if __name__ == '__main__':
#     # This only runs if I do: python math_tools.py
#     # 只有当我执行 python math_tools.py 时才会运行
    print("Testing add function:")
    print(add(10, 5))   

class Dog:
    # 构造函数：初始化对象的属性
    # Constructor: Initialize object attributes
    def __init__(self, name, breed):
        self.name = name   # 属性 Attribute
        self.breed = breed # 属性 Attribute

    # 方法：对象的行为
    # Method: Object behavior
    def bark(self):
        print(f"{self.name} is barking: Woof!")

# 使用类创建对象
# Creating an object using the class
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark() # 输出: Buddy is barking: Woof!