import random
import time


# 创建一个类，可实例化成具体的游戏角色
class Role:
    def __init__(self, name='【角色】'):  # 把角色名作为默认参数
        self.name = name
        self.life = random.randint(100, 150)
        self.attack = random.randint(30, 50)


# 创建3个子类，可实例化为3个不同的职业

class Knight(Role):
    def __init__(self, name='【圣光骑士】'):  # 把子类角色名作为默认参数
        Role.__init__(self, name)  # 利用了父类的初始化函数
        self.life = self.life * 5  # 骑士有5份血量
        self.attack = self.attack * 3  # 骑士有3份攻击力

    # 职业克制关系
    def fight_buff(self, opponent, str1, str2):
        if opponent.name == '【暗影刺客】':
            self.attack = int(self.attack * 1.5)
            print('『%s』【圣光骑士】对 『%s』【暗影刺客】说：“让无尽光芒制裁你的堕落！”' % (str1, str2))


class Assassin(Role):
    def __init__(self, name='【暗影刺客】'):
        Role.__init__(self, name)
        self.life = self.life * 3
        self.attack = self.attack * 5

    # 职业克制关系
    def fight_buff(self, opponent, str1, str2):
        if opponent.name == '【精灵弩手】':
            self.attack = int(self.attack * 1.5)
            print('『%s』【暗影刺客】对 『%s』【精灵弩手】说：“主动找死，就别怪我心狠手辣。”' % (str1, str2))


class Bowman(Role):
    def __init__(self, name='【精灵弩手】'):
        Role.__init__(self, name)
        self.life = self.life * 4
        self.attack = self.attack * 4

    # 职业克制关系
    def fight_buff(self, opponent, str1, str2):
        if opponent.name == '【圣光骑士】':
            self.attack = int(self.attack * 1.5)
            print('『%s』【精灵弩手】对 『%s』【圣光骑士】说：“骑着倔驴又如何？你都碰不到我衣服。”' % (str1, str2))


# 创建一个类，可生成3V3并展示：可分为：欢迎语→随机生成→展示角色
class Game():
    def __init__(self):
        self.players = []  # 存玩家顺序
        self.enemies = []  # 存敌人顺序
        self.score = 0


import time


# 创建一个类，可实例化成具体的游戏角色
class Role:
    def __init__(self, name='【角色】'):  # 把角色名作为默认参数
        self.name = name
        self.life = random.randint(100, 150)
        self.attack = random.randint(30, 50)


# 创建3个子类，可实例化为3个不同的职业

class Knight(Role):
    def __init__(self, name='【圣光骑士】'):  # 把子类角色名作为默认参数
        Role.__init__(self, name)  # 利用了父类的初始化函数
        self.life = self.life * 5  # 骑士有5份血量
        self.attack = self.attack * 3  # 骑士有3份攻击力

    # 职业克制关系
    def fight_buff(self, opponent, str1, str2):
        if opponent.name == '【暗影刺客】':
            self.attack = int(self.attack * 1.5)
            print('『%s』【圣光骑士】对 『%s』【暗影刺客】说：“让无尽光芒制裁你的堕落！”' % (str1, str2))


class Assassin(Role):
    def __init__(self, name='【暗影刺客】'):
        Role.__init__(self, name)
        self.life = self.life * 3
        self.attack = self.attack * 5

    # 职业克制关系
    def fight_buff(self, opponent, str1, str2):
        if opponent.name == '【精灵弩手】':
            self.attack = int(self.attack * 1.5)
            print('『%s』【暗影刺客】对 『%s』【精灵弩手】说：“主动找死，就别怪我心狠手辣。”' % (str1, str2))


class Bowman(Role):
    def __init__(self, name='【精灵弩手】'):
        Role.__init__(self, name)
        self.life = self.life * 4
        self.attack = self.attack * 4

    # 职业克制关系
    def fight_buff(self, opponent, str1, str2):
        if opponent.name == '【圣光骑士】':
            self.attack = int(self.attack * 1.5)
            print('『%s』【精灵弩手】对 『%s』【圣光骑士】说：“骑着倔驴又如何？你都碰不到我衣服。”' % (str1, str2))


