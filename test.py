class Survey():
    # 收集调查问卷的答案
    def __init__(self, question):
        self.question = question
        self.response = []

    # 显示调查问卷的题目
    def show_question(self):
        print(self.question)

    # 存储问卷搜集的答案
    def store_reponse(self, new_response):
        self.response.append(new_response)


# 请实例化 Survey() 类，并且显示出这次的调查问卷问题约 2 行代码
food_survey = Survey()

# 存储问卷调查的答案
while True:
    response = input('请回答问卷问题，按 q 键退出：')
    if response == 'q':
        break
    # 请将答案用问卷系统存储起来,约 1 行代码
        food_survey.store_reponse(response)

    # 输出测试
    for food in food_survey.response:
        print('美食：' + food)
