print("STEP COUNTER")
daily_goal=int(input("What is your daily step goal? "))
completed_as_of_now=int(input("How many steps have you taken today? "))
remaining=daily_goal-completed_as_of_now
if remaining>0:
    print(f"You need {remaining} more steps to reach your goal!")
else:
    print(f"Congratulations! You have exceeded your goal by {-remaining} steps")
