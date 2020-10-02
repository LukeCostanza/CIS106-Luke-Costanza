# This program displays the gross pay of an hourly worker.


def display_results(weekly, monthly, annually):
    print("your pay this Week is $" + str(weekly))
    print("your pay this Month is $" + str(monthly))
    print("your pay this Year is $" + str(annually))


def get_hours():
    print("Hours")
    hours = int(input())
    return hours


def get_rate():
    print("rate")
    rate = int(input())
    return rate


def process_weekly(hours):
    weekly = hours * rate
    return weekly


def process_monthly(weekly):
    monthly = weekly * 4.33
    return monthly


def process_annually(monthly):
    annually = monthly * 12
    return annually


def main():
    hours = get_hours()
    rate = get_rate()
    weekly = process_weekly(hours)
    monthly = process_monthly(weekly)
    annually = process_annually(monthly)


main()
