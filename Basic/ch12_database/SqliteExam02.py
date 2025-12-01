import sqlite3

from xml.etree.ElementTree import parse

# step01 : xml 파일 읽기
tree = parse('sungjuk.xml')
root = tree.getroot()

# step02 : sqlite DB 열기
conn = sqlite3.connect('sungjuk.db')
mycursor = conn.cursor()

# step03 : 테이블 삭제 후 생성
try:
    mycursor.execute('drop table sungjuk')
except sqlite3.OperationalError:
    print('테이블이 존재하지 않습니다.')
# end try

# xml 문서 구조를 보고 테이블 만들기
sql = '''
    create table sungjuk(
        id text,
        subject text,
        jumsu integer
)
'''

mycursor.execute(sql)

# step04 : xml 데이터를 DB에 추가하기
data_list = [] # 데이터 베이스에 추가할 행 목록

# root : xml 전체
# 1개 find , 여러개 findall , iter
for student in root.iter('student'):
    sid = student.find('id').text
    subject = student.find('subject').text
    jumsu = student.find('jumsu').text
    data_list.append((sid, subject, jumsu))
# end for

# print(data_list)

sql = "insert into sungjuk values (?, ?, ?)"
mycursor.executemany(sql, data_list)

conn.commit() # 데이터 베이스 커밋처리

# step05 : 전체 목록을 보여주는 함수 작성
def getAllStudents(dbcursor):
    for onetuple in dbcursor:
        print('아이디 : ' + onetuple[0], end='')
        print(', 과목 : ' + onetuple[1], end='')
        print(', 점수 : ' + str(onetuple[2]))
    #end for
#end def

# step05 : 테이블의 내용 출력
sql = 'select * from sungjuk'
mycursor.execute(sql)
getAllStudents(mycursor)

# step06 : 작업 객체를 닫기
mycursor.close()
conn.close()