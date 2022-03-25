from wage_computation import EmployeeWageComputation

if EmployeeWageComputation.attendance():
    print("Employee is present")
    print("Daily Wage: ", EmployeeWageComputation.daily_wage())
else:
    print("Employee is absent")