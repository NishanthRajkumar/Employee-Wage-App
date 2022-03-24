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
                computes daily wage for full day work
            Return:
                returns the daily wage
        """
        is_full_time = random.choice([True, False])
        if is_full_time:
            return 20*8
        return 20*4