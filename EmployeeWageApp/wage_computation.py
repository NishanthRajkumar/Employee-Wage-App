'''
    @Author: Nishanth
    @Date: 24-03-2022 14:52:00
    @Last Modified by: Nishanth
    @Last Modified time: 24-03-2022 20:20:00
    @Title: To compute employee wage as given in the use cases
'''
import random

class EmployeeWageComputation:

    def __init__(self):
        self.total_days_worked = 0
        self.total_hours_worked = 0
        self.wage_log = []
    
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
        total_hours = hours_per_day(random.choice([1, 2]))
        return (total_hours*wage_per_hour, total_hours)
    
    def monthly_wage(self):
        """
            Description:
                Computes monthly wage assuming no of working days per month as 20.
            Return:
                returns the monthly wage and the list of daily wages
        """
        total_wage = 0
        daily_wage_list = []
        for i in range(0,20):
            if self.attendance():
                daily_wage, hours_worked = self.daily_wage()
                total_wage += daily_wage
                daily_wage_list.append((f"Day {i}", daily_wage))
                self.total_days_worked += 1
                self.total_hours_worked += hours_worked
        return (total_wage, daily_wage_list)
    
    def wage_condition(self):
        """
            Description:
                Repeatedly computes monthly wage until 
                either total hours worked is 100 or total days worked is 20
            Return:
                returns monthly wage that meets the condition
        """
        total_wage = 0
        while (self.total_days_worked < 20 and self.get_work_hours() < 100):
            self.reset()
            total_wage, daily_wage_list = self.monthly_wage()
        else:
            self.wage_log.append((total_wage, daily_wage_list))
            return total_wage
    
    def get_work_hours(self):
        """
            Description:
                returns the total hours worked by the employee at the time of calling this method
            Return:
                returns total hours worked
        """
        return self.total_hours_worked