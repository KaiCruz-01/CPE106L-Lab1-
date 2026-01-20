student = { 
    "id": "2025-001", 
    "name": "Juan Dela Cruz", 
    "grades": [88, 90, 85] 
} 
student["grades"]

student["name"] = "Juan D. Cruz"

print ("--- STUDENT REPORT ---")
print ("Name:   ", student["name"])
print ("ID:     ", student["id"])
print ("Grades: ", student["grades"])

average = sum(student["grades"]) / len(student["grades"])
print("Average:", round(average, 2))
