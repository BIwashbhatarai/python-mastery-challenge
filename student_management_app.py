import os 

student_file = "students.txt"
def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    grade = input("Enter Grade: ")
    
    with open (student_file, "a") as file:
        file.write(f"{name},{roll},{grade}\n")
    print("✅ Student added successfully!\n")
    
def view_student():
    if not os.path.exists(student_file):
        print("❌ No student data found.\n")
        return
    
    with open (student_file,"r")as file:
        students = file.readlines()
    
    if not students:
        print("❌No student available.\n")
    else:
        print("\nAll Students: ")
        for student in students:
            parts = student.strip().split(",")
            if len(parts) == 3:
                name, roll, grade = parts
                print(f"Name: {name} | Roll: {roll} | Grade: {grade}")
            else:
                print(f"⚠️ Corrupted data: {student}")
        print()
        
def search_student():
    keyword = input("Enter name to search: ").lower()
    found = False
    
    if not os.path.exists(student_file):
        print("❌ No student data found.\n")
        return
    
    with open(student_file, "r") as file:
        for student in file:
            parts = student.strip().split(",")
            if len(parts) == 3:
                name, roll, grade = parts 
                if keyword in name.lower():
                    print(f"✅ Found: Name {name} | Roll: {roll} | Grade: {grade}")
                    found = True
    if not found:
        print("❌ Student not found.\n")
    
    
def delete_student():
    view_student()
    roll_to_delete = input("Enter the roll number to delete: ")
    
    if not os.path.exists(student_file):
        print("❌ No student data found.\n")
        return
    
    updated_student = []
    with open(student_file, "r") as file:
        students = file.readlines()
        
    for student in students: 
        parts = student.strip().split(",")
        if len(parts) == 3:
            name, roll , grade = parts
            if roll != roll_to_delete:
                updated_student.append(student)
            else:
                found = True
    with open(student_file, "w") as file:
        file.writelines(updated_student)
    if found:
        print("✅ Student deleted successfully\n")
    else:
        print("❌ Student with that roll number not found.\n") 
        
def main():
    while True:
        print("📚 Student management menu")
        print("1) Add Student")
        print("2) View Student")
        print("3) Search Student")
        print("4) Delete Student")
        print("5) Exit")
        try:
            choice = input("Enter your choice(1-5): ")
            if choice == "1":
                add_student()
            elif choice == "2":
                view_student()
            elif choice == "3":
                search_student()
            elif choice == "4":
                delete_student()
            elif choice == "5":
                print("👋Exiting Studene Management app. ")
            else:
                print("Please enter correct option (1-5)")
        except Exception as e:
            print("An error has occured. i.e", e)
            
if __name__ == "__main__":
    main()