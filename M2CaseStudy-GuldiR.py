## author: GuldiR
## date: 01/24/2024
## program name: M2 Case Study - If, else, and while
## program desc: 
## This program allows for students last name, first name, and GPA to be entered and print a message stating whether the student made it to the Deans List or Honors Roll if they meet the GPA requirements.


def verify_deans_list(student_gpa):
    return student_gpa >= 3.5  

def verify_honor_roll(student_gpa):
    return student_gpa >= 3.25

#
def add_student():

    student_last = input("Enter student's last name (or enter 'zzz' to quit)): ")
    ## validation check
    if student_last.upper() == "ZZZ":
        return None, None, None
    
    student_first = input("Enter the student's first name: ")    
    student_gpa = float(input("Enter student GPA: "))


    return student_last, student_first, student_gpa

def main() -> None:
    """Main program loop"""

    while True:
        student_last, student_first, student_gpa = add_student()
        if student_last is None or student_first is None or student_gpa is None:
            break

       
        if verify_deans_list(student_gpa):
            print(f"{student_first} {student_last} qualified for the Deans List! \n")
        
        elif verify_honor_roll(student_gpa):
            print(f"{student_first} {student_last} qualified for the Honor Roll! \n")
        else:
            print("Student does not qualify for additional recognition at the present time. \n")


if __name__ == "__main__":
    main()