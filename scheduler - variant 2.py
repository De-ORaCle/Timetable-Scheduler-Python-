# Course Definitions
courses = {
    100: {
        "anthropology_and_archaeology": ["ARC 122"],
        "physics": ["PHY 101", "PHY 104", "PHY 105", "PHY 118"],
        "mathematics": ["MAT 141", "MAT 142"],
        "statistics": ["STA 121", "STA 131"],
        "chemistry": ["CHE 103", "CHE 127/126", "CHE 176/177", "CHE 191"],
        "geography": ["GEO 141"],
        "computer_science": ["CSC 103"],
        "zoology": ["ZOO 112", "ZOO 115", "ZOO 117", "ZOO 118"],
        "microbiology": ["MIC 121"],
        "geology": ["GEY 103"],
        "botany": ["BOT 141"],
        # Add other departments for the 100 level courses
    },
    200: {
        "anthropology_and_archaeology": ["ARC 222", "ANT 226", "ANT 228", "ANT 225"],
        "physics": ["PHY 205", "PHY 272", "PHY 298", "PHY 299"],
        "mathematics": ["MAT 212", "MAT 222", "MAT 223", "MAT 233", "MAT 253"],
        "statistics": ["STA 221", "STA 231"],
        "chemistry": ["CHE 218", "CHE 226", "CHE 251", "CHE 259", "CHE 276"],
        "geography": ["GEO 201", "GEO 202", "GEO 211", "GEO 231", "GEO 271", "GEO 281"],
        "computer_science": ["CSC 221", "CSC 222", "CSC 233/236", "CSC 234", "CSC 241", "CSC 272", "CSC 293"],
        "zoology": ["ZOO 212", "ZOO 215", "ZOO 216"],
        "biochemistry": ["BIO 212"],
        "microbiology": ["MIC 221", "MIC 222", "MIC 299"],
        "geology": ["GEY 234", "GEY 247", "GEY 286", "GEY 298"],
        "industrial_che": ["ICH 247", "ICH 267"],
        "botany": ["BOT 241", "BOT 242"]
        # Add courses for the 200 level
    },
    300: {
        "anthropology_and_archaeology": ["ARC 321", "ARC 322", "ARC 323", "ANT 328", "ANT 362"],
        "physics": ["PHY 305", "PHY 308", "PHY 312", "PHY 313", "PHY 316", "PHY 399"],
        "mathematics": ["MAT 322", "MAT 323", "MAT 331", "MAT 342"],
        "statistics": ["STA 322", "STA 323", "STA 325", "STA 331", "STA 333", "STA 334"],
        "chemistry": ["CHE 326", "CHE 328", "CHE 356"],
        "geography": ["GEO 302", "GEO 313", "GEO 314", "GEO 331", "GEO 332", "GEO 350", "GEO 383"],
        "computer_science": ["CSC 301"],
        "zoology": ["ZOO 311", "ZOO 315", "ZOO 319", "ZOO 320", "ZOO 322", "ZOO 323"],
        "biochemistry": ["BIO 212"],
        "microbiology": ["MIC 322", "MIC 325", "MIC 326", "MIC 327", "MIC 328"],
        "geology": ["GEY 306", "GEY 308", "GEY 357", "GEY 358", "GEY 361", "GEY 375", "GEY 377", "GEY 399"],
        "industrial_che": ["ICH 349", "ICH 366", "ICH 387"],
        "botany": ["BOT 342", "BOT 344", "BOT 351", "BOT 361"]
    },
    400: {
        "anthropology_and_archaeology": ["ARC 421", "ARC 422", "ARC 429", "ANT 428"],
        "physics": ["PHY 408", "PHY 482", "PHY 483", "PHY 485", "PHY 486", "PHY 488", "PHY 488", "SEMINAR"],
        "mathematics": ["MAT 407", "MAT 411", "MAT 416", "MAT 417", "MAT 418"],
        "statistics": ["STA 414", "STA 422", "STA 423", "STA 424", "STA 443", "STA 459", "STA 461"],
        "chemistry": ["CHE 416", "CHE 425", "CHE 428", "CHE 429", "CHE 451", "CHE 452", "CHE 473", "CHE 475", "CHE 476",
                      "CHE 478", "SEMINAR"],
        "geography": ["GEO 412", "GEO 421", "GEO 424", "GEO 431", "GEO 435", "GEO 436", "GEO 413"],
        "computer_science": ["CSC 411", "CSC 422", "CSC 433", "CSC 492"],
        "zoology": ["ZOO 411", "ZOO 412", "ZOO 413", "ZOO 414", "ZOO 416", "ZOO 417", "ZOO 421", "ZOO 422", "ZOO 424"],
        "biochemistry": ["BIO 411", "BIO 413", "BIO 414", "BIO 415"],
        "microbiology": ["MIC 404", "MIC 423", "MIC 424", "MIC 430"],
        "geology": ["GEY 463", "GEY 472", "GEY 476", "GEY 484", "GEY 486", "GEY 488", "GEY 437"],
        "industrial_che": ["ICH 447", "ICH 467", "ICH 481", "ICH 487"],
        "botany": ["BOT 413", "BOT 415", "BOT 417", "BOT 451", "BOT 462"]
    }
    # Add courses for the other levels
}