# 创建一个类，可生成3V3并展示：可分为：欢迎语→随机生成→展示角色
class Game():
    def __init__(self):
        self.players = []  # 存玩家顺序
        self.enemies = []  # 存敌人顺序
        self.score = 0  # 比赛积分
        self.i = 0  # 记轮次
        # 依次执行以下函数
        self.game_start()  # 欢迎语
        self.born_role()  # 随机生成6个角色
        self.cooperat_role()
        self.show_role()  # 展示角色

    # 欢迎语
    def game_start(self):
        print('------------ 欢迎来到“炼狱角斗场” ------------')
        print('在昔日的黄昏山脉，奥卢帝国的北境边界上，有传说中的“炼狱角斗场”。')
        print('鲜血与战斗是角斗士的归宿，金钱与荣耀是角斗士的信仰！')
        print('今日，只要你【你的队伍】能取得胜利，你将获得一笔够花500年的财富。')
        time.sleep(2)
        print('将随机生成【你的队伍】和【敌人队伍】！')
        input('\n狭路相逢勇者胜，请按任意键继续。\n')

    # 随机生成6个角色
    def born_role(self):
        for i in range(3):
            self.players.append(random.choice([Knight(), Assassin(), Bowman()]))
            self.enemies.append(random.choice([Knight(), Assassin(), Bowman()]))

    def cooperat_role(self):
        if self.players[0].name  == self.players[1].name  and self.players[0].name  == self.players[2].name :
            for i in self.players:
                i.attack = int(i.attack * 1.25)
            print("团队合作，我方攻击力提升50%,分别为{0}{1}{2}".format(self.players[0].attack,self.players[1].attack,self.players[2].attack))
        if self.enemies[0].name  == self.enemies[1].name  and self.enemies[0].name  == self.enemies[2].name :
            for i in self.enemies:
                i.attack = int(i.attack * 1.25)
            print("敌方老贼团队合作攻击力提升50%,分别为{0}{1}{2}".format(self.enemies[0].attack,self.enemies[1].attack,self.enemies[2].attack))
        if self.players[0].name !=self.players[1].name  and self.players[0].name !=self.players[2].name  and self.players[1].name !=self.players[2].name :
            for i in self.players:
                i.attack = int(i.attack * 1.25)
            print("搭配干活不累，我方攻击力提升50%,分别为{0},{1},{2}".format(self.players[0].attack,self.players[1].attack,self.players[2].attack))
        if self.enemies[0].name  != self.enemies[2].name  and self.enemies[0].name  != self.enemies[1].name  and self.enemies[1].name  != self.enemies[2].name :
            for i in self.enemies:
                i.attack = int(i.attack * 1.25)
            print("敌方老贼男女搭配干活不累攻击力提升50%,分别为{0}{1}{2}".format(self.enemies[0].attack,self.enemies[1].attack,self.enemies[2].attack))


    # 展示角色
    def show_role(self):
        print('----------------- 角色信息 -----------------')
        print('你的队伍：')
        for i in range(3):
            print('『我方』%s 血量：%s  攻击：%s' %
                  (self.players[i].name, self.players[i].life, self.players[i].attack))
        print('--------------------------------------------')

        print('敌人队伍：')
        for i in range(3):
            print('『敌方』%s 血量：%s  攻击：%s' %
                  (self.enemies[i].name, self.enemies[i].life, self.enemies[i].attack))
        print('--------------------------------------------')
        input('请按回车键继续。\n')
        # 比赛积分
        self.i = 0  # 记轮次
        # 依次执行以下函数
        self.game_start()  # 欢迎语
        self.born_role()  # 随机生成6个角色
        self.show_role()  # 展示角色
        self.order_role()  # 排序并展示
        self.pk_role()  # 让双方 Pk 并展示结果
        self.show_result()  # 展示最终结局


    # 欢迎语
    def game_start(self):
        print('------------ 欢迎来到“炼狱角斗场” ------------')
        print('在昔日的黄昏山脉，奥卢帝国的北境边界上，有传说中的“炼狱角斗场”。')
        print('鲜血与战斗是角斗士的归宿，金钱与荣耀是角斗士的信仰！')
        print('今日，只要你【你的队伍】能取得胜利，你将获得一笔够花500年的财富。')
        time.sleep(2)
        print('将随机生成【你的队伍】和【敌人队伍】！')
        input('\n狭路相逢勇者胜，请按任意键继续。\n')


    # 随机生成6个角色
    def born_role(self):
        for i in range(3):
            self.players.append(random.choice([Knight(), Assassin(), Bowman()]))
            self.enemies.append(random.choice([Knight(), Assassin(), Bowman()]))
game=Game()