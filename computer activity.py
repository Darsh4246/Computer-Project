total = int(input("Enter total marks:"))
obtained = int(input("Enter marks obtained:"))
if total < obtained:
    print("Total is greater than obtained.")
else:
    pass
percent = (obtained/total)*100
print("Percentage:",percent)

if percent > 90:
    grade = "A"
elif percent >= 80:
    grade = "B"
elif percent >= 70:
    grade = "C"
elif percent >= 60:
    grade = "D"
else:
    grade = "E"

print("Grade:",grade)  
    
