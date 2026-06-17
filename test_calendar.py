from agents.calendar import create_calendar
from agents.scheduler import build_schedule, save_schedule

result = create_calendar([])

schedule = build_schedule(result)

file = save_schedule(schedule)

print("\n🔥 WEEKLY CONTENT SCHEDULE CREATED 🔥\n")

i = 0
while i < len(schedule):

    item = schedule[i]

    print("DAY:", item["day"])
    print("IDEA:", item["post"]["idea"])
    print("FILE SAVED:", file)

    print("\n----------------------\n")

    i += 1