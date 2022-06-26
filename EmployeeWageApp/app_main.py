'''
    @Author: Nishanth
    @Date: 24-03-2022 14:52:00
    @Last Modified by: Nishanth
    @Last Modified time: 24-03-2022 20:13:00
    @Title: Entry point of the project
'''
import sys
from wage_computation import EmployeeWageComputation
import logging

file_path = "C:\\Users\\Nishanth\\Desktop\\codingclub\\CFP\\Repos\\Employee-Wage-App\\EmployeeWageApp\\Log files\\Wage.log"

logging.basicConfig(handlers=[logging.FileHandler(file_path, mode="a"), logging.StreamHandler(sys.stdout)], level=logging.INFO)

employee1 = EmployeeWageComputation()

logging.info(f"Monthly Wage: {employee1.wage_condition()}")
logging.info(f"Total hours worked: {employee1.get_work_hours()}")
logging.info(f"Total days worked: {employee1.total_days_worked}")
for wage in employee1.wage_log:
    logging.info(f"Wage info(total_wage, (day, daily_wage)): {wage}")