# 所有金钱以1元为单位！


def fund_cal(money_cur, profit, money_add_every_year):
    if profit < 0:
        return
    years_count = 0
    money_res = money_cur
    while years_count < 20:
        money_res = money_res * (1 + profit) + money_add_every_year
        years_count += 1
        print(f"years: {years_count}, money: {money_res:.1f}")


# 固定周期利率，固定周期，确定结果
def fix_profits_cal_res(init_money, monthly_add, profit, cycles, dsp=False):
    part_one = init_money * ((profit + 1) ** cycles)
    part_two = 0
    for index in range(cycles):
        part_two += (profit + 1) ** index
    part_two *= monthly_add
    result = part_one + part_two
    if dsp:
        print(f"初始资金: {init_money}¥")
        print(f"周期投入: {monthly_add}¥")
        print(f"周期收益: {profit * 100}%")
        print(f"总周期数: {cycles}")
        print("---------------------")
        print(f"最终结果: {result:.1f}¥")
        print(f"投资收益: {result - (monthly_add * cycles + init_money):0.1f}¥\n")
    return result


# 计算每月投资平均值，理想情况，假设每个月不可能超过10%收益
def automatic_investment_plan_monthly(init_money, money_future, profit_monthly, how_many_months, dsp=False) -> float:
    if profit_monthly > 0.1:
        print("10% every month? You may in a dream! Give up it!")
        return 0
    if init_money >= money_future or profit_monthly < 0 or init_money < 0 or how_many_months <= 1:
        return 0
    max_monthly_add = (money_future - init_money) / how_many_months
    min_monthly_add = 1
    while fix_profits_cal_res(init_money, min_monthly_add, 0.1, how_many_months) < money_future:
        min_monthly_add += 1
    while max_monthly_add - min_monthly_add > 1:
        mid = (max_monthly_add + min_monthly_add) / 2
        if fix_profits_cal_res(init_money, mid, profit_monthly, how_many_months) > money_future:
            max_monthly_add = mid
        else:
            min_monthly_add = mid
    print(f"初始资金: {init_money}¥")
    print(f"目标资金: {money_future}¥")
    print(f"每月收益: {profit_monthly * 100}%")
    print(f"总月数: {how_many_months}")
    print("---------------------")
    print(f"每月金额: {min_monthly_add:.1f}¥")
    print(f"投资收益: {money_future - (min_monthly_add * how_many_months + init_money):0.1f}¥\n")
    return min_monthly_add