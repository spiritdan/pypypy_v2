# 更具有程序猿思想
import random

class Role():
    def __init__(self, name='【角色】'):  # 把角色名作为默认参数
        self.name = name
        self.life = random.randint(100,150)
        self.attack = random.randint(30,50)

# 创建三个子类，可实例化为3个不同类型的角色
class Knight(Role):
    def __init__(self, name='【圣光骑士】'):   # 把子类角色名作为默认参数
        Role.__init__(self,name)  # 利用了父类的初始化函数
        self.life = self.life*5  # 骑士有5份血量
        self.attack = self.attack*3    # 骑士有3份攻击力

class Assassin(Role):
    def __init__(self, name='【暗影刺客】'):
        Role.__init__(self,name)
        self.life = self.life*3
        self.attack = self.attack*5

class Bowman(Role):
    def __init__(self, name='【精灵弩手】'):
        Role.__init__(self,name)
        self.life = self.life*4
        self.attack = self.attack*4

a = Role()
print(a.name + '的血量是' + str(a.life) + '；攻击力是' + str(a.attack))

b = Knight()
print(b.name + '的血量是' + str(b.life) + '；攻击力是' + str(b.attack))

c = Assassin()
print(c.name + '的血量是' + str(c.life) + '；攻击力是' + str(c.attack))

d = Bowman()
print(d.name + '的血量是' + str(d.life) + '；攻击力是' + str(d.attack))