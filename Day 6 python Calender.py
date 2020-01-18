import calendar

#take input from user
year,month=input('Enter year and Month: ').split()
print(calendar.month(int(year),int(month)))