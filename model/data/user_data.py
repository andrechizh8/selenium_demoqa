from dataclasses import dataclass
from typing import Literal
import random
from faker import Faker

faker = Faker()


@dataclass
class User:
    gender: Literal["Male", "Female", "Other"]
    subjects: Literal['Maths', 'Accounting', 'Arts', 'Social Studies', 'English', 'Chemistry', 'Physics',
    'Computer Science', 'Economics', 'History', 'Civics', 'Commerce', 'Biology', 'Hindi']
    hobby: Literal['Sports', 'Reading', 'Music']
    state: Literal['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
    city: Literal['Karnal', 'Panipat', 'Delhi', 'Gurgaon', 'Noida', 'Agra', 'Merrut', 'Lucknow', 'Jaipur', 'Jaiselmer']
    date: str = None
    first_name: str = None
    last_name: str = None
    phone: str = None
    picture: str = None
    email: str = None
    address: str = None
    like: str = None


user = User(gender=random.choice(["Male", "Female", "Other"]),
            subjects=random.choice(['Maths', 'Accounting', 'Arts', 'Social Studies', 'English', 'Chemistry', 'Physics',
                                    'Computer Science', 'Economics', 'History', 'Civics', 'Commerce', 'Biology',
                                    'Hindi']), hobby=random.choice(['Sports', 'Reading', 'Music']),
            state=random.choice(['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']), city=random.choice(
        ['Karnal', 'Panipat', 'Delhi', 'Gurgaon', 'Noida', 'Agra', 'Merrut', 'Lucknow', 'Jaipur', 'Jaiselmer']),
            date="08 Dec 1992",
            first_name=faker.first_name(), last_name=faker.last_name(), phone="9183346139", picture="resources/1.txt",
            email=faker.email(), address=faker.job(), like=random.choice(["Yes", "Impressive"]))
