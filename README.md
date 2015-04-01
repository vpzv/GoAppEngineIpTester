## Go agent IP test tool
Testing available IPs for Google app engine / GoAgent


Note: [`iplist.txt`](iplist.txt) is from https://github.com/justjavac/Google-IPs. Thank you @justjavac!

### Feature:
* Test all IPs in "iplist.txt"
* Analyze most fast IPs
* Auto update "proxy.ini" if it exists in the same folder. (Automatically backup before updating)

### Installation:
1. Copy 4 files ([`file_utils.py`](file_utils.py), [`iplist.txt`](iplist.txt), [`test_connections.py`](test_connections.py), [`update_ips.py`](update_ips.py)) to &lt;go agent home folder>/local/
2. Run [`update_ips.py`](update_ips.py) in command line. The configurations will be changed to


 ```
 google_cn = <new ip>
 google_hk = <new ip>
 google_talk = <new ip>
 ```


3. Restart GoAgent


Note: If you delete yyyy-MM-dd_connect_result.csv file, the ips will be tested again by running [`update_ips.py`](update_ips.py).
