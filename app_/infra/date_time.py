from datetime import datetime

def curr_date():
    return datetime.now().strftime("%d")

def curr_month():
    return datetime.now().strftime("%m")