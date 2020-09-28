# This program will determan the users age in months days hours and seconds.


def display_results(month, day, hour, second):
  print("your age in months is: " + str(month))
  print("your age in days is: " + str(day))
  print("your age in hours is: " + str(hour))
  print("your age in seconds is: " + str(second))


def get_age():
  print("How old are you? ")
  age = int(input())
  return age


def process_month(age):
  month = age * 12
  return month


def process_day(age):
  day = age * 365
  return day


def process_hour(day):
  hour = day * 24
  return hour


def process_second(hour):
  second = hour * 60 * 60
  return second


def main():
  age = get_age()
  month = process_month(age)
  day = process_day(age)
  hour = process_hour(day)
  second =process_second(hour)
  display_results(month, day, hour, second)
  


main() 
