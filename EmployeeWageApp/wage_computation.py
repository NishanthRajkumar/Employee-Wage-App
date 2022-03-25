'''
    @Author: Nishanth
    @Date: 24-03-2022 14:52:00
    @Last Modified by: Nishanth
    @Last Modified time: 24-03-2022 19:27:00
    @Title: To compute employee wage as given in the use cases
'''
import random

class EmployeeWageComputation:

    def attendance(self):
        """
            Description:
                checks if employee is absent or present.
                Uses random to get attendance of employee
            Return:
                true if present, false if absent
        """
        return random.choice([True, False])
    
    def daily_wage(self):
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
        total_hours = 0
        try:
            total_hours = hours_per_day(random.choice([1, 2]))
            if total_hours == 0:
                raise Exception("Invalid hours per day recieved from switch-case")
        except Exception as e:
            print("Exception message: ", e)
        return total_hours*wage_per_hour
    
    def monthly_wage(self):
        """
            Description:
                Computes monthly wage assuming no of working days per month as 20.
            Return:
                returns the monthly wage
        """
        total_wage = 0
        for _ in range(0,20):
            if self.attendance():
                total_wage += self.daily_wage()
        return total_wage