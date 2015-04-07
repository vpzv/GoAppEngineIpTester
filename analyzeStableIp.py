__author__ = 'Howard'

import csv
import sys
import time
import statistics
import os

import test_connections as test


if not sys.argv or len(sys.argv) < 2:
    print('Please specify file to analyze')
    exit()

if not os.path.isfile(sys.argv[1]):
    print("Please specify correct file name in current folder")

file_to_analyze = sys.argv[1]

read_data = csv.reader(open(file_to_analyze, 'r'))
data = []
for row in read_data:
    data.append(row)
Header = data[0]
data.pop(0)

data.sort(key=lambda r: float(r[1]))

allIpConnections = []
for ipData in data[:30]:
    print('Testing ' + ipData[0])
    ipConnections = [ipData[0]]
    for i in range(1, 10):
        cost_time = test.check_ip_available(ipData[0])
        ipConnections.append(cost_time)
        print("%d --> %.5f" % (i, float(cost_time)))
        time.sleep(1)
    ipConnections.append(statistics.variance(ipConnections[1:]))
    allIpConnections.append(ipConnections)

allIpConnections.sort(key=lambda r: float(r[-1]))

print(allIpConnections)
print('|'.join('{}'.format(k[1][0]) for k in enumerate(allIpConnections)))

with open("Analyze_" + file_to_analyze, 'a') as csvFile:
    spam_writer = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spam_writer.writerow(allIpConnections)


