# Timetable Scheduler Documentation

## Overview
The "Timetable Scheduler" is a Python program that generates a random timetable schedule for university courses. It assigns courses to different time slots on weekdays (Monday to Friday) from 8 am to 6 pm, in 2-hour intervals. The scheduler takes into account course conflicts and special courses with conflicting time slots. The output is presented in a tabular format using the "tabulate" library.

## Course Definitions
The timetable scheduler starts with the definition of courses offered at different levels (100, 200, 300, 400) and departments. The courses are stored in a nested dictionary called `courses`. Each level has its own dictionary with department names as keys and corresponding courses as values.

## Special Courses with Conflicts
The scheduler also takes into account special courses that have conflicts with other courses. These courses are specified in the `special_conflict_courses` dictionary, arranged by levels. Each level has its own dictionary with department names as keys and the list of conflicting course codes as values.

## Functions
### `has_course_conflict`
This function checks if there is a conflict between a proposed course and the existing courses scheduled for a given day and time slot. It takes the parameters:
- `day`: The day of the week (e.g., "Monday").
- `start_time`: The starting time of the proposed course (24-hour format, e.g., 8 for 8 am).
- `end_time`: The ending time of the proposed course (24-hour format, e.g., 10 for 10 am).
- `department`: The department to which the course belongs (e.g., "chemistry").

### `assign_course`
This function assigns a course to a specific day and time slot in the schedule. It takes the parameters:
- `day`: The day of the week (e.g., "Monday").
- `start_time`: The starting time of the course (24-hour format, e.g., 8 for 8 am).
- `end_time`: The ending time of the course (24-hour format, e.g., 10 for 10 am).
- `course`: The code of the course to be assigned (e.g., "PHY 101").

## Schedule Generation
The timetable schedule is created using the following steps:

1. Initialize the `schedule` dictionary: A dictionary is created for each day of the week (Monday to Friday), and each day contains a nested dictionary with time slots as keys and empty lists as values. The time slots range from 8 am to 6 pm in 2-hour intervals.

2. Assign Regular Courses: For each level and department, the scheduler randomly selects a day, a start time (from 8 am to 4 pm), and an end time (2 hours later) for each course. It checks for conflicts using the `has_course_conflict` function and assigns the course to the schedule using the `assign_course` function if there are no conflicts.

3. Assign Special Conflict Courses: The scheduler also considers special courses with conflicts and assigns them in a similar manner as regular courses.

## Output
The timetable schedule is displayed in a tabular format using the "tabulate" library. The table includes columns for the time slot and each day of the week (Monday to Friday). The courses assigned to each time slot are displayed in the respective cells. If multiple courses are scheduled at the same time slot on the same day, they are listed vertically in the cell.

## Restrictions and Possible Improvements
- The current implementation does not account for class durations other than 2 hours. It assumes all courses take 2 hours per day.
- The scheduler assigns courses randomly without considering factors like student preferences, faculty availability, or room availability.
- It is possible for the scheduler to get stuck in an infinite loop if it cannot find a suitable time slot for a course due to conflicts. Implementing a mechanism to handle such cases would be beneficial.
- The "tabulate" library is used for display purposes, but the output could be further enhanced with additional formatting options and better readability.
- There may be performance issues when scheduling a large number of courses or when the number of time slots is limited.
- The scheduler is tailored to a specific dataset of courses and may need modification to adapt to different university course structures.

## Conclusion
The "Timetable Scheduler" is a basic program that generates a random timetable for university courses while considering course conflicts. It serves as a starting point for more sophisticated scheduling algorithms and can be further improved to cater to specific requirements and constraints of universities or educational institutions.
