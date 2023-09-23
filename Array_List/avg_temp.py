"""
Calculate the average temp
"""

temps = []

total_days = int(input("How many days temperature? "))

for day in range(1, total_days+1):
	temp = int(input(f"Enter day {day}'s temp: "))
	temps.append(temp)

average_temp = sum(temps)/total_days

print(f"Average = {average_temp}")

count = 0
for temp in temps:
	if temp > average_temp:
		count += 1

print(f"{count} day(s) above average")