steps = input("Enter steps for 7 days separated by spaces: ")
steps_list = list(map(int, steps.split()))

def total_steps(data):
    return sum(data)

def average_steps(data):
    return sum(data) // len(data)

def max_steps(data):
    return max(data)

def min_steps(data):
    return min(data)

def goal_met(data):
    result = [ ]
    for day in data:
        if day >= 10000:
            result.append(True)
        else:
            result.append(False) 
    return result        


total=total_steps(steps_list)
average = average_steps (steps_list)
highest = max_steps(steps_list)
lowest = min_steps(steps_list)
goals = goal_met(steps_list)

print("Total stpes:", total)
print("Average daily steps:", average)
print("Highest steps in a day:", highest)
print("Lowest steps in a day:", lowest)
print("Goal met each day:", goals)