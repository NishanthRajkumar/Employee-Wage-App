'''
    @Author: Nishanth
    @Date: 24-03-2022 14:52:00
    @Title: To compute employee wage as given in the use cases
'''
import random

class EmployeeWageComputation:

    def attendance():
        """
            Description:
                checks if employee is absent or present.
                Uses random to get attendance of employee
            Return:
                true if present, false if absent
        """
        return random.choice([True, False])
    
    def daily_wage():
        """
            Description:
                Computes daily wage for total hours worked.
                Total hours depends on if employee is part-time or full-time.
                Part-time/Full-time is decided using random module
            Return:
                returns the daily wage
        """
        wage_per_hour = 20
        total_hours_case = {
            True: 8,
            False: 4
        }
        total_hours = total_hours_case[random.choice([True, False])]
        return total_hours*wage_per_hour