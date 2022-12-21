from explorecourses import CourseConnection
from explorecourses.classes import Course

from datetime import date
import re


CONNECT = CourseConnection()
TODAY = date.today()
CURRENT_SCHOOL_YEAR = f"{TODAY.year}-{TODAY.year + 1}"


def split_name(name: str) -> (str, str):
    """
    >>> split_name("Econ202")
    ('Econ', '202')
    >>> split_name("ECON 202")
    ('ECON', '202')
    >>> split_name("cs224n")
    ('cs', '224n')
    """
    subject = get_subject(name)
    code = get_code(name)
    return subject, code


def get_code(name: str) -> str:
    """
    >>> get_code("MATH19")
    '19'
    >>> get_code("cs224n")
    '224n'
    """
    m = re.search(r"\d", name)
    return name[m.start():].strip() if m else ""


def get_subject(name: str) -> str:
    """
    >>> get_subject("MATH19")
    'MATH'
    >>> get_subject("MATH19-21")
    'MATH'
    >>> get_subject("MATH 19")
    'MATH'
    """
    m = re.search(r"\d", name)
    return name[:m.start()].strip() if m else ""

def get_names(course: Course) -> set[str]:
    """
    >>> cs224n = get_course("cs224n")
    >>> list(sorted(get_names(cs224n)))
    ['CS 224N', 'LINGUIST 284', 'SYMSYS 195N']
    >>> cs181w = get_course("cs181w")
    >>> list(sorted(get_names(cs181w)))
    ['CS 181W']
    """
    names = set()
    # get primary name (i.e., subject + code)
    primary_name = f"{course.subject} {course.code}".upper()
    names.add(primary_name)

    # get aliases
    m = re.search(r"\((.*?)\)", course.title)
    if m:
        for g in m.groups():
            if g.isalpha():  # NOTE: handles courses like 'CS 181W: Computers, Ethics, and Public Policy (WIM)'
                continue
            for alias in g.split(","):
                names.add(format_name(alias))
    return names


def format_name(name: str) -> str:
    """
    >>> format_name("econ 202")
    'ECON 202'
    >>> format_name("econ202")
    'ECON 202'
    >>> format_name("cs224n")
    'CS 224N'
    """
    name = name.upper()
    subject, code = split_name(name)
    return f"{subject} {code}"


def get_course(name: str, year=CURRENT_SCHOOL_YEAR) -> Course:
    """
    >>> get_course("econ 202").title
    'Microeconomics I'
    >>> get_course("cs224n").title
    'Natural Language Processing with Deep Learning (LINGUIST 284, SYMSYS 195N)'
    >>> get_course("linguist284").title
    'Natural Language Processing with Deep Learning (CS 224N, SYMSYS 195N)'
    """
    name = format_name(name)
    courses = CONNECT.get_courses_by_query(name, year)
    for course in courses:
        if name in get_names(course):
            return course
    return None


def courses_conflict(course1: Course, course2: Course) -> bool:
    # TODO: do this w/ greedy algorithm similar to CS 161
    return False
