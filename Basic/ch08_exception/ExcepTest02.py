# ExcepTest02.py

def student(findStudent):
    students = ['철수', '영희', '민수', '지영']
    if findStudent in students:
        print(f'학생 \'{findStudent}\'은(는) 존재합니다.')
    else:
        message = f'학생 \'{findStudent}\'은(는) 존재하지 않습니다.'
        raise Exception(message)
# end def student
try:
    checkList = ['철수', '훈식']
    for stu in checkList:
        student(stu)
    # end for
except Exception as err:
    print('예외 발생 : {}'.format(err))
    # end for

