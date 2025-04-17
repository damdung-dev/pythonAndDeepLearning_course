import POO21
list_studentName=[]
list_id=[]
list_semester=[]
list_courseName=["Java",".Net","C/C++"]
print("WELCOME TO STUDENT MANAGEMENT\n"
      "\t 1.Create"
      "\t 2.Find and Sort"
      "\t 3.Update/Delete"
      "\t 4.Report"
      "\t 5.Exit")
sel1= input("Please type one of the numbers above: ")
if sel1=="1":
    dem = 1
    print("===================Dữ liệu nhập vào=============================")
    while True:
        studentName = input(f"Tên học sinh {dem}: ")
        id = input("ID: ")
        semester = input("Kỳ học: ")
        courseName = input("Tên khóa học: ")
        list_studentName.append(studentName)
        list_id.append(id)
        list_semester.append(semester)
        if courseName not in list_courseName:
            print("Hiện không có khóa học của bạn")
            continue
        dem += 1
        print("-------------------------------------------------------------")
        if dem > 3:
            print("Bạn có muốn nhập tiếp")
            sel2 = input("1.yes\n2.no  ")
            if sel2 == "yes" or sel2 == "y" or sel2 == "1":
                continue
            elif sel2 == "no" or sel2 == "n" or sel2 == "2":
                break
            else:
                break
        else:
            continue
    print("===================Dữ liệu trong hệ thống======================")
    for dem1 in range(1, len(list_studentName) + 1):
        st=POO21.Students(list_id[dem1-1],list_studentName[dem1-1],list_semester[dem1-1],list_courseName[dem1-1])
        st.create()
elif sel1=="2":
    for dem3 in range(1, len(list_studentName) + 1):
        st = POO21.Students(list_id[dem3 - 1], list_studentName[dem3 - 1], list_semester[dem3 - 1],
                            list_courseName[dem3 - 1])
        st.find_and_sort()
else:
    exit()
