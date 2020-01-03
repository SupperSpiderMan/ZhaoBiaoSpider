# coding=gbk

'''�ܵ��ļ���������д��excel�ļ�'''

import xlwt

import sys
sys.path.append('..')
from Settings import filename, SearchType

def settle(data):
    '''
    ��������
    :param data: Ҫд�������
    :param searchType: ��������
    :return: ����������
    '''
    if SearchType == 1:
        searchType = '�ؼ�������'
    elif SearchType == 2:
        searchType = 'URL����'
    elif SearchType == 3:
        searchType = '�ؼ���+URL����'

    result = [['��ת����', '����', '���', '����ʱ��', '������', '�����ؼ���', '��Ϣ��Դ', '������ʽ']]
    for d in data:
        for value in d['value']:
            if value['data'] == '����������':
                result.append(['����������', '����������', '����������', '����������', '����������', value['keyword'], d['name'], searchType])
            else:
                for info in value['data']:
                    result.append([info['url'], info['title'], info['synopsis'], info['create_time'], info['name'], value['keyword'], d['name'], searchType])
    write(result)

def write(result):
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet1')

    row = 0
    for item in result:
        cow = 0
        for info in item:
            sheet.write(row, cow, info)
            cow += 1
        row += 1

    book.save(filename)
    print('�ļ��ѱ�����', filename)


# if __name__ == '__main__':
#     data = [{'name': '���������ɹ���', 'value': [{'keyword': '�״�', 'data': [{'url': 'http://www.ccgp-ningxia.gov.cn/public/NXGPPNEW/dynamic/contents/CGGG/ZBGG/content.jsp?id=04be87a5-42aa-474b-b8ce-68a3451e8c27&cid=316&sid=1&type=101', 'title': '���������Ӳ���ɹ�(�״����ݴ��������', 'synopsis': 'δ�ṩ���', 'create_time': '2019-06-03', 'name': 'δ�ṩ������'}, {'url': 'http://www.ccgp-ningxia.gov.cn/public/NXGPPNEW/dynamic/contents/CGGG/ZBGG/content.jsp?id=1b43a88d-8544-47f4-a197-79f944417c05&cid=316&sid=1&type=101', 'title': '���Ļ����������������Ժ����ɹ��ɱ�һ�廯������������ܼ������ͼ������״����ݴ����༭���', 'synopsis': 'δ�ṩ���', 'create_time': '2017-06-30', 'name': 'δ�ṩ������'}]}, {'keyword': '�����״�', 'data': '����������'}]}]
#     settle(data)