import mysql.connector as sql

conn = sql.connect(host='localhost',
                   user='root',
                   passwd='',                    #your password
                   database='project')
# if conn.is_connected():
# print("Successfully Connected")
c1 = conn.cursor()
print("=================================================================================================================")
print("SSB Computer Institute Management System")
print("=================================================================================================================")
print("1. Enrolling For A Course")
print("2. Edit Enrollments (as admin)")
print("3. Display Details")
print("4. Exit")
choice = int(input("Enter the Choice - "))

if choice == 1:
        v_admno = int(input("Enter the Admission Number: "))
        v_candidatename = input("Enter your name : ")
        v_course = input("Enter the Course: ")
        v_time = ''
        v_teacher=''
        if v_course == 'JAVA':
            v_course = 'JAVA'
            v_time = '6 months'
            v_teacher = 'Mr.Herry'
        elif v_course == 'Python':
            v_course = 'Python'
            v_time = '5 months'
            v_teacher = 'Mr.Potter'
        elif v_course == 'C':
            v_course = 'C'
            v_time = '7 months'
            v_teacher = 'Mr.Bush'
        elif v_course == 'BASIC':
            v_course = 'BASIC'
            v_time = '4 months'
            v_teacher = 'Ms.Granger'
        elif v_course == 'HTML':
            v_course = 'HTML'
            v_time = '8 months'
            v_teacher = "Ms.Susan"

        V_SQL_Insert = "insert into candidates values (" + str(v_admno) + ",'" + v_candidatename + "','" + v_course + "','" + v_time +"','" + v_teacher + "'" + ")"
        c1.execute(V_SQL_Insert)
        print(" ")
        print("You are Enrolled Mr.", v_candidatename, ". Congrats!!!")
        conn.commit()
        print(" ")
        print("Your enrollment for", v_course, "course is successful!")

if choice == 2:
    uname = input("Enter Username:")
    passwd = input("Enter Password:")
    u_name = 'Sukhman'
    pass_wd = '777'
    if (uname == u_name) and (passwd == pass_wd):
        print("!!Password Accepted!!")
        print("1. Delete An Enrollment")
        print("2. Edit Name")
        print("3. Edit Course")
        print(" ")
        option = int(input("Which of the above options would you like to choose ?"))

        if option == 1:
            change_adm_no = int(input("Enter the admission number of the candidate to be removed:"))
            V_SQL_Insert = "delete from candidates where admno = " + str(change_adm_no)
            c1.execute(V_SQL_Insert)
            print("")
            print("Successfully removed")
            conn.commit()
        if option == 2:
            change_adm_no = int(input("Enter the admission number of the candidate whose name is to be changed:"))
            change_name = input("Enter the desired name:")
            V_SQL_Insert = "update candidates set candidate_name = '" + change_name + "' where admno = " + str(
                change_adm_no)
            c1.execute(V_SQL_Insert)
            print("")
            print("Successfully edited")
            conn.commit()
        if option == 3:
            change_adm_no = int(input("Enter the admission number of the candidate whose course is to be changed:"))
            change_course = input("Enter the Course: ")
            if change_course == 'JAVA':
                change_course = 'JAVA'
            elif change_course == 'Python':
                change_course = 'Python'
            elif change_course == 'C':
                change_course = 'C'
            elif change_course == 'BASIC':
                change_course = 'BASIC'
            elif change_course == 'HTML':
                change_course = 'HTML'
            V_SQL_Insert = "update candidates set course = '" + change_course + "' where admno = " + str(
                change_adm_no)
            c1.execute(V_SQL_Insert)
            print("")
            print("Successfully modified")
            conn.commit()

    else:
        print("Wrong Username or Password")

if choice == 3:
    c1.execute("Select * from candidates")
    data = c1.fetchall()
    for row in data:
        print("=========================================================================================================")
        print("Candidates Details ")
        print("Admission Number : ", row[0])
        print("Candidate Name   : ", row[1])
        print("Course Selected  : ", row[2])
        print("Duration  : ", row[3])
        print("Teacher  : ", row[4])
if choice == 4:
    print('Thank You ')
