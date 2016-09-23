days = {"Saturday":-2, "Sunday":-1, "Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4}

def n_full_weekends(n_days, start_day):
    n_days += days[start_day]
    if n_days <= 0:
        n_weekends = 0
    else:
        n_weekends = n_days//7
    return n_weekends
    