from wage_computation import EmployeeWageComputation

if EmployeeWageComputation.attendance():
    print("Employee is present")
else:
    print("Employee is absent")

print("Daily Wage: ", EmployeeWageComputation.daily_wage())