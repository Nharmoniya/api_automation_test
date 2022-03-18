# 小明和小红比较月薪，小明输入月薪，小红输入月薪，得出结果谁的月薪高
# 根据年薪，扣除五险一金，个税后，计算到手工资,年终奖为一个月工资不用交税
# 假设五险一金比例个是8%，个税是超过5000的部分的百分之1

# def cal(money1, money2):
#     if money1 > money2:
#         print("小明工资高")
#     elif money2 > money1:
#         print("小红工资高")
#     else:
#         print("输入错误请重新输入两人的工资")
#
#
# xiaoming = int(input("请输入小明的工资:"))
# xiaohong = int(input("请输入小红的工资:"))
# cal(xiaoming, xiaohong)


def cal_total(money):
    wuxian = 0.08
    yijin = 0.08
    year = 12
    total = 0
    annual_bonus=money
    if money <= 5000:
        total = (year * (money - (money * wuxian + money * yijin)))+annual_bonus
        print("你的年薪为："+str(total))
    elif money > 5000:
        total = (year * (money - (money * wuxian + money * yijin + ((money - 5000) * 0.01))))+annual_bonus
        print("你的年薪为："+str(total))
    else:
        print("输入有误请重新输入")


yuexin = float(input("请输入自己的月薪:"))
cal_total(yuexin)
