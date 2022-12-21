"""
Simplifying Assumptions:
* no SLE
* no language experience

Complications:
* math classes satisfy WAY_FR, so we don't need extra WAY_FR classes; but we don't
need optimality in the initial generation, just feasibility so this consideration may be unimportant


Prerequisite Orderings [medium]
Proper Quarter [easy]
Time conflicts [hard]
Two STEM classes per quarter [potentially hard]
WAYS courses [problem is that I don't have preferences over ways courses]
"""
from explorecourses.filters import *

# UG Requirements
WAY_EDP = "filter-ger-WAYEDP"  # NOTE: Engaging Diversity (ED) was changed to Exploring Difference and Power (EDP) in 2022-2023
# TODO: ED was changed to EDP so you have to change the tag later
WAYS = [WAY_AII, WAY_SI, WAY_SMA] * 2 + [WAY_AQR, WAY_CE, WAY_ER, WAY_FR]
WRITING = [WRITING1, WRITING2]
# TODO: language
# TODO: PWR

MATH_INTRO = ["MATH 51", "MATH 52", "MATH 53"]
MATH_ADV = ["MATH"] * 8 + ["ELECTIVE"] * 4  # 8 adv. math classes + 4 pre-approved electives
