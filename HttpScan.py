import requests
import sys
from queue import Queue
import threading
from user_agent import user_agent_list
from optparse import OptionParser
 
class HttpScanMain:
	def __init__(self, options):
		self.url = options.url
		self.count = options.count
		
	class HttpScan(threading.Thread):
		def __init__(self, queue,total):
			threading.Thread.__init__(self)
			self._queue = queue
			self._total = total
				
		def run(self):
			while not self._queue.empty():
				url = self._queue.get()

				threading.Thread(target=self.msg).start()
 
				try:
					r = requests.get(url=url, headers=user_agent_list.get_user_agent(), timeout=8,)
					if r.status_code == 200 or r.status_code == 302:
						sys.stdout.write('\r' + '[+]%s\t\t\n' % (url))
						result = open('result.txt','a+')
						result.write(url)
						result.write('\r\n')
						result.close()
				except Exception as e:
					pass
 
		def msg(self):
			per = 100 - float(self._queue.qsize())/float(self._total) * 100
			percentage = "%s Finished| %s All| Scan in %1.f %s"%((self._total - self._queue.qsize()),self._total,per,'%')
			sys.stdout.write('\r'+'[*]'+percentage)
 
	def start(self):
		result = open('result.txt','w')
		result.close()
 
		queue = Queue()
 

		for i in range(1, 65536):
			queue.put(self.url+":"+str(i).rstrip())

		total = queue.qsize()
 
		threads = []
		thread_count = int(self.count)
 
		for i in range(thread_count):
			threads.append(self.HttpScan(queue,total))
		for i in threads:
			i.start()
		for i in threads:
			i.join()
 
if __name__ == '__main__':
 
	print ('''
 _   _ _   _         _____                 
| | | | | | |       /  ___|                
| |_| | |_| |_ _ __ \ `--.  ___ __ _ _ __  
|  _  | __| __| '_ \ `--. \/ __/ _` | '_ \ 
| | | | |_| |_| |_) /\__/ / (_| (_| | | | |
\_| |_/\__|\__| .__/\____/ \___\__,_|_| |_|
              | |                          
              |_|                         
                                                                                                             
	''')
 
	parser = OptionParser('./web_dir_scan.py -u <Target URL> [-t <Thread_count>]')
	parser.add_option('-u','--url',dest='url',type='string',help='target url for scan')
	parser.add_option('-t','--thread',dest='count',type='int',default=1000,help='scan thread_count,default=1000')
	(options,args)=parser.parse_args()
 
	if options.url :
		HttpScan = HttpScanMain(options)
		HttpScan.start()
		sys.exit(1)
	else:
		parser.print_help()
		sys.exit(1)


