#import sys
#import os
import random
import string
import pythonwhois
#im refraining to linking the twitter feed or the link to malware ill leave thatas an exercise for you
# uncompyle6 version 2.11.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Apr 12 2019, 15:32:40) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.46.3)]
# Embedded file name: redkeeper.py 
# Compiled at: 2018-09-20 11:31:08
# requests.get('https://bit.ly/2Zlmmzb') -> tracking image as well to monitor loads ?

#wtf so lets make a killswitch that generates a single ascii char  uber malware here ;)
def gen_switches():
    switches = []
    for i in range(26):
        kill_switch = 'iuqerfsodp9ifjaposdfjhgosurijfaewrwergwe' + random.choice(string.ascii_lowercase) + '.com'
        print(kill_switch)
        switches.append(kill_switch)
    return switches


registerd_switches = []
killswitch_domains = gen_switches()
for dom in killswitch_domains:
    details = pythonwhois.get_whois(dom)
    if details:
       try:
          print(details['contacts']['registrant'])
          local_info = {'domain':dom,'whois_info':details['contacts']['registrant']}
          registerd_switches.append(local_info)
          
       except:
          pass


for info in registerd_switches:
    print(info)
