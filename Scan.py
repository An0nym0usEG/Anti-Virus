import requests
import os
import time
import sys
import hashlib, pefile
from random import randint

key = '79a0a3f5b8a1883c38eaa16991e960ac84953879e181b1c3e674e8ac25e3ad16'
output = '%s-log.txt'%randint(0, 999999)
allFiles = []
BUF_SIZE = 65536
md5 = hashlib.md5()

print('''
             ,----------------,              ,---------,
        ,-----------------------,          ,"        ,"|
      ,"                      ,"|        ,"        ,"  |
     +-----------------------+  |      ,"        ,"    |
     |  .-----------------.  |  |     +---------+      |
     |  |                 |  |  |     | -==----'|      |
     |  |                 |  |  |     |         |      |
     |  |  AntiVirus.py   |  |  |/----|`---=    |      |
     |  |                 |  |  |   ,/|==== ooo |      ;
     |  |                 |  |  |  // |(((( [33]|    ,"
     |  `-----------------'  |," .;'| |((((     |  ,"
     +-----------------------+  ;;  | |         |,"
        /_)______________(_/  //'   | +---------+
   ___________________________/___  `,
  /  oooooooooooooooo  .o.  oooo /,   \,"-----------
 / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
/_==__==========__==_ooo__ooo=_/'   /___________,"
`-----------------------------|

\n\n''')

def arquivos():
        allFiles = []
        for root, subfiles, files in os.walk('C:\\Users'):
                for names in files:
                        allFiles.append(os.path.join(root, names))
 
        return allFiles


def VT_Request(hash, key, output, diritems):
	params = {'apikey': key, 'resource': hash}
	url = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params)
	json_response = url.json()

	response = int(json_response.get('response_code'))

	if response == 0:
		'''
		print('(%s - %s) is not in Virus Total'%(hash, diritems))
		file = open(output,'a')
		file.write('(%s-%s) is not in Virus Total'%(hash, diritems))
		file.write('\n')
		file.close()
		'''
		pass

	elif response == 1:

		positives = int(json_response.get('positives'))
		if positives == 0:

			print('[==>] Found File:\n(%s - %s) is not malicious'%(hash, diritems))
			'''
			file = open(output,'a')
			file.write('%s-%s) is not malicious'%(hash, diritems))
			file.write('\n')
			file.close()
			'''
			pass

		else:
			print('[==>] Found File:\n(%s - %s) is malicious'%(hash, diritems))
			file = open(output,'a')
			file.write('(%s-%s) is malicious, Result: %s'%(hash, diritems, json_response['scans']['Kaspersky']['result']))
			file.write('\n')
			file.close()
	else:
		print(hash + 'could not be searched. Please try again later.')

def open_file():
	files = arquivos()
	#print(files)
	for items in files:
		if os.path.isfile(items) == True:
			size = len(items)
			sub_name = size-4

			if items[sub_name:] == '.exe':
				try:
					with open(items, 'rb') as f:
						data = f.read(BUF_SIZE)
						md5.update(data)
						f.close()
					md = "{0}".format(md5.hexdigest())
					try:
						VT_Request(md, key, output, items)
					except:
						pass
				except:
					pass

			elif items[sub_name:] == '.dll':
				try:
					with open(items, 'rb') as f:
						data = f.read(BUF_SIZE)
						md5.update(data)
						f.close()
					md = "{0}".format(md5.hexdigest())
					try:
						VT_Request(md, key, output, items)
					except:
						pass
				except:
					pass

			elif items[sub_name:] == '.bat':
				try:
					with open(items, 'rb') as f:
						data = f.read(BUF_SIZE)
						md5.update(data)
						f.close()
					md = "{0}".format(md5.hexdigest())
					try:
						VT_Request(md, key, output, items)
					except:
						pass
				except:
					pass

			elif items[sub_name:] == '.vbs':
				try:
					with open(items, 'rb') as f:
						data = f.read(BUF_SIZE)
						md5.update(data)
						f.close()
					md = "{0}".format(md5.hexdigest())
					try:
						VT_Request(md, key, output, items)
					except:
						pass
				except:
					pass
			else:
				pass
open_file()
