# -*- coding: utf-8 -*-
# IMPORTANT: Windows console codepage 949

import tokenize
import time
import re
import datetime
import os

# tokenize
YEAR = r'(?P<YEAR>\d+)년'
MONTH = r'(?P<MONTH>\d+)월'
DAY = r'(?P<DAY>\d+)일'
HOUR = r'(?P<HOUR>\d+)시'
MINUTE = r'(?P<MINUTE>\d+)분'
WS = r'(?P<WS>\s+)'

if __name__ == '__main__':
    token_key = ['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE']
    default_key = ['%Y', '%m', '%d', '%H', '%M']

    uid = time.strftime('%Y-%m-%d-%H%M%S')

    # date input
    desired = input('Enter the Desired Date: ')
    date_pat = re.compile('|'.join([YEAR, MONTH, DAY, HOUR, MINUTE, WS]))
    parse_date = tokenize.Token()

    dateDict = parse_date.generate_dict(date_pat, desired)

    # parsing
    for tok, cur in zip(token_key, default_key):
        if tok is 'HOUR':
            dateDict[tok] = '12'
        elif tok is 'MINUTE':
            dateDict[tok] = '0'

        if tok not in dateDict.keys():
            dateDict[tok] = time.strftime(cur)

    target_str = dateDict['YEAR'] + \
                 dateDict['MONTH'] + \
                 dateDict['DAY'] + \
                 dateDict['HOUR'] + \
                 dateDict['MINUTE']

    target_date = datetime.datetime.strptime(target_str, ''.join(default_key))
    start_date = target_date - datetime.timedelta(hours=1)

    start_str = datetime.datetime.strftime(start_date, '%Y%m%dT%H%M%S')
    target_str = datetime.datetime.strftime(target_date, '%Y%m%dT%H%M%S')

    ## plan memo
    sentence = input('Enter Your Plan: ')

    check_text = '### CHECK ###\n{}년 {}월 {}일 {}시 {}분 이벤트\n {}'.format(
        dateDict['YEAR'],
        dateDict['MONTH'],
        dateDict['DAY'],
        dateDict['HOUR'],
        dateDict['MINUTE'],
        sentence
    )
    print(check_text, end=' ')
    yn = input('y/n: ')

    # print(sentence)
    # remark y/n

    # ics formatting
    # preprocessing

    # formatting
    ics_format = """
BEGIN:VCALENDAR
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
PRODID:BOT Product
BEGIN:VEVENT
UID:{}
DTSTAMP:{}
DTSTART:{}
DTEND:{}
SUMMARY:{}
DESCRIPTION:{}
BEGIN: VALARM
TRIGGER: -PT1440M
DESCRIPTION: 자동 생성된 이벤트 입니다.
END:VALARM
END:VEVENT
END:VCALLENDAR
""".format(
        uid,
        time.strftime('%Y%m%dT%H%M%S'),
        start_str,
        target_str,
        sentence,
        sentence,
    )

    print(ics_format)

    # binary encoding
    ics_format = ics_format.encode('utf-8')

    # make ics
    filename = uid + '.ics'
    with open(filename, 'wb') as f:
        f.write(ics_format)

    os.system('start ' + filename)
    print('Success!')
