import requests
import os
import json
from pprint import pprint

class liepin_suggestList(object):
	"""docstring for liepin_suggestList"""
	def __init__(self):
		super(liepin_suggestList, self).__init__()
		# self.arg = arg
		self.url='http://apic.liepin.com/api/com.liepin.searchfront4c.pc-search-suggest-list?keyword=中药'#%E5%B5%8C%E5%85%A5%E5%BC%8F
		self.headers={
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
			'Accept': 'application/json, text/plain, */*',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			'X-Fscp-Version': '1.1',
			'X-Requested-With': 'XMLHttpRequest',
			'X-Fscp-Std-Info': '{"client_id": "40108"}',
			'X-Fscp-Trace-Id': '5deb30cd-7dfa-4839-a915-dde7495cf966',
			'X-Client-Type': 'web',
			'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/"}',

		}
		self.s=requests.session()

	def access_mainpage(self):
		r=self.s.get('http://ips.chacuo.net')
		print(r.cookies)

	def download_suggestList(self):
		r=self.s.get(self.url,headers=self.headers)
		print(r.status_code)
		print(r.text)
		# print(r.cookies)

class liepin_searchjob(object):
	"""docstring for liepin_searchjob"""
	def __init__(self):
		super(liepin_searchjob, self).__init__()
		# self.arg = arg
		self.url='https://apic.liepin.com/api/com.liepin.searchfront4c.pc-search-job'#%E5%B5%8C%E5%85%A5%E5%BC%8F
		self.X_Fscp_Std_Info={"client_id": "40108"}
		self.headers={
			'X-Fscp-Version': '1.1',
			'X-Fscp-Std-Info':json.dumps(self.X_Fscp_Std_Info),
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101  Safari/537.36',
			'X-Fscp-Bi-Stat': '{"location": ""}',
			'Content-Type': 'application/json;charset=UTF-8;',
			'X-Requested-With': 'XMLHttpRequest',
			'X-Client-Type': 'web',
			'X-Fscp-Trace-Id': 'e1929537-67e9-497a-9287-862c1af97549'
		}
		# self.s=requests.session()
		self.mainSearchPcConditionForm={'city':'410','dq':'410','currentPage':0,'key':'python','workYearCode':'0'}
		self.data={'mainSearchPcConditionForm':'%s' % self.mainSearchPcConditionForm}
		self.form_data={'data':self.data}
		self.payload={"data":{"mainSearchPcConditionForm":{"city":"410","dq":"410","currentPage":0,"pageSize":40,"key":"算法","suggestTag":"","workYearCode":"0"}}}
		# self.data={"data":json.dumps({"mainSearchPcConditionForm":json.dumps({"city":"410","dq":"410","currentPage":0,"key":"opencv"})})}
		self.proxy={
			'http':'http://127.0.0.1:7890',
			'https':'http://127.0.0.1:7890'
		}

	def download_liepin_searchjob(self):
		print(json.dumps(self.data))
		r=requests.post(self.url,headers=self.headers,json=self.payload,proxies=self.proxy)#,verify=False ,json=self.form_data
		#data="%7b%22%64%61%74%61%22%3a%7b%22%6d%61%69%6e%53%65%61%72%63%68%50%63%43%6f%6e%64%69%74%69%6f%6e%46%6f%72%6d%22%3a%7b%22%63%69%74%79%22%3a%22%34%31%30%22%2c%22%64%71%22%3a%22%34%31%30%22%2c%22%63%75%72%72%65%6e%74%50%61%67%65%22%3a%30%2c%22%70%61%67%65%53%69%7a%65%22%3a%34%30%2c%22%6b%65%79%22%3a%22%70%79%74%68%6f%6e%22%2c%22%77%6f%72%6b%59%65%61%72%43%6f%64%65%22%3a%22%30%22%7d%7d%7d",
		print(r.status_code)
		# pprint(r.text)
		result_ret=json.loads(r.text)
		jobCardList=result_ret['data']['data']['jobCardList']
		for i in jobCardList:
			dataInfo=i['dataInfo']

			job=i['job']
			job_labels=job['labels']
			job_requireEduLevel=job['requireEduLevel']
			jobId=job['jobId']
			job_refreshTime=job['refreshTime']
			jobKind=job['jobKind']
			job_title=job['title']
			job_salary=job['salary']
			job_dq=job['dq']
			topJob=job['topJob']
			job_requireWorkYears=job['requireWorkYears']
			job_link=job['link']
			job_advViewFlag=job['advViewFlag']
			job_dataPromId=job['dataPromId']

			recruiter=i['recruiter']
			recruiter_imId=recruiter['imId']
			recruiter_imUserType=recruiter['imUserType']
			recruiter_chatted=recruiter['chatted']
			recruiterName=recruiter['recruiterName']
			recruiterTitle=recruiter['recruiterTitle']
			recruiterId=recruiter['recruiterId']
			recruiterPhoto=recruiter['recruiterPhoto']

			comp=i['comp']
			compName=comp['compName']
			compId=comp['compId'] if 'compId' in comp else ''
			compScale=comp['compScale']
			compStage=comp['compStage'] if 'compStage' in comp else ''
			compLogo=comp['compLogo']
			compIndustry=comp['compIndustry']
			comp_link=comp['link']

			dataParams=i['dataParams']

			print(job_labels,job_requireEduLevel,job_title,job_salary,job_dq,job_requireWorkYears,job_link)
			print(recruiterName,recruiterTitle)
			print(compName,compScale,compStage,compIndustry,comp_link)
			print('\n')

	def 
		# print()
		# print(r.cookies)
  
if __name__ == '__main__': 
	# liepin_suggestList=liepin_suggestList()
	# liepin_suggestList.download_suggestList()

	liepin_searchjob=liepin_searchjob()
	liepin_searchjob.download_liepin_searchjob()