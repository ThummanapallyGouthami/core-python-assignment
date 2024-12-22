def average(marks):
   return sum(marks) / len(marks)

def average_marks(students):
   return {name: average(marks) for name, marks in students.items()}

def top_performer(average_marks):
   return max(average_marks, key=average_marks.get)
students = {
   "John": [85, 78, 92],
   "Alice": [88, 79, 95],
   "Bob": [70, 75, 80]
}
average_marks1 = average_marks(students)
top_performer1 = top_performer(average_marks1)
print(f"Average Marks: {average_marks1}")
print(f"Top Performer: \"{top_performer1}\"")