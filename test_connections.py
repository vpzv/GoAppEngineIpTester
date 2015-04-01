__author__ = 'Howard'

import csv
import time
import os
import sys
import httplib

MAX_TIME_OUT = 1
RESULT_FILE_PATH = time.strftime("%Y-%m-%d") + "_connect_result.csv"
IP_SOURCE_FILE = 'iplist.txt'


def check_ip_available(test_ip):
    conn = httplib.HTTPSConnection(test_ip, timeout=MAX_TIME_OUT)
    try:
        start = time.time()
        conn.request("GET", "/")
        if conn.getresponse().status == 200:
            return time.time() - start
        else:
            return 999999
    except Exception:
        return 999999
    finally:
        conn.close()


def write_result(_ip, _time):
    with open(RESULT_FILE_PATH, 'a') as csvFile:
        spam_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spam_writer.writerow([_ip, _time])


def test_connection():
    if os.path.isfile(RESULT_FILE_PATH):
        os.remove(RESULT_FILE_PATH)
    total_line_num = sum(1 for line in open(IP_SOURCE_FILE))
    with open(IP_SOURCE_FILE, "r") as ins:
        for line_num, line_text in enumerate(ins):
            sys.stdout.write('\r')
            sys.stdout.write('Testing connections... %.2f%%(%d/%d)' % (float(line_num) / total_line_num * 100, line_num, total_line_num))
            sys.stdout.flush()
            if not line_text or not line_text.strip(' \t\n\r'):
                continue
            elif line_text.startswith('Country:'):
                sys.stdout.write('\nStart testing ' + line_text.strip(' \t\n\r') + '\n')
            else:
                ip = line_text.strip(' \t\n\r')
                connect_time = check_ip_available(ip)
                if connect_time <= MAX_TIME_OUT:
                    write_result(ip, connect_time)
