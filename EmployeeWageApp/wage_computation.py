'''
    @Author: Nishanth
    @Date: 24-03-2022 14:52:00
    @Last Modified by: Nishanth
    @Last Modified time: 24-03-2022 19:54:00
    @Title: To compute employee wage as given in the use cases
'''
import random

class EmployeeWageComputation:

    def __init__(self):
        self.total_days_worked = 0
        self.total_hours_worked = 0
    
    def reset(self):
        """
            Description:
                Resets the total days and hours worked to 0
        """
        self.total_days_worked = 0
        self.total_hours_worked = 0

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
                returns the daily wage and hours worked that day
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
        return (total_hours*wage_per_hour, total_hours)
    
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
                daily_wage, hours_worked = self.daily_wage()
                total_wage += daily_wage
                self.total_days_worked += 1
                self.total_hours_worked += hours_worked
        return total_wage
    
    def wage_condition(self):
        """
            Description:
                Repeatedly computes monthly wage until 
                either total hours worked is 100 or total days worked is 20
            Return:
                returns monthly wage that meets the condition
        """
        total_wage = 0
        while (self.total_days_worked < 20 and self.total_hours_worked < 100):
            self.reset()
            total_wage = self.monthly_wage()
        else:
            return total_wage