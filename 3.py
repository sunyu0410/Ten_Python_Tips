# 3 Using utf-8 in your code

# Python 3 uses utf-8 by default

class Person():
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
    
    def introduce(self):
        print(f"Hello, my name is {self.name},"
              f" and I'm a {self.occupation}.")

person1 = Person('David Jones', 'brand')
person1.introduce()






# class 人物():
#   def __init__(自身, 名字, 职业):
#     自身.名字 = 名字
#     自身.职业 = 职业
  
#   def 报告(自身):
#     print(f"大家好，我叫{自身.名字}，我是一个{自身.职业}。")


# 人物1 = 人物('大卫琼斯', '品牌')
# 人物1.报告()
