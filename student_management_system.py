student=[]
def load_students():
    try:
        with open("student.txt","r") as file:
            content=file.read()
            if content:
                print("Previous records found and loaded successfully!")
            else:
                print("No records found")
    except FileNotFoundError:
        print("No records found")
load_students()


def add_student():
    name=input("Enter Name of Student=")
    roll_no=int(input("Enter Roll No of Student="))
    atmost=int(input("MAX MARKS="))
    print("Enter Marks of given Subjects")
    maths=float(input("MATHS:"))
    python=float(input("PYTHON:"))
    ai=float(input("ARTIFICIAL INTELLIGENCE:"))
    english=float(input("ENGLISH:"))
    physics=float(input("PHYSICS:"))
    subject={"MATHS":maths,"PYTHON":python,"ARTIFICIAL INTELLIGENCE":ai,"ENGLISH":english,"PHYSICS":physics}
    total=maths+python+ai+english+physics
    percentage=total*100/atmost/5
    if percentage>=90:
        grade="A grade"
    elif percentage>=75:
        grade="B grade"
    elif percentage>=60:
        grade="C grade"
    else:
        grade="D grade"
    scorecard={"name":name,"roll no":roll_no,"marks":subject,"total":total,"percentage":percentage,"grade":grade}
    student.append(scorecard)
    with open("student.txt","a") as file:
        file.write(f"Name:{name} |Roll No:{roll_no} | Maths:{maths} | Python:{python} | Artificial Intelligence:{ai} | English:{english} | Physics:{physics} | Total:{total} | percentage:{percentage} | grade:{grade}\n")
    print("Student added successfully!")



def view_std():
    if len(student)==0:
        print("No student details added please first!")
    else:
        for scorecard in student:
            print("============================================================================================")
            print("Name:", scorecard["name"])
            print("Roll No:", scorecard["roll no"])
            for subject in scorecard["marks"]:
                print(subject,":",scorecard["marks"][subject])
            print("Total",":",scorecard["total"])
            print("percentage",":",round(scorecard["percentage"],2),"%")
            print("grade",":",scorecard["grade"])

def search_std():
    search=input("Enter name of Student:")
    found=False
    for scorecard in student:
        if scorecard["name"].lower()==search.lower():
            found=True
            print("============================================================================================")
            print("Name:", scorecard["name"])
            print("Roll No:", scorecard["roll no"])
            for subject in scorecard["marks"]:
                print(subject,":",scorecard["marks"][subject])
            print("Total",":",scorecard["total"])
            print("percentage",":",round(scorecard["percentage"],2),"%")
            print("grade",":",scorecard["grade"])
    if found==False:
            print("Student_not_found")

def topper():
    if len(student)==0:
        print("_NO_STUDENT_ADDED_YET_")
    else:
        topper=student[0]
        for scorecard in student:
            if scorecard["percentage"]>topper["percentage"]:
                topper=scorecard
        print("============================================================================================")
        print("TOPPER:",topper["name"])
        print("Name:", topper["name"])
        print("Roll No:", topper["roll no"])
        for subject in topper["marks"]:
            print(subject,":",topper["marks"][subject])
        print("Total",":",topper["total"])
        print("percentage",":",round(topper["percentage"],2),"%")
        print("grade",":",topper["grade"])

def menu():
    print("============================================================================================")
    print("______________________________STUDENT_MANAGEMENT_SYSTEM_____________________________________")
    print("============================================================================================")
    print("1. Add student")
    print("2. View all Student")
    print("3. Search Student") 
    print("4. Find Topper")
    print("5. Exit")   
while True:
    menu()
    choice=int(input("Enter choice: "))

    if choice==1:
        add_student()
    elif choice==2:
        view_std()
    elif choice==3:
        search_std()
    elif choice==4:
        topper()
    elif choice==5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
