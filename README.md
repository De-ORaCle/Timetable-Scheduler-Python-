# Timetable Scheduler Documentation

## Introduction

The "Timetable Scheduler" is a Python program designed to create a timetable schedule for courses offered at a university or educational institution. The program takes into account different course levels, departments, and special courses with potential scheduling conflicts. It aims to distribute the courses across weekdays and timeslots in a fair and conflict-free manner.

## Requirements

To run the "Timetable Scheduler" program, the following requirements must be met:

1. Python: The program is written in Python, so Python must be installed on the system.
2. `tabulate` library: The program uses the `tabulate` library to format and print the timetable table.

You can install the `tabulate` library using the following command:

```bash
pip install tabulate
```

## Course Definitions

The program starts by defining the available courses for different levels and departments. The courses are organized into three dictionaries:

1. `lower_unit_courses`: Contains courses for lower-level units (100, 200, 300, 400).
2. `higher_unit_courses`: Contains courses for higher-level units (100, 200, 300, 400).
3. `special_conflict_courses`: Contains courses that may have conflicts with other courses.

Each dictionary is organized by course level (100, 200, 300, 400), and for each level, courses are further grouped by department. Each department contains a list of courses offered.

## Timetable Schedule

The timetable schedule is represented as a nested dictionary called `schedule`, which stores course assignments for each weekday and time slot. The weekdays are represented as keys (e.g., "Monday", "Tuesday"), and each day maps to a dictionary containing time slots as keys (e.g., 8, 10) and lists of assigned courses as values.

The timetable schedule follows these conventions:

- Each course is assigned to a time slot of 2 hours.
- The time slots range from 8 am to 6 pm (8:00 - 18:00).
- Courses are assigned to the schedule using the `assign_course` and `assign_course_twice_a_week` functions, which ensure conflict-free scheduling.

## Functions

The program defines several functions to manage course assignments and scheduling:

1. `has_course_conflict`: This function checks if a given course in a department has a time slot conflict with other courses on a specific day.

2. `assign_course`: This function assigns a course to a specific day and time slot by adding it to the `schedule` dictionary.

3. `assign_course_twice_a_week`: This function is similar to `assign_course`, but it assigns a course to two different days during the week.

## Execution

1. The program creates an empty `schedule` dictionary with pre-defined time slots for each day of the week (from 8 am to 6 pm).

2. Lower-level courses (100, 200, 300, 400) are assigned to the schedule using a random selection of days and time slots, ensuring no conflicts.

3. Higher-level courses are assigned to the schedule twice a week, again avoiding conflicts.

4. Special conflict courses are assigned to the schedule for their respective levels, ensuring no conflicts.

5. The final timetable is formatted and printed using the `tabulate` library to display the course assignments for each day and time slot.

## Restrictions

1. The program assigns each course to a 2-hour time slot, and the time slots are fixed from 8 am to 6 pm. If your university's schedule has different time slot durations or a different range of hours, you will need to modify the program accordingly.

2. The program assumes that courses can be scheduled on weekdays only (Monday to Friday). If your institution has courses on weekends or other specific days, you will need to adjust the program to accommodate those days.

3. The program uses a random assignment strategy for lower-level courses. As a result, running the program multiple times may produce different timetables. If you prefer a deterministic approach or have specific requirements for course assignments, you should modify the assignment logic.

4. The program does not consider any prerequisites or course-specific constraints. It only focuses on avoiding conflicts between courses on the timetable.

5. The program may not handle all possible edge cases related to course assignments. Additional validation and testing may be necessary to ensure robustness for specific scenarios.

## Conclusion

The "Timetable Scheduler" is a basic Python program that generates a timetable schedule for courses offered at a university. It allows you to specify different course levels, departments, and special conflict courses. The program uses a random assignment approach to distribute the courses across weekdays and time slots while avoiding conflicts. However, due to its simplicity, it may require modifications to suit specific institutional requirements or constraints.
