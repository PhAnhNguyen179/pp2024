#student mark manager system
#use tuples,dicts,lists,No objects/classes
"""
tuples: Immutable sequence;Contain any type of element; A very common use of tuples is a simple representation of
pairs: Positition (x, y),Size (w, h)
used to store multiple items in a single variable

dict: used to store data values in key:value pairs;a collection which is ordered*, changeable and do not allow duplicates

list:Mutable sequence;Values can be changed later;Flexible, widely used;Comma separated declaration
store multiple items in a single variable
"""





#initialize variables
students = [] #initialize emty list
courses =[]

#input functions

def input_number_of_students():
    global students
    number_of_students = int(input("Enter number of students in class: "))
    for i in range(number_of_students):
        student_id = input("Enter the student ID " + str(i + 1) + ": ")
        student_name = input("Enter the student name " + str(i + 1) + ": ")
        student_dob = input("Enter the student DoB " + str(i + 1) + ": ")
        students.append({"id": student_id, "name": student_name, "dob": student_dob, "marks": {}})

def input_number_of_courses():
    global courses
    number_of_courses = int(input("Enter the number of courses: "))
    for i in range(number_of_courses):
        course_id = input("Enter the course ID " + str(i + 1) + ": ")
        course_name = input("Enter the course name " + str(i + 1) + ": ")
        courses.append({"id": course_id, "name": course_name, "students": []})

def select_course():
    for course in courses:
        print(course['id'] + ": " + course['name'])
    course_id = input("Select a course: ")
    selected_course = None
    for c in courses:
        if c["id"] == course_id:
            selected_course = c
            break
    return selected_course

def list_student_marks_for_given_course(course):
    print("Student marks for course " + course['id'] + ":")
    for student in students:
        if student["id"] in course["students"]:
            print(student['id'] + ": " + str(student['marks'][course['id']]))
def print_course_info(course):
    print(course['id'] + ": " + course['name'])

def print_student_info(student):
    print(student['id'] + ": " + student['name'])

def select_course():
    for course in courses:
        print_course_info(course)
    
    course_id = input("Select a course: ")
    selected_course = None
    
    for c in courses:
        if c["id"] == course_id:
            selected_course = c
            break
    
    return selected_course

def list_courses():
    print("Courses:")
    for course in courses:
        print_course_info(course)

def list_students():
    print("Students:")
    for student in students:
        print_student_info(student)

def show_student_marks_for_given_course(course):
    print("Marks for students in course " + course['id'] + ":")
    for student in students:
        if student["id"] in course["students"]:
            print(student['id'] + ": " + str(student['marks'][course['id']]))

def mark_for_student_in_course(course):
    student_id = input("Enter the student ID to add a mark: ")
    for student in students:
        if student["id"] == student_id:
            mark = float(input("Enter the mark for student " + student['id'] + " in course " + course['id'] + ": "))
            student["marks"][course["id"]] = mark
            course["students"].append(student["id"])
            return
    print("Student not found with ID:", student_id)
    
input_number_of_students()
input_number_of_courses()
list_courses()
list_students()
selected_course = select_course()
if selected_course:
    mark_for_student_in_course(selected_course)
    show_student_marks_for_given_course(selected_course)
    list_student_marks_for_given_course(selected_course)
else:
    print("No course selected.")