# Special courses with conflicts (arranged by levels)
special_conflict_courses = {
    100: {
        "chemistry": ["CHE 127", "CHE 176", ],
        "physics": ["PHY 101"],
        "zoology": ["ZOO 115"],
        "microbiology": ["MIC 121"],
        # Add other departments for the 100 level conflicts
    },
    200: {
        "biochemistry": ["BIO 212", "BIO 212"],
        "chemistry": ["CHE 259"],
        # Add other departments for the 200 level conflicts
    },
    300: {
        "mathematics": ["MAT 353"],
        # Add departments and conflict courses for the 300 level
    },
    400: {
        "biochemistry": ["BIO 413", "BIO 411", "BIO 414"],
        "botany": ["BOT 415"],
        # Add departments and conflict courses for the 400 level
    }
}

# Define the timetable schedule
schedule = {
    "Monday": {},
    "Tuesday": {},
    "Wednesday": {},
    "Thursday": {},
    "Friday": {}
}

import random
from tabulate import tabulate

# Define the function to check for course conflicts
def has_course_conflict(day, start_time, end_time, department):
    for time in range(start_time, end_time, 2):  # Adjusting the time range to 2-hour slots
        if time in schedule[day]:
            for existing_course in schedule[day][time]:
                if existing_course.startswith(department):
                    return True
    return False

# Define the function to assign a course to a time slot
def assign_course(day, start_time, end_time, course):
    for time in range(start_time, end_time, 2):  # Adjusting the time range to 2-hour slots
        if time not in schedule[day]:
            schedule[day][time] = []
        schedule[day][time].append(course)

# Create the timetable schedule with 2-hour specific slots from 8 am to 6 pm
schedule = {}
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    schedule[day] = {time: [] for time in range(8, 18, 2)}

# Assign the courses for each level and department
for level, courses_by_department in courses.items():
    for department, department_courses in courses_by_department.items():
        for course in department_courses:
            assigned = False
            while not assigned:
                day = random.choice(list(schedule.keys()))
                start_time = random.randint(0, 5) * 2 + 8  # Random start time from 8 am to 4 pm in 2-hour slots
                end_time = start_time + 2  # Each course gets 2 hours per day
                if end_time <= 18 and not has_course_conflict(day, start_time, end_time, department):
                    assign_course(day, start_time, end_time, course)
                    assigned = True

# Assign the conflict courses based on levels
for level, conflict_courses_by_department in special_conflict_courses.items():
    for department, conflict_courses in conflict_courses_by_department.items():
        for conflict_course in conflict_courses:
            assigned = False
            while not assigned:
                day = random.choice(list(schedule.keys()))
                start_time = random.randint(0, 5) * 2 + 8  # Random start time from 8 am to 4 pm in 2-hour slots
                end_time = start_time + 2  # Each course gets 2 hours per day
                if end_time <= 18 and not has_course_conflict(day, start_time, end_time, department):
                    assign_course(day, start_time, end_time, conflict_course)
                    assigned = True

# Create a table to display the schedule
table = []
for day, timetable in schedule.items():
    table.append([day])
    for time, courses in sorted(timetable.items()):
        course_list = "\n".join(courses)
        table.append([f"{time}:00 - {time+2}:00", course_list])
    table.append([])

# Print the timetable schedule
print(tabulate(table, headers=["Day", "Time Slot", "Course"], tablefmt="grid"))
