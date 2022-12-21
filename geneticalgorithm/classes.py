from explorecourses.classes import Course
from explorecourses import CourseConnection

import geneticalgorithm.utils

# DEBUGGING
connect = CourseConnection()



class Agenda:
    def __init__(self, num_years: int):
        """
        Optimize the GA agenda!
        """
        self.years = [Year() for _ in range(num_years)]


    def display(self):
        for i, year in enumerate(self.years):
            print(f"YEAR {i}:")
            year.display(offset="\t")

    def satisfies_ways(self):
        pass


    def satisfies_math(self):
        pass


class Year:
    def __init__(self):
        self.fall = Quarter()
        self.winter = Quarter()
        self.spring = Quarter()
        self.summer = Quarter()
        self.quarters = [self.fall, self.winter, self.spring, self.summer]

    def display(self, offset=""):
        print(f"{offset}FALL:", end=" ")
        self.fall.display()
        print(f"{offset}WINTER:", end=" ")
        self.winter.display()
        print(f"{offset}SPRING:", end=" ")
        self.spring.display()
        print(f"{offset}SUMMER:", end=" ")
        self.summer.display()


class Quarter:
    def __init__(self):
        self.courses = []

    def enroll(self, course: Course):
        """
        >>> fall = Quarter()
        >>> econ202 = utils.get_course("econ202")
        >>> fall.enroll(econ202)
        >>> [course.title for course in fall.courses]
        ['Microeconomics I']
        """
        self.courses.append(course)

    def total_units(self) -> (int, int):
        """
        >>> fall = Quarter()
        >>> econ202 = utils.get_course("econ202")
        >>> fall.enroll(econ202)
        >>> fall.total_units()
        (2, 5)
        """
        min_units = 0
        max_units = 0
        for course in self.courses:
            min_units += course.units_min
            max_units += course.units_max
        return min_units, max_units

    def display(self):
        print([course.title for course in self.courses])

    def feasible(self):
        pass
        # TODO
        # time conflicts
        # every course is active
