def activity_selection(activities):
    selected_activities = []
    activities.sort(key=lambda x: x[2])  # Sort activities by finish time
    selected_activities.append(activities[0])  # Select the first activity
    previous_finish_time = activities[0][2]  # Finish time of the first activity
    
    for activity in activities[1:]:
        start_time = activity[1]
        if start_time >= previous_finish_time:
            selected_activities.append(activity)
            previous_finish_time = activity[2]

    return selected_activities

all_activities = []
while True:
    start_time = int(input("\nEnter the start time of the activity: "))
    finish_time = int(input("Enter the finish time of the activity: "))
    all_activities.append([len(all_activities) + 1, start_time, finish_time])
    choice = input("\nDo you want to add another activity? (y/n): ").strip().lower()
    if choice != 'y':
        break

result = activity_selection(all_activities)

print("\nMaximum number of activities that can be performed: ", len(result))
print("\nActivities that can be selected are as follows: ")
print("Activity Number\tStart-Time\tEnd-Time")
for activity in result:
    print(f"{activity[0]}\t\t{activity[1]}\t\t{activity[2]}")