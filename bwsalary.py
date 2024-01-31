years = int(input("Enter years of work: "))
worktype = input("Enter kind of work: ").lower()
income = {"b":['10,000','12,000','15,000'],
        "w":['20,000','40,000','75,000']}
if years >= 5 and worktype in income:
    print("Salary: ", income[worktype][2])  
if years < 5 and years >= 2 and worktype in income:
    print("Salary: ", income[worktype][1])    
if years < 2 and worktype in income:
    print("Salary: ", income[worktype][0])
