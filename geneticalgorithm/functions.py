import itertools

from explorecourses import CourseConnection, Course
connect = CourseConnection()

from geneticalgorithm.classes import Agenda


def pick_math_classes(n: int, prerequisite_graph) -> list[Course]:
    """
    Given the prerequisite graph of the math department, pick n math classes so that
    no class has an unsatisfied prerequisite. Return the n math classes in some topological
    ordering.
    """
    # TODO: hook up
    # TODO: given the prerequisite graph of the math department, pick

def generate():
    # pick 8 random math classes; topologically sort them
    pass


def generate_random_feasible_schedule() -> Agenda:
    """
    >>> schedule = generate_random_feasible_schedule()
    >>> schedule.display()
    """
    schedule = Agenda(num_years=4)
    return schedule
