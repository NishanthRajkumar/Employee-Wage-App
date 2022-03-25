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
        def hours_per_day(case):
            """
                Description:
                    Implements swtich case and retrieves the hours per day based on case argument
                Return:
                    returns hours per day
            """
            switch_case = {
                1: 8,
                2: 4
            }
            return switch_case.get(case, 0)
        wage_per_hour = 20
        total_hours = hours_per_day(random.choice([1, 2]))
        return total_hours*wage_per_hour