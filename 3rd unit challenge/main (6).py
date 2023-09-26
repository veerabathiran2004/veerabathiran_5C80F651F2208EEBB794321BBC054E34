class student:
  def __init__(self, name, roll_number, cgpa):
   self.name = name 
   self.roll_number = roll_number
   self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                          key=lambda student: student.cgpa,
                          reverse=True)
  return sorted_students



students = [
  student("kumar", "A123", 99.9),
  student("raaju", "A124", 56.4),
  student("ravi", "A125", 86.6),
  student("choota bheem", "A126", 98.6),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("NAME: {}, Roll Number: {}, cgpa: {}".format(student.name, student.roll_number, student.cgpa))