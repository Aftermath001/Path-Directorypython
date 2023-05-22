import csv
# Open up csv file
# with open('/home/alvin/Development/code/phase3/Path-Directorypython/path/Q4/Student.csv') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)
with open('/home/alvin/Development/code/phase3/Path-Directorypython/path/Q4/Student.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[1] < '18':
            with open ('/home/alvin/Development/code/phase3/Path-Directorypython/path/Q4/young_students.txt','a') as student_file:

                student_file.write(str(row)+ '\n')
            # with open ('/home/alvin/Development/code/phase3/Path-Directorypython/path/Q4/young_students.txt') as student_file:
            #     content = student_file.read()
            # print (content)
        else:
            print 