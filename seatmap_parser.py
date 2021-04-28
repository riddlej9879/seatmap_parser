from xml.dom import minidom
from file_parser import *
import simplejson as json
import requests


dom1 = minidom.parse('seatmap1.xml')
dom2 = minidom.parse('seatmap2.xml')


f = open('data1.json', 'w')
f.write(json.dumps(parse_element(dom1), sort_keys=True, indent=4))
f.close()

f = open('data2.json', 'w')
f.write(json.dumps(parse_element(dom2), sort_keys=True, indent=4))
f.close()
