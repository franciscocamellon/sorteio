def students_list():
    formated_list = []
    file = open('students.txt', 'r', encoding="utf8")
    for line in file:
        n_line = line.replace('\n','')
        formated_list.append(n_line)
        formated_list.sort()
    return formated_list
    print(formated_list)


students_list()