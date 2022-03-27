import argparse
import json
import os
import subprocess
from collections import Counter, OrderedDict
from datetime import datetime

parser = argparse.ArgumentParser(description='Process access.log')
parser.add_argument("-path", default="/home/al/PycharmProjects/OTUS/otus_project/nine_homework/logs/")
parser_args = parser.parse_args()
FILE_DIR = parser_args.path
FILE_EXE = r".log"
ALL_FILES = [_ for _ in os.listdir(FILE_DIR) if _.endswith(FILE_EXE)]

REQUEST_COUNTER = {}
IP_LIST = []
LONG_REQUEST = {}


def read_log():
	for file in ALL_FILES:
		ALL_REQUESTS = 0
		with open(f"{FILE_DIR}{file}") as f:
			for _ in f:
				data = f.readline()
				if not data:
					break
				else:
					ALL_REQUESTS += 1
					ip_list = data.split()[0]
					IP_LIST.append(ip_list)
					long_req_key = data.split()[-1]
					LONG_REQUEST[data] = long_req_key
		
		for request in ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]:
			res = subprocess.run([f"grep -c '{request} ' {FILE_DIR}{file}"], shell=True, capture_output=True)
			value = res.stdout.decode('utf-8').strip("\n")
			REQUEST_COUNTER[value] = request
	
	most_common = Counter(IP_LIST).most_common(3)
	l = []
	for i in most_common:
		l.append(i[0])
	
	item = OrderedDict(sorted(LONG_REQUEST.items(), key=lambda x: int(x[1])))
	long_req = list(item)[-3:]
	
	filename = datetime.now().strftime('%d-%m-%Y-%H:%M.json')
	
	all_dict = {'Отчёт':
		[{
			'Общее количество выполненных запросов': f"{ALL_REQUESTS}",
			'Количество запросов по HTTP-методам': f"{REQUEST_COUNTER}",
			'Топ 3 IP адресов': f"{l}",
			'Топ 3 самых долгих запросов': f"{long_req}",
		}]
	}
	
	with open(filename, 'w', encoding="utf-8") as file:
		json.dump(all_dict, file, ensure_ascii=False, indent=4)
	
	print(all_dict)


if __name__ == "__main__":
	read_log()
