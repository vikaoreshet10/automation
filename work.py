year = 365
days_of_the_week = 7
week = year / days_of_the_week
print(week)

print(24 * days_of_the_week * week)
total_hours = 24 * days_of_the_week * week

hours = int(input())
hours_of_year = hours * days_of_the_week * week

print(hours_of_year)

print(hours_of_year / total_hours)
