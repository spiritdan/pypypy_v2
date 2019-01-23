import time
import datetime
input("欢迎使用“时间管理器”！请按回车继续。")

while True:
    task_name = input('请输入任务名：')
    task_time = int(input('你觉得自己至少可以专注这个任务多少分钟？输入 N 分钟'))
    input('此次任务信息：\n我要完成的任务：%s\n我至少要专注：%d分钟\n按回车开始计时：' % (task_name, task_time))
    start = time.time()
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    st = str(task_time) + ":00"
    dt = datetime.datetime.strptime(st, "%M:%S")
    # for t in range(task_time*60,0,-1):  # 实际代码：分钟转成秒要乘60，用-1来倒计时。
    str_dt = dt.strftime("%M:%S")

    for x in range(int(task_time) * 60-1, -1, -1):
        dt = dt + datetime.timedelta(seconds=int('-{0}'.format(1)))
        mystr = "倒计时" + dt.strftime("%M:%S")
        print("\b" * (len(mystr) * 2), end="", flush=True)
        print(mystr, end="")
        time.sleep(1)
    print('你已经专注了 %d 分钟，很棒~再加把劲，完成任务！' % task_time)  # 倒计时后，才继续运行之后的代码。

    # 询问任务是否完成
    task_status = input('请在任务完成后按输入y:')
    if task_status == 'y':
        end = time.time()
        end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        actual_time = int((end - start) / 60)
        start_end = start_time + '——' + end_time + '\n'
        with open('timelog3.txt', 'a', encoding='utf-8') as f:
            f.write(task_name + ' 的预计时长为：' + str(task_time) + '分钟\n')
            f.write(task_name + ' 的实际时长为：' + str(actual_time) + '分钟,具体时间为：' + start_end)
        again = input('建立一个新任务请按 y, 退出时间日志记录器请按 q：')
        if again == 'q':
            break
    else:
        print('抱歉，你的输入有误。请重启时间记录器。')

print('愿被你善待的时光，予你美好的回赠。')
