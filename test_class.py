class Animal():  # 创建一个父类“动物”
    def __init__(self, name='动物'):
        self.name = name
        self.init_attack=100
        self.attack=self.init_attack  # 动物的攻击力是100


class Cat(Animal):  # 创建一个子类“猫”
    def __init__(self, name='猫'):
        Animal.__init__(self, name)  # 完全继承动物的初始化函数，也就是攻击力还是100

    def fight_buff(self, opponent):
        self.attack=self.init_attack
        # fight_buff的意思是“战斗强化”，opponent的意思是“对手”
        if opponent.name == '老鼠':
            self.attack = int(self.attack * 1.5)


class Rat(Animal):  # 创建一个子类“老鼠”
    def __init__(self, name='老鼠'):
        Animal.__init__(self, name)  # 完全继承动物的初始化函数，也就是攻击力还是100


class Monkey(Animal):  # 创建一个子类“猴子”
    def __init__(self, name='猴子'):
        Animal.__init__(self, name)  # 完全继承动物的初始化函数，也就是攻击力还是100


Tom = Cat()  # 实例化一只叫做Tom的猫
Jerry = Rat()  # 实例化一只叫做Jerry的老鼠
Bobo = Monkey()  # 实例化一只叫做Bobo的猴子



print('猫的攻击力是：')
print(Tom.attack)

Tom.fight_buff(Jerry)
print('遇到老鼠，猫的攻击力是：')
print(Tom.attack)

Tom.fight_buff(Bobo)
print('遇到猴子，猫的攻击力是：')
print(Tom.attack)