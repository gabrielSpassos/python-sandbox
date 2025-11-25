import calendar
from datetime import date

def working_days_in_current_month():
    today = date.today()
    year, month = today.year, today.month
    
    month_calendar = calendar.monthcalendar(year, month)
    print(f"Current year {year} Current Month: {month}")
    
    working_days = sum(
        1
        for week in month_calendar
        for day in week[:5]  # Monday–Friday (0–4)
        if day != 0         # 0 = padding day (not in month)
    )
    
    return working_days

if __name__ == "__main__":
    working_days = working_days_in_current_month()
    print(f"Working days in the current month: {working_days}")
