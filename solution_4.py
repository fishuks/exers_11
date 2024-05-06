import random

class Subject:
    '''
    The Subject class represents a subject in the schedule.

    Attributes:

    - name (str): The name of the subject.

    Methods:

    - __init__(self, name): Initializes a Subject object.
    - __str__(self): Returns the name of the subject.
    '''
    def __init__(self, name):
        '''
        Initializes a Subject object with a given name.

        Parameters:
        name (str): The name of the subject.
        '''
        self.name = name

    def __str__(self):
        '''
        Returns the name of the subject as a string.

        Returns:
        str: The name of the subject.
        '''
        return f'{self.name}'

class Lesson:
    '''
    The Lesson class represents a lesson in the schedule.

    Attributes:

    - subject (Subject): The subject of the lesson.
    - time (str): The time of the lesson.

    Methods:

    - __init__(self, subject, time): Initializes a Lesson object.
    - __str__(self): Returns a string representation of the lesson.
    '''
    def __init__(self, subject, time):
        '''
        Initializes a Lesson object with a subject and time.

        Parameters:
        subject (Subject): The subject of the lesson.
        time (str): The time of the lesson.
        '''
        self.subject = subject
        self.time = time

    def __str__(self):
        '''
        Returns a string representation of the lesson including time and subject.

        Returns:
        str: String representation of the lesson.
        '''
        return f"{self.time}: {self.subject}"

class Schedule:
    '''
    The Schedule class represents the schedule for a group.

    Attributes:

    - group_name (str): The name of the group.
    - days (dict): A dictionary with days of the week as keys and lists of lessons as values.

    Methods:

    - __init__(self, group_name): Initializes a Schedule object.
    - add_lesson(self, day, lesson): Adds a lesson to the schedule on a specific day.
    - print_schedule(self): Prints the schedule for the group.
    - __str__(self): Returns a string representation of the schedule.
    '''
    def __init__(self, group_name):
        '''
        Initializes a Schedule object for a specific group.

        Parameters:
        group_name (str): The name of the group.
        '''
        self.group_name = group_name
        self.days = {
            "Понедельник": [],
            "Вторник": [],
            "Среда": [],
            "Четверг": [],
            "Пятница": [],
            "Суббота": [],
        }

    def add_lesson(self, day, lesson):
        '''
        Adds a lesson to a specific day in the schedule.

        Parameters:
        day (str): The day of the week.
        lesson (Lesson): The lesson to add.
        '''
        if len(self.days[day]) < 5 and lesson.time not in [lesson.time for lesson in self.days[day]]:
            self.days[day].append(lesson)

    def print_schedule(self):
        '''
        Prints the schedule for the group with lessons for each day.
        '''
        print(f"Расписание группы {self.group_name}")
        for day, lessons in self.days.items():
            print(f"\n{day}:")
            if lessons:
                for lesson in lessons:
                    print(lesson)
            else:
                print("Выходной")

    def __str__(self):
        '''
        Returns a string representation of the schedule.

        Returns:
        str: String representation of the schedule.
        '''
        return f'{self.group_name} : {self.days}'

def read_subjects(filename):
    '''
    Reads subjects from a file and returns a list of Subject objects.

    Parameters:
    filename (str): The name of the file containing subjects.

    Returns:
    list: List of Subject objects.
    '''
    with open(filename, "r", encoding="utf-8") as file:

        return [Subject(line.strip()) for line in file]

def read_times(filename):
    '''
    Reads times from a file and returns a list of time strings.

    Parameters:
    filename (str): The name of the file containing times.

    Returns:
    list: List of time strings.
    '''
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]

def create_schedule(group_name, subjects_filename, times_filename):
    '''
    Creates a schedule for a group based on subjects and times provided in files.

    Parameters:
    group_name (str): The name of the group.
    subjects_filename (str): The filename containing subjects.
    times_filename (str): The filename containing times.

    Returns:
    Schedule: A Schedule object for the group.
    '''
    subjects = read_subjects(subjects_filename)
    times = read_times(times_filename)
    schedule = Schedule(group_name)
    random.shuffle(subjects)
    
    for subject in subjects:
    
        day = random.choice(list(schedule.days.keys()))
        time = random.choice(times)
        schedule.add_lesson(day, Lesson(subject, time))
    
    return schedule

