def total_steps(steps):
    return sum(steps)
def average_steps(steps):
    return sum(steps) // len(steps)
def highest_steps(steps):
    return max(steps)
def lowest_steps(steps):
    return min(steps)
def goal_met(steps):
    results = []
    for s in steps:
        results.append(s >= 10000)
    return results

steps_input = input().split()
steps = []
for s in steps_input:
    steps.append(int(s))

total=total_steps(steps)
avg = average_steps (steps)
highest = highest_steps(steps)
lowest = lowest_steps(steps)
goals = goal_met(steps)

print("Total stpes:", total)
print("Average daily steps:", avg)
print("Highest steps in a day:", lowest)
print("Lowest steps in a day:", lowest)
print("Goal met each day:", goals)