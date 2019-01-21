# 员工管理系统
# ===总结
# @classMethod
# 【加上面一句本方法可以使用类属性，以下cls为自己定义的变量，
# self也可传递，需放在__init__函数中
# 注意方法中不使用类属性时不能加上面一句】
# 【遗留问题：类名后面的():括号加和不加有什么区别？
# 【遗留问题：此处（看结尾处：实例化类时有一例不成功被阻时保留了上一例结果）两行如果不注掉的话，还会打印一遍小李的信息，也就是说当第二个实例传值不正确被阻止时，它保留了第一个实例的结果？好凌乱】
# 】=
# 创建人事系统类
class staffSystem:  # 【遗留问题：可以不用():加不加有什么区别？不加是对象，加是函数？】

    # 员工姓名、工资、绩效声明
    staffName = ''
    staffSalary = 0  # 类里面为什么还要定义下？可以设置初始值，防止不传参数时报错
    staffKpi = 0
    staffList = ['小王', '小赵', '小钱', '小周', '大王', '大赵', '小李']

    # 检查员工姓名是否在员工列表中
    @classmethod
    def checkStaffName(cls, inputName):
        # 注意:检测名字为输入名字，还没有设成类属性，检测通过才会录入为类属性。
        # 所以此处没用cls.staffName
        if inputName in cls.staffList:
            return True
        else:
            return False

    # 录入员工信息类
    @classmethod
    def setInfo(cls, staffName, staffSalary, staffKpi):

        if cls.checkStaffName(staffName) == True:  # 先检测员工名字是否为公司员工再录入

            cls.staffName = staffName
            cls.staffSalary = staffSalary
            cls.staffKpi = staffKpi

            print("录入正确~")

        else:
            print("录入错误！%s 不是本公司员工！" % staffName)

    # 输入打印员工信息类
    @classmethod
    def showInfo(cls):
        if cls.checkStaffName(cls.staffName) == True:  # 先检测员工名字是否为公司员工再打印
            print(cls.staffName + '的工作信息如下：')
            print('本月工资：%d ' % cls.staffSalary)
            print('本年绩效：%d ' % cls.staffKpi)

    @classmethod
    def showKpiReward(cls):
        if cls.checkStaffName(cls.staffName) == True:  # 先检测员工名字是否为公司员工再评测
            kpi = cls.staffKpi
            name = cls.staffName
            if kpi > 95:
                print("恭喜%s拿到明星员工奖杯！" % name)
            elif 80 <= kpi <= 95:
                print("恭喜%s拿到优秀员工奖杯！" % name)
            elif kpi < 80:
                print("很遗憾%s这次没有评上奖杯，希望来年努力工作，勇创佳绩！" % name)


newStaff = staffSystem()
newStaff.setInfo('小李', 10000, 95)
newStaff.showInfo()
newStaff.showKpiReward()
print("-------------------")
newStaff2 = staffSystem()
newStaff2.setInfo('小王王', 1000, 55)
newStaff2.showInfo()#【遗留问题：此处两行如果不注掉的话，还会打印一遍小李的信息，也就是说当第二个实例传值不正确被阻止时，它保留了第一个实例的结果？好凌乱～】
# newStaff2.showKpiReward()
