import requests
import os
import json
from pprint import pprint
from lxml import etree
from QiYeWeChat_Bot import QiyeWeChat_Bot
from sendmail import MailSender

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
		self.payload={"data":{"mainSearchPcConditionForm":{"city":"410","dq":"410","currentPage":0,"pageSize":40,"key":"亚马逊运营","suggestTag":"","workYearCode":"1$3"}}}

		self.self_payload={"data":{"mainSearchPcConditionForm":{"city":"050090","dq":"050090","currentPage":0,"pageSize":40,"key":"爬虫","suggestTag":"","workYearCode":"1$3","salary":"10$20","jobKind":"2","compScale":"080","compKind":"","eduLevel":"040"}}}
		"""
		{"data":{"mainSearchPcConditionForm":{"city":"410","dq":"410","pubTime":"","currentPage":0,"pageSize":40,"key":"后端","suggestTag":"","workYearCode":"0","compId":"","compName":"","compTag":"","industry":"","salary":"","jobKind":"","compScale":"","compKind":"","compStage":"","eduLevel":""},"passThroughForm":{"scene":"input","skId":"","fkId":"","ckId":"e4fddwg1v6j8attv8uflv2cdyj1pazv8","suggest":null}}}
  
		city  "410"-全国 "050090"-深圳
		dq "410"-全国 "050090"-深圳 "050090030"-南山区 "050090020"-福田区
		pubTime ""-不限 "7"-一周以内 "30"-一月以内
		currentPage 0-首页
  		pageSize 40-总页
		key ""-搜索关键词
		suggestTag ""-无
		workYearCode "0"-不限  "1"-应届生 "2"-实习生 "0$1"-一年以内 "1$3"-1-3年 "3$5"-3-5年 "5$10"-5-10年 "10$999"-10年以上
		compId ""-无
		compName ""-无
		compTag ""-无 "qua_0001"-高新技术企业 "qua_0004"-财富中国500强 "qua_0009"-创新企业100强 
		industry ""-无 "H01$H01"-IT/互联网/游戏$不限 "H01$H0001"-IT/互联网/游戏$游戏  "H02$H0018"-电子/通信/半导体$电子/半导体/集成电路 
		salary ""-无 "0$3"-3K以下 3K-5K 5K-10K "10$20"-10K-20K 20K-40K 40K-60K "60$999"-60K以上 自定义
		jobKind ""-无 "1"-猎头职位 "2"-企业职位
		compScale ""-无 "010"-1-49人 "020"-50-99人 "030"-100-499人 "040"-500-999人 "050"-1000-2000人 "060"-2000-5000人 "070"-5000-10000人 "080"-10000人以上
		compKind ""-无 "010"-外商独资.外企办事处 "050"-国内上市公司
		compStage ""-无 "01"-天使轮 "02"-A轮 "03"-B轮 "04"-C轮 "05"-D轮及以上 "06"-已上市 "07"-战略融资 "08"-融资未公开 "99"-其他
		eduLevel ""-无 "010"-博士 "020"-MBA/EMBA "030"-硕士 "040"-本科 "050"-大专 "060"-中专/中技 "080"-高中 "090"-初中及以下 
  		"""
		# self.data={"data":json.dumps({"mainSearchPcConditionForm":json.dumps({"city":"410","dq":"410","currentPage":0,"key":"opencv"})})}
		self.proxy={
			'http':'http://127.0.0.1:7890',
			'https':'http://127.0.0.1:7890'
		}

	def get_job_detail_infos(self,job_link):
		print('【访问】 {job_link}'.format(job_link=job_link))
		r=requests.get(job_link,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'})
		r.encoding=r.apparent_encoding
		html=etree.HTML(r.text)
		web_title=html.xpath('//head/title/text()')[0]
		job_id=job_link.split('/')[-1].split('.')[0]
		job_title=html.xpath('//div[@class="job-apply-content"]//span[@class="name ellipsis-1"]/text()')[0]
		job_salary=html.xpath('//div[@class="job-apply-content"]//span[@class="salary"]/text()')[0]
		job_properties=html.xpath('//div[@class="job-apply-content"]//div[@class="job-properties"]/span/text()')
		company_url=html.xpath('//main//content//div[@class="title-box"]//span/a/@href')[0]
		company_id=company_url.split('/')[-2]
		job_intro_tag=html.xpath('//main//content//section[@class="job-intro-container"]//ul/li/text()')
		job_tags=str(tuple(job_properties+job_intro_tag))
		job_intro_content=html.xpath('//main//content//dd[@data-selector="job-intro-content"]//text()')[0]
		try:
			company_intro=html.xpath('//main//content//section[@class="company-intro-container"]//div[@class="inner ellipsis-3"]/text()')[0]
		except IndexError as e:
			company_intro=html.xpath('//main//content//section[@class="company-intro-container"]//div[@class="inner ellipsis-3"]/text()')
			if (not company_intro):
				company_intro=''
			print(f"company_intro为{company_intro}")
		# print(web_title)
		# # print(job_id)
		# print(job_title)
		# print(job_salary)
		# print(job_tags)
		# print(job_intro_content)#岗位职责/职位要求
		# print(company_intro)#公司简介
		return (job_tags,job_intro_content)
		# quit()

	def download_liepin_searchjob(self):
		ALL_JOB_STR_QIYE_WECHAT=''
		ALL_JOB_STR_MAIL=''
		JOB_NUM=3
		JOB_COUNT=0
		# print(json.dumps(self.data))
		r=requests.post(self.url,headers=self.headers,json=self.self_payload,proxies=self.proxy)#,verify=False ,json=self.form_data
		#data="%7b%22%64%61%74%61%22%3a%7b%22%6d%61%69%6e%53%65%61%72%63%68%50%63%43%6f%6e%64%69%74%69%6f%6e%46%6f%72%6d%22%3a%7b%22%63%69%74%79%22%3a%22%34%31%30%22%2c%22%64%71%22%3a%22%34%31%30%22%2c%22%63%75%72%72%65%6e%74%50%61%67%65%22%3a%30%2c%22%70%61%67%65%53%69%7a%65%22%3a%34%30%2c%22%6b%65%79%22%3a%22%70%79%74%68%6f%6e%22%2c%22%77%6f%72%6b%59%65%61%72%43%6f%64%65%22%3a%22%30%22%7d%7d%7d",
		print("<{status_code}>".format(status_code=r.status_code))
		# pprint(r.text)
		result_ret=json.loads(r.text)
		jobCardList=result_ret['data']['data']['jobCardList']
		for i in jobCardList:
			JOB_STR=""""""
			dataInfo=i['dataInfo']
			job=i['job']
			job_labels=job['labels']
			job_requireEduLevel=job['requireEduLevel']
			jobId=job['jobId']
			job_refreshTime=job['refreshTime']
			jobKind='猎头职位' if job['jobKind']=='1' else '企业职位'
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
			compStage=comp['compStage'] if 'compStage' in comp else '无'
			compLogo=comp['compLogo']
			compIndustry=comp['compIndustry']
			comp_link=comp['link']

			dataParams=i['dataParams']

			# print(job_labels,job_requireEduLevel,job_refreshTime,jobKind,job_title,job_salary,job_dq,job_requireWorkYears,job_link)
			
			# print(jobKind,job_refreshTime)
			# print(recruiterName,recruiterTitle)
			# print(compName,compScale,compStage,compIndustry,comp_link)
			job_tags,job_intro_content=self.get_job_detail_infos(job_link)
			JOB_STR_QIYE_WECHAT="""【{job_title} {job_salary}】\n{recruiterName} {recruiterTitle}\n{compName} {compScale} {compStage} {compIndustry}\n{jobKind} 发布时间:{job_refreshTime}\n{job_dq} {job_requireWorkYears} {job_requireEduLevel} {job_labels} \n\n{job_intro_content}\n\n""".format(job_title=job_title,job_salary=job_salary,job_dq=job_dq,job_requireWorkYears=job_requireWorkYears,job_requireEduLevel=job_requireEduLevel,job_labels=job_labels,recruiterName=recruiterName,recruiterTitle=recruiterTitle,compName=compName,compScale=compScale,compStage=compStage,compIndustry=compIndustry,job_intro_content=job_intro_content,jobKind=jobKind,job_refreshTime=job_refreshTime)
			JOB_STR_MAIL="""【{job_title} {job_salary}】<br>{recruiterName} {recruiterTitle}<br>{compName} {compScale} {compStage} {compIndustry}<br>{jobKind} 发布时间:{job_refreshTime}<br>{job_dq} {job_requireWorkYears} {job_requireEduLevel} {job_labels} <br><br>{job_intro_content}<br><br>""".format(job_title=job_title,job_salary=job_salary,job_dq=job_dq,job_requireWorkYears=job_requireWorkYears,job_requireEduLevel=job_requireEduLevel,job_labels=job_labels,recruiterName=recruiterName,recruiterTitle=recruiterTitle,compName=compName,compScale=compScale,compStage=compStage,compIndustry=compIndustry,job_intro_content=job_intro_content,jobKind=jobKind,job_refreshTime=job_refreshTime)
			print(JOB_STR_QIYE_WECHAT)
			ALL_JOB_STR_QIYE_WECHAT+=JOB_STR_QIYE_WECHAT
			ALL_JOB_STR_MAIL+=JOB_STR_MAIL
			JOB_COUNT+=1
			if JOB_COUNT==JOB_NUM:
				Bot_1.send_text(ALL_JOB_STR_QIYE_WECHAT)
				mailsender.sendMail('MacBot',['saintbcy@163.com'],[],'【个人职位推荐x3】',mailsender.content(ALL_JOB_STR_MAIL))
				quit()
			else:
				pass
			# quit()

	
		# print()
		# print(r.cookies)
  
if __name__ == '__main__': 
	# liepin_suggestList=liepin_suggestList()
	# liepin_suggestList.download_suggestList()
	Bot_1=QiyeWeChat_Bot()
	mailsender=MailSender()
	liepin_searchjob=liepin_searchjob()
	liepin_searchjob.download_liepin_searchjob()