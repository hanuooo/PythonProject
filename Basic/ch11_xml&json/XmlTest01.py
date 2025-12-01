from xml.etree.ElementTree import Element, ElementTree
from xml.etree.ElementTree import SubElement

xmldata = Element('student', address="상수동")

xmldata.attrib['birth'] = '19951225'

SubElement(xmldata, 'name').text = '김대호'
SubElement(xmldata, 'age').text = '20'
SubElement(xmldata, 'gender').text = '남자'
SubElement(xmldata, 'grade').text = 'A'
SubElement(xmldata, 'university').text = '서강대'


# 아래 코드는 주석을 상세히 작성한 내용입니다.
def indent(elem, level=0):
    """
    XML 요소(elem)에 들여쓰기와 개행을 적용하여
    사람이 읽기 좋은 형태로 XML 문자열을 정렬(Pretty Print)하는 함수.

    매개변수:
        elem  : 정렬할 XML 요소(ElementTree.Element)
        level : 현재 들여쓰기 단계(재귀적으로 호출될 때 증가)
    """
    mytab = '\t'  # 들여쓰기(tab) 문자
    i = '\n' + level * mytab  # 현재 레벨에 맞는 개행 + 들여쓰기

    # -------------------------------
    # 1) 자식 요소가 있는 경우
    # -------------------------------
    if len(elem):
        # 현재 요소의 텍스트가 없거나 공백뿐인 경우 → 들여쓰기 적용
        if not elem.text or not elem.text.strip():
            elem.text = i + mytab  # 자식 시작 전에 한 단계 더 들여쓰기

        # 현재 요소의 tail(닫힌 후 뒤에 오는 텍스트)이 없거나 공백만인 경우 → 들여쓰기 적용
        if not elem.tail or not elem.tail.strip():
            elem.tail = i

        # 모든 자식 요소에 대해 재귀적으로 들여쓰기 적용
        for elem in elem:
            indent(elem, level + 1)

        # 마지막 자식 요소 처리 후 tail 정리
        if not elem.tail or not elem.tail.strip():
            elem.tail = i

    # -------------------------------
    # 2) 자식 요소가 없는 경우(leaf element)
    # -------------------------------
    else:
        # 레벨이 0이 아니면서 tail이 없거나 공백뿐인 경우 → 들여쓰기 적용
        # (루트 요소는 tail 필요 없음)
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
# end def

indent(xmldata)

xmlFile = 'XmlTest01.xml'
ElementTree(xmldata).write(xmlFile, encoding='UTF-8')
print(xmlFile + '파일이 생성되었습니다.')

