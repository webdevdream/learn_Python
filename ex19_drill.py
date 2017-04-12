# Get the required data from user
name = input("please enter the employee name: ")
basic = int(input("Basic Salary: "))
over_time_hours = int(input("Over time hours: "))
allow = int(input("Allowence: "))
bonus = int(input("Bonus: "))

def salary(name, basic, over_time_hours, allow, bonus):
    over_time_value = (basic / 240) * over_time_hours * 1.5
    total = basic + over_time_value + allow + bonus
    print ("\nOver time value: %d SR." % over_time_value)
    print ("%s Total Salary is: %d SR." % (name , total))

salary(name, basic, over_time_hours, allow, bonus)
