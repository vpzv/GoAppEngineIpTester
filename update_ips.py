__author__ = 'Howard'

import csv
import os
import time
import test_connections as test
import file_utils
import shutil

RESULT_FILE_PATH = time.strftime("%Y-%m-%d") + "_connect_result.csv"
PROXY_INI_FILE = 'proxy.ini'
PROXY_INI_BACKUP_FILE = 'proxy.ini.bak'

if not os.path.isfile(RESULT_FILE_PATH):
    print('No test result found. Now testing...')
    test.test_connection()
else:
    print('Use ' + RESULT_FILE_PATH + ' to get the fast ips')

read_data = csv.reader(open(RESULT_FILE_PATH, 'r'))
data = []
for row in read_data:
    data.append(row)
Header = data[0]
data.pop(0)

data.sort(key=lambda r: float(r[1]))

if not data:
    print('No ip has been found available, please set MAX_TIME_OUT(test_connections.py) larger value(time out per ip testing in seconds).')
    exit()

best_ips = ''
for conn_row in data[:20]:
    best_ips += conn_row[0] + '|'


print('\nThe best ips are: ')
print(best_ips[:-1])

if not os.path.isfile(PROXY_INI_FILE):
    print('\nWarn: If running under the same folder with "%s", "%s" will be automatically updated' % (PROXY_INI_FILE, PROXY_INI_FILE))
    exit()

# Backup proxy.ini
if not os.path.isfile(PROXY_INI_BACKUP_FILE):
    shutil.copy2(PROXY_INI_FILE, PROXY_INI_BACKUP_FILE)
    print('\nBacked up "%s" to "%s"' % (PROXY_INI_FILE, PROXY_INI_BACKUP_FILE))

file_utils.replace(PROXY_INI_FILE, r'^google_cn\s=\s.*$', 'google_cn = ' + best_ips[:-1])
file_utils.replace(PROXY_INI_FILE, r'^google_hk\s=\s.*$', 'google_hk = ' + best_ips[:-1])
file_utils.replace(PROXY_INI_FILE, r'^google_talk\s=\s.*$', 'google_talk = ' + best_ips[:-1])
print('\nSuccessfully updated "proxy.ini" with best ips! Please restart GoAgent.')