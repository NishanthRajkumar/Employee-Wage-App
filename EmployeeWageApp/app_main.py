'''
    @Author: Nishanth
    @Date: 24-03-2022 14:52:00
    @Last Modified by: Nishanth
    @Last Modified time: 24-03-2022 19:54:00
    @Title: Entry point of the project
'''
from wage_computation import EmployeeWageComputation

employee1 = EmployeeWageComputation()

print("Monthly Wage: ", employee1.wage_condition())
print("Total hours worked: ", employee1.total_hours_worked)
print("Total days worked: ", employee1.total_days_worked)