class Student:
    total_students = 0
    programs = {'CSE': {}, 'ECE': {}}

    def __init__(self, name, roll_number, batch, program, academic_year):
        self.name = name
        self.roll_number = roll_number
        self.batch = batch
        self.program = program
        self.academic_year = academic_year
        Student.total_students += 1

    @staticmethod
    def reclaim_roll_number(roll_number):
        if not roll_number.startswith('20'):
            return None
        parts = roll_number.split('-')
        if len(parts) != 5:
            return None
        if parts[1] != 'miit' or parts[3] not in ['cse', 'ece']:
            return None
        return roll_number

    def get_info(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Batch: {self.batch}, Program: {self.program}, Academic Year: {self.academic_year}"

    @classmethod
    def count_students(cls):
        print(f"Total number of students: {cls.total_students}")

    @classmethod
    def count_students_by_program(cls):
        for program, batches in cls.programs.items():
            total_students = sum(len(batch) for batch in batches.values())
            print(f"Total number of students in {program}: {total_students}")

    @classmethod
    def print_students_info(cls):
        for program, batches in cls.programs.items():
            for batch, students in batches.items():
                print(f"Students in {batch} batch of {program}:")
                for student in students:
                    print(student.get_info())
                print()


if __name__ == "__main__":
    # Creating student instances for 2015 batch
    for i in range(1, 61):
        roll_number = Student.reclaim_roll_number(f"2015-miit-cse-{str(i).zfill(3)}")
        student = Student(f"Student_{i}", roll_number, '2015', 'CSE', '2015')
        Student.programs['CSE'].setdefault('2015', []).append(student)

    for i in range(1, 56):
        roll_number = Student.reclaim_roll_number(f"2015-miit-ece-{str(i).zfill(3)}")
        student = Student(f"Student_{i}", roll_number, '2015', 'ECE', '2015')
        Student.programs['ECE'].setdefault('2015', []).append(student)

    # Creating student instances for 2016 batch
    for i in range(1, 56):
        roll_number = Student.reclaim_roll_number(f"2016-miit-cse-{str(i).zfill(3)}")
        student = Student(f"Student_{i}", roll_number, '2016', 'CSE', '2016')
        Student.programs['CSE'].setdefault('2016', []).append(student)

    for i in range(1, 57):
        roll_number = Student.reclaim_roll_number(f"2016-miit-ece-{str(i).zfill(3)}")
        student = Student(f"Student_{i}", roll_number, '2016', 'ECE', '2016')
        Student.programs['ECE'].setdefault('2016', []).append(student)

    Student.count_students()
    Student.count_students_by_program()
    Student.print_students_info()
