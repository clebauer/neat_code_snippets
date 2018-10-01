# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell> {}

import pandas as pd

# <codecell> {}

def how_many_hours(num_weeks, dedicated_weekly_hours):
    return num_weeks * dedicated_weekly_hours

# <markdowncell> {}

# ### 3 months is roughly 13 weeks, thank you Google.
# ### 4 weeks is... 4 weeks, duh.

# <codecell> {}

expected_weekly_hours = 10 # 2 per weekday

class1_hours_needed = how_many_hours(13, expected_weekly_hours)
class2_hours_needed = how_many_hours(4, expected_weekly_hours)

# <markdowncell> {}

# ### So class1 requires 130 hours to complete and class2 requires 40 hours to complete.

# <codecell> {}

class1_hours_needed, class2_hours_needed

# <markdowncell> {}

# ### I've created a dataframe that holds these total hours until completion so I can...

# <codecell> {}

hour_tracker = pd.DataFrame(data=[class1_hours_needed, class2_hours_needed], 
                            columns=['total_hours'],
                            index=['class1','class2'])

# <markdowncell> {}

# ### show y'all how many weeks each class will take if you contribute 1 to 7 hours per day (5 days a week)

# <codecell> {}

days_per_week = 5
for x in range(1,7):
    # recreate the column name each time
    col_name = 'weeks_at_{}hpd'.format(x)
    
    # divide the total_hours by the days_per week set above and by our x (number of hours committed.)
    # this could also be written as hour_tracker['total_hours]/(days_per_week*x), thank you algebra.
    hour_tracker[col_name] = hour_tracker['total_hours']/days_per_week/x
    
# purely aesthetic, this is just more readable
hour_tracker = hour_tracker.T.astype(int)

# <markdowncell> {}

# # Assuming 5 days a week
# #### Let hpd mean hours per day

# <codecell> {}

hour_tracker

# <markdowncell> {}

# # Let's make this into a function

# <codecell> {}

# We input udacity's 'timeline' weeks (if months, multiply by 4 or use unit='months'),
# the number of days per week we can commit to,
# and the number of hours per day we can commit to...
# Out pops how many weeks it will take to complete!
def how_many_weeks_needed(udacity_time, udacity_unit, days_per_week, hours_per_day):
    # If we put in months, make it weeks
    if udacity_unit == 'months':
        udacity_weeks = udacity_time * 4
        
    # Since each class is expecting 5 days a week, 2 hours a day: 
    total_class_hours = udacity_weeks * 10
    
    # We calculate how many hours a week we can contribute:
    hours_per_week = hours_per_day * days_per_week
    
    # We divide the total by how many hours per week we're committing:
    how_many_weeks = total_class_hours / hours_per_week
    
    return how_many_weeks

# <markdowncell> {}

# ### For class 1, which expects 3 months of time...
# #### At 4 days per week with 2 hours_per_day:

# <codecell> {}

how_many_weeks_needed(udacity_time = 3, 
                      udacity_unit = 'months',
                     days_per_week = 4, 
                     hours_per_day = 2)

# <codecell> {}



# <metadatacell>

{"kernelspec": {"display_name": "Python 2", "name": "python2", "language": "python"}}