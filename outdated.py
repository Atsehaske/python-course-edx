months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    day, month, year = get_date()
    print(f"{year}-{month:02}-{day:02}")



def get_date():
    while True:
        try:
            date = input("Date: ").title().strip()
            if "/" in date:
                month, day, year = date.split("/")
                year, month, day = int(year.strip()), int(month.strip()), int(day.strip())
            elif "," in date:
                month_day, year = date.split(",")
                month, day = month_day.strip().split(" ")

                if month not in months:
                    raise ValueError

                month = months.index(month)+1
                year, day = int(year.strip()), int(day.strip())
            if not(1 <= day <= 31):
                raise ValueError
            if not(1 <= month <= 12):
                raise ValueError
            return day, month, year
        except (ValueError, NameError, UnboundLocalError):
            pass

main()
