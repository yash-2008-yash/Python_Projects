#CGPA Calculator by Yashwanth

def marks_to_cgpa(marks):
    if 91 <= marks <= 100:
        return 10
    elif 81 <= marks <= 90:
        return 9
    elif 71 <= marks <= 80:
        return 8
    elif 61 <= marks <= 70:
        return 7
    elif 51 <= marks <= 60:
        return 6
    elif 41 <= marks <= 50:
        return 5
    elif 35 <= marks <= 40:
        return 4
    else:
        return 0

print("Welcome to CGPA Calculator\n")

marks = []
for i in range(1, 7):
    m = int(input(f"Enter marks for Subject {i}: "))
    marks.append(marks_to_cgpa(m))

cgpa = sum(marks) / len(marks)
print(f"\nYour CGPA is {cgpa}")
