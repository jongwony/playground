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

    # date input
    desired = input('Enter the Desired Date: ')
    title = input('Enter Summary: ')
    location = input('Enter Location: ')
    desc = input('Enter Description: ')
    duration = input('Enter Duration(시간): ')
    alarm = input('Enter Alarm(시간 전): ')

    duration = int(duration)
    alarm = int(alarm)
    assert duration > 0, "숫자를 입력해야 합니다."
    assert alarm > 0, "숫자를 입력해야 합니다."

    token_key = ['YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE']
    default_key = ['%Y', '%m', '%d', '%H', '%M']

    uid = time.strftime('%Y-%m-%d-%H%M%S')

    date_pat = re.compile('|'.join([YEAR, MONTH, DAY, HOUR, MINUTE, WS]))
    parse_date = tokenize.Token()

    dateDict = parse_date.generate_dict(date_pat, desired)

    # parsing
    for tok, cur in zip(token_key, default_key):
        if tok not in dateDict.keys():
            dateDict[tok] = time.strftime(cur)

    start_date_str = dateDict['YEAR'] + \
                     dateDict['MONTH'] + \
                     dateDict['DAY'] + \
                     dateDict['HOUR'] + \
                     dateDict['MINUTE']

    start_date = datetime.datetime.strptime(start_date_str, ''.join(default_key))
    end_date = start_date + datetime.timedelta(hours=duration)

    start_date_str = datetime.datetime.strftime(start_date, '%Y%m%dT%H%M%S')
    end_date_str = datetime.datetime.strftime(end_date, '%Y%m%dT%H%M%S')

    check_text = '### CHECK ###\n{}년 {}월 {}일 {}시 {}분 이벤트\n {}'.format(
        dateDict['YEAR'],
        dateDict['MONTH'],
        dateDict['DAY'],
        dateDict['HOUR'],
        dateDict['MINUTE'],
        desc
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
PRODID:Product by Jongwon
BEGIN:VEVENT
UID:{}
DTSTAMP:{}
DTSTART:{}
DTEND:{}
LOCATION:{}
SUMMARY:{}
DESCRIPTION:{}
BEGIN: VALARM
TRIGGER: -PT{}M
DESCRIPTION:{}
END:VALARM
END:VEVENT
END:VCALLENDAR
""".format(
        uid,
        time.strftime('%Y%m%dT%H%M%S'),
        end_date_str,
        start_date_str,
        location,
        title,
        desc,
        alarm*60,
        desc
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
