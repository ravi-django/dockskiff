from datetime import datetime, timedelta


def get_saturdays(s_d, e_d):
    """Getting saturdays days between 2 days"""
    for d in range(int((e_d - s_d).days) + 1):
        if (s_d + timedelta(d)).weekday() == 5:
            yield s_d + timedelta(d)


def print_interval_days(d):
    """Get interval days"""
    # check 4th saturday or not
    # starting day of month
    is_4th_st = d.day in range(22, 28 + 1)
    # is divisible by 5
    str_dt = datetime.strftime(d, '%Y%m%d')
    is_div = int(str_dt) % 5 == 0
    if (is_4th_st or is_div) and not (is_4th_st and is_div):
        print(str_dt)


if __name__ == '__main__':

    start_date_str = str(input("enter start date: "))
    end_date_str = str(input("enter end date: "))
    s_d = datetime.strptime(start_date_str, '%Y%m%d')
    e_d = datetime.strptime(end_date_str, '%Y%m%d')
    s_days = get_saturdays(s_d, e_d)

    for s_day in s_days:
        print_interval_days(s_day)
