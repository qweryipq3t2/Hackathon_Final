import mysql.connector as ms
connect = ms.connect(host = "localhost", port=3306,password = "Hungrie@20",
                     user = "root", database ="details")


# Get a cursor
cur = connect.cursor()

# Execute a query
values = (874785307530, "Bold jeck", 25, 9845398756,"BLA BLABLA", "EXP1")
cur.execute("INSERT into Pd(Aadhar_no,Full_name,age,Phone_no,vulnerabilities,Experience,Urgency_score) "
"VALUES (%s,%s,%s,%s,%s,%s,%s)", values)
values1 = ("Satish lai", 9783085044,"Bricklaying",35,"Bettahulsur",300)
cur.execute("INSERT INTO Jl(Employer,Employer_Phoneno,jb_name , Availability, \
location,Fixed_wage_per_hr)" "VALUES (%s,%s,%s,%s,%s,%s)", values1)
values2=(874785307530,"Bricklaying", True)
cur.execute("INSERT into J_A(Aadhar_no,Assigned_jb, Assigned)" "VALUES (%s,%s,%s)", values2)
connect.commit()


priority_values = ()


# Fetch assigned jobs
cur.execute("SELECT Assigned_jb FROM J_A WHERE Assigned = TRUE")
assigned_jobs = cur.fetchall()

# Reduce availability
for job in assigned_jobs:
    cur.execute(
        "UPDATE Jl SET Availability = Availability - 1 WHERE jb_name = %s",
        (job[0],)
    )
connect.commit()

cur.execute("Select Availability from Jl;")
t = cur.fetchall()
connect.commit()    

# Close connection
cur.close()
