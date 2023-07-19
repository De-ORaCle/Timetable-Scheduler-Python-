import random
from tabulate import tabulate

generalCourses = {
    'mathematics': {
        '100L': {
            'MAT101': 4,
            'MAT111': 4
        },
        '200L': {
            'MAT242': 4,
            'MAT251': 4
        },
        '300L': {
            'MAT342': 4,
            'MAT351': 4
        },
        '400L': {
            'MAT442': 4,
            'MAT451': 4
        }
    },
    'physics': {
        '100L': {
            'PHY103': 3,
            'PHY104': 3
        },
        '200L': {
            'PHY203': 3,
            'PHY204': 3
        }
    }
}

otherCourses = {
    'mathematics': {
        '100L': {
            'MAT121': 4,
            'MAT142': 4
        },
        '200L': {
            'MAT222': 4,
            'MAT221': 4
        },
        '300L': {
            'MAT322': 4,
            'MAT321': 4
        },
        '400L': {
            'MAT422': 4,
            'MAT421': 4
        }
    },
    'physics': {
        '100L': {
            'PHY105': 3,
            'PHY102': 3
        },
        '200L': {
            'PHY222': 3,
            'PHY221': 3
        },
        '300L': {
            'PHY322': 3,
            'PHY321': 3
        },
        '400L': {
            'PHY422': 3,
            'PHY421': 3
        }
    }
}

# Define the time slots and days of the week
time_slots = ['8:00am - 10:00am', '10:00am - 12:00pm', '12:00pm - 2:00pm', '2:00pm - 4:00pm', '4:00pm - 6:00pm', '6:00pm - 8:00pm']
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Define the function to assign courses to time slots
def assign_courses_to_slots(courses, level):
    timetable = {day: {slot: [] for slot in time_slots} for day in days_of_week}
    assigned_slots = set()
    
    for department, levels in courses.items():
        if level in levels:
            courses_level = levels[level]
            for course, units in courses_level.items():
                course_hours = units // 2
                available_slots = list(set(time_slots) - assigned_slots)
                random.shuffle(available_slots)
                assigned_days = random.sample(days_of_week, course_hours)
                
                for i in range(course_hours):
                    day = assigned_days[i]
                    slot = available_slots[i]
                    timetable[day][slot].append(course)
                    assigned_slots.add(slot)
    
    return timetable

# Assign courses for each level and department
all_timetables = []
for level in ['100L', '200L', '300L', '400L']:
    general_timetable = assign_courses_to_slots(generalCourses, level)
    other_timetable = assign_courses_to_slots(otherCourses, level)
    all_timetables.append({**general_timetable, **other_timetable})

# Sort the timetables by day and time
sorted_timetables = []
for timetable in all_timetables:
    sorted_timetable = {day: {slot: sorted(courses) for slot, courses in slots.items()} for day, slots in timetable.items()}
    sorted_timetables.append(sorted_timetable)

# Create the table headers
headers = ['Day', 'Time Slot', 'Courses']

# Initialize the table data
table_data = []

# Populate the table data
for day in days_of_week:
    for slot in time_slots:
        courses = []
        for timetable in sorted_timetables:
            courses.extend(timetable[day][slot])
        if courses:
            table_data.append([day, slot, ', '.join(courses)])

# Generate the table
table = tabulate(table_data, headers=headers, tablefmt='grid')

# Print the timetable table
print(table)
