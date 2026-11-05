# Store students as roll_no -> {"name": ..., "marks": {subject: score}}.
records = {}
def addStudent():
	global records
	roll = str(input("Enter Roll Number  :"))
	if(roll in records.keys()):
		print("Roll Number Already exsists")
		return 
	name = str(input("Enter Name  :"))
	math = int(input("Enter the Marks in Maths : "))
	phy = int(input("Enter the Marks in Physics : "))
	chem = int(input("Enter the Marks in Chemestry : "))
	if((math >= 0 and math <= 100) and (phy >= 0 and phy <= 100) and (chem >= 0 and chem <= 100)):
		records[roll] = {"name" : name,"marks" : {"math":math,"phy":phy,"chem":chem}}
		print("Record Inserted Succesfully")
		# print(records)

	else : 
		print("Abnormal Input Please verify the marks legality")
# addStudent()
def updateStudent():
	global records
	roll = str(input("Enter Roll Number  :"))
	if(roll not in records.keys()):
		print("Roll Number Dosen't exsists")
		return 

	sub = str(input("Enter the Subject Name that needs to be updated")).lower()
	upMarks = int(input("Enter the Updated Marks : "))
	if (upMarks>= 0 and upMarks <= 100):
		records[roll]["marks"][sub] = upMarks
		print("Update Succesfull")
	else : 
		print("Invalid Marks")

def deleteStudent():
	global records
	roll = str(input("Enter Roll Number  :"))
	if(roll not in records.keys()):
		print("Roll Number Dosen't exsists")
		return 
	deleted_record = records.pop(roll, None) 
	if deleted_record != None:
		print("Deleted... ")
	else : 
		print("Couldn't delete data")


def showRecords():
	global records
	roll = str(input("Enter Roll Number  :"))
	if(roll not in records.keys()):
		print("Roll Number Dosen't exsists")
		return 
	student = records[roll]
	print("Name: ",student['name'])
	print("Marks : ",student['marks'])

def showReports():
    global records
    if not records:
        print("No student records available.")
        return

    print("\n--- REPORTS ---")
    
    print("\n1. Average Marks of Every Student:")
    averages = {roll: round(sum(data['marks'].values()) / len(data['marks']), 2) for roll, data in records.items()}
    for roll, avg in averages.items():
        print(f"   Roll {roll} ({records[roll]['name']}) -> {avg}")


    if averages:
        topper_roll = max(averages, key=averages.get)
        print(f"\n2. Topper: {records[topper_roll]['name']} (Roll: {topper_roll}, Average: {averages[topper_roll]})")

    print("\n3. Highest Scorer in Each Subject:")
    
    all_subjects = {sub for data in records.values() for sub in data['marks'].keys()}
    for sub in sorted(all_subjects):
        
        highest_scorer = max(records.values(), key=lambda x: x['marks'].get(sub, -1))
        score = highest_scorer['marks'].get(sub)
        print(f"   {sub.capitalize()} -> {highest_scorer['name']} ({score})")

    
    print("\n4. Students Scoring Below 40 in At Least One Subject:")
    below_40_students = [
        (data['name'], sub, score) 
        for data in records.values() 
        for sub, score in data['marks'].items() 
        if score < 40
    ]
    if below_40_students:
        for name, sub, score in below_40_students:
            print(f"   {name} scored {score} in {sub}")
    else:
        print("   None")

    
    print("\n5. Grade-wise Grouping (Based on Average Marks):")
    grades = {"A": [], "B": [], "C": [], "D": [], "F": []}
    for roll, avg in averages.items():
        name = records[roll]['name']
        if avg >= 90:
            grades["A"].append(name)
        elif avg >= 75:
            grades["B"].append(name)
        elif avg >= 60:
            grades["C"].append(name)
        elif avg >= 40:
            grades["D"].append(name)
        else:
            grades["F"].append(name)
            
    for grade, names in grades.items():
        print(f"   Grade {grade}: {names if names else 'None'}")



while True:
    print("\n--- Student Database Menu ---")
    print("1. Add a student")
    print("2. Update one subject's marks for a student")
    print("3. Delete a student")
    print("4. Show a student's full record")
    print("5. Reports")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        addStudent()
    elif choice == '2':
        updateStudent()
    elif choice == '3':
        deleteStudent()
    elif choice == '4':
        showRecords()
    elif choice == '5':
        showReports()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select between 1 and 6.")


'''
--- Student Database Menu ---
1. Add a student
2. Update one subject's marks for a student
3. Delete a student
4. Show a student's full record
5. Reports
6. Exit
Enter your choice (1-6): 1
Enter Roll Number  :101
Enter Name  :Jay
Enter the Marks in Maths : 90
Enter the Marks in Physics : 70
Enter the Marks in Chemestry : 90
Record Inserted Succesfully

--- Student Database Menu ---
1. Add a student
2. Update one subject's marks for a student
3. Delete a student
4. Show a student's full record
5. Reports
6. Exit
Enter your choice (1-6): 4
Enter Roll Number  :101
Name:  Jay
Marks :  {'math': 90, 'phy': 70, 'chem': 90}

--- Student Database Menu ---
1. Add a student
2. Update one subject's marks for a student
3. Delete a student
4. Show a student's full record
5. Reports
6. Exit
Enter your choice (1-6): 4
Enter Roll Number  :102
Roll Number Dosen't exsists

--- Student Database Menu ---
1. Add a student
2. Update one subject's marks for a student
3. Delete a student
4. Show a student's full record
5. Reports
6. Exit
Enter your choice (1-6): 1
Enter Roll Number  :102
Enter Name  :Khush
Enter the Marks in Maths : 90
Enter the Marks in Physics : 50
Enter the Marks in Chemestry : 99
Record Inserted Succesfully

--- Student Database Menu ---
1. Add a student
2. Update one subject's marks for a student
3. Delete a student
4. Show a student's full record
5. Reports
6. Exit
Enter your choice (1-6): 1
Enter Roll Number  :Harshil
Enter Name  :kn
Enter the Marks in Maths : 324
Enter the Marks in Physics : 234
Enter the Marks in Chemestry : 23
Abnormal Input Please verify the marks legality

--- Student Database Menu ---
1. Add a student
2. Update one subject's marks for a student
3. Delete a student
4. Show a student's full record
5. Reports
6. Exit
Enter your choice (1-6): 1
Enter Roll Number  :103
Enter Name  :Harshil
Enter the Marks in Maths : 80
Enter the Marks in Physics : 80
Enter the Marks in Chemestry : 90
Record Inserted Succesfully

--- Student Database Menu ---
1. Add a student
2. Update one subject's marks for a student
3. Delete a student
4. Show a student's full record
5. Reports
6. Exit
Enter your choice (1-6): 5

--- REPORTS ---

1. Average Marks of Every Student:
   Roll 101 (Jay) -> 83.33
   Roll 102 (Khush) -> 79.67
   Roll 103 (Harshil) -> 83.33

2. Topper: Jay (Roll: 101, Average: 83.33)

3. Highest Scorer in Each Subject:
   Chem -> Khush (99)
   Math -> Jay (90)
   Phy -> Harshil (80)

4. Students Scoring Below 40 in At Least One Subject:
   None

5. Grade-wise Grouping (Based on Average Marks):
   Grade A: None
   Grade B: ['Jay', 'Khush', 'Harshil']
   Grade C: None
   Grade D: None
   Grade F: None

--- Student Database Menu ---
1. Add a student
2. Update one subject's marks for a student
3. Delete a student
4. Show a student's full record
5. Reports
6. Exit
Enter your choice (1-6): 6 
Exiting program. Goodbye!
'''



