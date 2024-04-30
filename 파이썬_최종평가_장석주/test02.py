def getStudent(no, name, major):
    student = {'학번': no, '이름': name, '전공': major}
    return student

no = input('학번 : ')
name = input('이름 : ')
major = input('전공명 : ')

student = getStudent(no, name, major)

print('학번 : ', no)
print('이름 : ', name)
print('전공 : ', major)