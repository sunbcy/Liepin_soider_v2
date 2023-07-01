import requests
import os
import time
import json
from pprint import pprint
from lxml import etree
from QiYeWeChat_Bot import QiyeWeChatBot
from sendmail import MailSender, content

from Connect_MySQL import Job_Request, Job_Recommendation
from conf import admin_mail, test_recv_mail


class LiepinSuggestList:
    """docstring for LiepinSuggestList"""

    def __init__(self):
        super(LiepinSuggestList, self).__init__()
        self.url = 'http://apic.liepin.com/api/com.liepin.\
        searchfront4c.pc-search-suggest-list?keyword=中药'  # %E5%B5%8C%E5%85%A5%E5%BC%8F
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
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
        self.s = requests.session()

    def download_suggestlist(self):  # 搜索关键字得到的关联词
        r = self.s.get(self.url, headers=self.headers)
        print(r.status_code)
        print(r.text)


def get_job_detail_infos(job_link):
    print('【访问】 {job_link}'.format(job_link=job_link))
    r = requests.get(job_link, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'})
    r.encoding = r.apparent_encoding
    html = etree.HTML(r.text)
    try:
        web_title = html.xpath('//head/title/text()')[0]
        job_id = job_link.split('/')[-1].split('.')[0]
        job_title = html.xpath('//div[@class="job-apply-content"]//span[@class="name ellipsis-1"]/text()')[0]
        job_salary = html.xpath('//div[@class="job-apply-content"]//span[@class="salary"]/text()')[0]
        job_properties = html.xpath('//div[@class="job-apply-content"]//div[@class="job-properties"]/span/text()')
        company_url = html.xpath('//main//content//div[@class="title-box"]//span/a/@href')[0]
        company_id = company_url.split('/')[-2]
        job_intro_tag = html.xpath('//main//content//section[@class="job-intro-container"]//ul/li/text()')
        job_tags = str(tuple(job_properties + job_intro_tag))
    except:
        job_tags = ''
    try:
        job_intro_content = html.xpath('//main//content//dd[@data-selector="job-intro-content"]//text()')[0]
    except IndexError:
        job_intro_content = ''
        print('Index Error !!!!!估计被猎聘安全中心发现了!!!!!!quit~~')
        quit()
    try:
        company_intro = html.xpath(
            '//main//content//section[@class="company-intro-container"]//div[@class="inner ellipsis-3"]/text()')[0]
    except IndexError :
        company_intro = html.xpath(
            '//main//content//section[@class="company-intro-container"]//div[@class="inner ellipsis-3"]/text()')
        if not company_intro:
            company_intro = ''
        print(f"company_intro为{company_intro}")
    # print(company_intro)  # 公司简介
    return job_tags, job_intro_content


class LiepinSearchjobs(object):
    """docstring for liepin_searchjob"""

    def __init__(self):
        super(liepin_searchjob, self).__init__()
        self.url = 'https://apic.liepin.com/api/com.liepin.searchfront4c.pc-search-job'  # %E5%B5%8C%E5%85%A5%E5%BC%8F
        self.X_Fscp_Std_Info = {"client_id": "40108"}
        self.headers = {
            'X-Fscp-Version': '1.1',
            'X-Fscp-Std-Info': json.dumps(self.X_Fscp_Std_Info),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101  Safari/537.36',
            'X-Fscp-Bi-Stat': '{"location": ""}',
            'Content-Type': 'application/json;charset=UTF-8;',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Client-Type': 'web',
            'X-Fscp-Trace-Id': 'e1929537-67e9-497a-9287-862c1af97549'
        }
        # self.s=requests.session()
        self.mainSearchPcConditionForm = {'city': '410',
                                          'dq': '410',
                                          'currentPage': 0,
                                          'key': 'python',
                                          'workYearCode': '0'}
        self.data = {'mainSearchPcConditionForm': '%s' % self.mainSearchPcConditionForm}
        self.form_data = {'data': self.data}
        # self.payload = {"data": {"mainSearchPcConditionForm": {"city": "410",
        #                                                        "dq": "410",
        #                                                        "currentPage": 0,
        #                                                        "pageSize": 40,
        #                                                        "key": "亚马逊运营",
        #                                                        "suggestTag": "",
        #                                                        "workYearCode": "1$3"}}}

        self.self_payload = {"data": {"mainSearchPcConditionForm": {"city": "050090",
                                                                    "dq": "050090",
                                                                    "currentPage": 0,
                                                                    "pageSize": 40,
                                                                    "key": "爬虫",
                                                                    "suggestTag": "",
                                                                    "workYearCode": "1$3",
                                                                    "salary": "10$20",
                                                                    "jobKind": "2",
                                                                    "compScale": "080",
                                                                    "compKind": "",
                                                                    "eduLevel": "040"}}}
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
        compScale ""-无 "010"-1-49人 "020"-50-99人 "030"-100-499人 "040"-500-999人 "050"-1000-2000人 
            "060"-2000-5000人 "070"-5000-10000人 "080"-10000人以上
        compKind ""-无 "010"-外商独资.外企办事处 "050"-国内上市公司
        compStage ""-无 "01"-天使轮 "02"-A轮 "03"-B轮 "04"-C轮 "05"-D轮及以上 "06"-已上市 "07"-战略融资 "08"-融资未公开 "99"-其他
        eduLevel ""-无 "010"-博士 "020"-MBA/EMBA "030"-硕士 "040"-本科 "050"-大专 "060"-中专/中技 "080"-高中 "090"-初中及以下 
          """
        self.proxy = {
            'http': 'http://127.0.0.1:7890',
            'https': 'http://127.0.0.1:7890'
        }

    def download_liepin_searchjob(self):
        person_count = 0
        job_requests = session.query(Job_Request).all()
        for job_request in job_requests:
            ALL_JOB_STR_QIYE_WECHAT = ''
            ALL_JOB_STR_MAIL = ''
            JOB_NUM = 2
            JOB_COUNT = 0
            send_flag = 0
            user_id, username, usermail, city, dq, pubTime, currentPage, pageSize, Key, suggestTag, workYearCode, compId, compName, compTag, industry, salary, jobKind, compScale, compKind, compStage, eduLevel, ctime, mtime = job_request.id, job_request.username, job_request.usermail, job_request.city, job_request.dq, job_request.pubTime, job_request.currentPage, job_request.pageSize, job_request.Key, job_request.suggestTag, job_request.workYearCode, job_request.compId, job_request.compName, job_request.compTag, job_request.industry, job_request.salary, job_request.jobKind, job_request.compScale, job_request.compKind, job_request.compStage, job_request.eduLevel, job_request.ctime, job_request.mtime
            # print(username,usermail,city,dq,pubTime,currentPage,pageSize,Key,suggestTag,workYearCode,compId,compName,compTag,industry,salary,jobKind,compScale,compKind,compStage,eduLevel,ctime,mtime)

            while currentPage < pageSize:
                self.self_payload = {"data": {"mainSearchPcConditionForm": {"city": city,
                                                                            "dq": dq,
                                                                            "pubTime": pubTime,
                                                                            "currentPage": currentPage,
                                                                            "pageSize": pageSize,
                                                                            "key": Key,
                                                                            "suggestTag": suggestTag,
                                                                            "workYearCode": workYearCode,
                                                                            "compId": compId,
                                                                            "compName": compName,
                                                                            "compTag": compTag,
                                                                            "industry": industry,
                                                                            "salary": salary,
                                                                            "jobKind": jobKind,
                                                                            "compScale": compScale,
                                                                            "compKind": compKind,
                                                                            "compStage": compStage,
                                                                            "eduLevel": eduLevel}}}

                r = requests.post(self.url,
                                  headers=self.headers,
                                  json=self.self_payload,
                                  timeout=3)  # ,proxies=self.proxy)#,verify=False
                time.sleep(5)
                print("<{status_code}>".format(status_code=r.status_code))
                result_ret = json.loads(r.text)
                try:
                    jobCardList = result_ret['data']['data']['jobCardList']
                except:
                    print('未获取到更多职位!')
                    JOB_COUNT += 1
                    send_flag = 1
                    Bot_1.send_text(ALL_JOB_STR_QIYE_WECHAT)
                    if usermail == test_recv_mail:  # 发给管理员
                        mailsender.sendmail('MacBot', [usermail], [], '【个人职位推荐x3】',
                                            content(ALL_JOB_STR_MAIL if ALL_JOB_STR_MAIL else '未获取到更多职位!请修改求职条件'))
                    else:  # 抄送给管理员
                        # mailsender.sendMail('MacBot',[admin_mail],[],'{user}【个人职位推荐x3】'.format(user=username),mailsender.content(ALL_JOB_STR_MAIL if ALL_JOB_STR_MAIL else '未获取到更多职位!请修改求职条件'))
                        mailsender.sendmail('MacBot', [usermail], [admin_mail],
                                            '{user}【个人职位推荐x3】'.format(user=username),
                                            content(ALL_JOB_STR_MAIL if ALL_JOB_STR_MAIL else '未获取到更多职位!请修改求职条件'))
                    # session.close()
                    break
                for i in jobCardList:
                    JOB_STR = """"""
                    dataInfo, job, recruiter, comp, dataParams = i['dataInfo'], i['job'], i['recruiter'], i['comp'], i['dataParams']

                    job_title = job['title']
                    job_salary = job['salary']
                    job_dq = job['dq']
                    job_requireWorkYears = job['requireWorkYears']
                    job_requireEduLevel = job['requireEduLevel']
                    job_labels = str(job['labels'])
                    jobId = job['jobId']
                    topJob = job['topJob']
                    job_advViewFlag = job['advViewFlag']
                    job_dataPromId = job['dataPromId']

                    recruiterName = recruiter['recruiterName']
                    recruiterTitle = recruiter['recruiterTitle']
                    recruiter_imId = recruiter['imId']
                    recruiter_imUserType = recruiter['imUserType']
                    recruiter_chatted = recruiter['chatted']
                    recruiterId = recruiter['recruiterId']
                    recruiterPhoto = recruiter['recruiterPhoto']
                    compName = comp['compName']
                    compScale = comp['compScale'] if 'compScale' in comp else '无'
                    compStage = comp['compStage'] if 'compStage' in comp else '无'
                    compLogo = comp['compLogo '] if 'compLogo' in comp else '无'
                    compIndustry = comp['compIndustry'] if 'compIndustry' in comp else '无'
                    comp_link = comp['link']

                    job_refreshTime = job['refreshTime']
                    jobKind = '猎头职位' if job['jobKind'] == '1' else '企业职位'

                    job_link = job['link']
                    compId = comp['compId'] if 'compId' in comp else ''

                    # print(job_labels,job_requireEduLevel,job_refreshTime,jobKind,job_title,job_salary,job_dq,job_requireWorkYears,job_link)
                    # print(jobKind,job_refreshTime)
                    # print(recruiterName,recruiterTitle)
                    # print(compName,compScale,compStage,compIndustry,comp_link)
                    # 抓取公司简介
                    job_tags, job_intro_content = get_job_detail_infos(job_link)
                    if job_intro_content:
                        job_origin = '猎聘'
                        job_recommendation = Job_Recommendation(dataInfo=dataInfo,
                                                                dataParams=dataParams,
                                                                job_title=job_title,
                                                                job_salary=job_salary,
                                                                job_dq=job_dq,
                                                                job_requireWorkYears=job_requireWorkYears,
                                                                job_requireEduLevel=job_requireEduLevel,
                                                                job_labels=job_labels,
                                                                job_link=job_link,
                                                                jobId=jobId,
                                                                topJob=str(topJob),
                                                                job_advViewFlag=str(job_advViewFlag),
                                                                job_dataPromId=job_dataPromId,
                                                                recruiterName=recruiterName,
                                                                recruiterTitle=recruiterTitle,
                                                                recruiter_imId=recruiter_imId,
                                                                recruiter_imUserType=recruiter_imUserType,
                                                                recruiter_chatted=str(recruiter_chatted),
                                                                recruiterId=recruiterId,
                                                                recruiterPhoto=recruiterPhoto,
                                                                compId=compId,
                                                                compName=compName,
                                                                compScale=compScale,
                                                                compStage=compStage,
                                                                compLogo=compLogo,
                                                                compIndustry=compIndustry,
                                                                comp_link=comp_link,
                                                                job_intro_content=job_intro_content,
                                                                jobKind=jobKind,
                                                                job_refreshTime=job_refreshTime,
                                                                job_origin=job_origin,
                                                                username=username,
                                                                usermail=usermail)
                        session.add(job_recommendation)
                    else:
                        print('!!!!!估计被猎聘安全中心发现了!!!!!!quit~~')
                        quit()

                    try:  # 已上传过的job就回滚
                        session.commit()
                    except Exception:
                        session.rollback()

                    # 数据库中取出此人未推送的数据项
                    unpushed_jobs = session.query(Job_Recommendation).\
                        filter(Job_Recommendation.push_flag == 'false', Job_Recommendation.username == username).first()
                    if unpushed_jobs:
                        push_id = unpushed_jobs.id
                        session.query(Job_Recommendation).filter_by(id=push_id).update(
                            {Job_Recommendation.push_flag: 'true'})
                        session.commit()

                        unpushed_job_title, unpushed_job_salary, unpushed_recruiterName, unpushed_recruiterTitle, unpushed_compName, unpushed_compScale, unpushed_compStage, unpushed_compIndustry, unpushed_jobKind, unpushed_job_refreshTime, unpushed_job_dq, unpushed_job_requireWorkYears, unpushed_job_requireEduLevel, unpushed_job_labels, unpushed_job_intro_content, unpushed_username, unpushed_usermail = unpushed_jobs.job_title, unpushed_jobs.job_salary, unpushed_jobs.recruiterName, unpushed_jobs.recruiterTitle, unpushed_jobs.compName, unpushed_jobs.compScale, unpushed_jobs.compStage, unpushed_jobs.compIndustry, unpushed_jobs.jobKind, unpushed_jobs.job_refreshTime, unpushed_jobs.job_dq, unpushed_jobs.job_requireWorkYears, unpushed_jobs.job_requireEduLevel, unpushed_jobs.job_labels, unpushed_jobs.job_intro_content, unpushed_jobs.username, unpushed_jobs.usermail
                        # print(unpushed_job_title,unpushed_job_salary,unpushed_recruiterName,unpushed_recruiterTitle,unpushed_compName,unpushed_compScale,unpushed_compStage,unpushed_compIndustry,unpushed_jobKind,unpushed_job_refreshTime,unpushed_job_dq,unpushed_job_requireWorkYears,unpushed_job_requireEduLevel,unpushed_job_labels,unpushed_job_intro_content)

                        JOB_STR_QIYE_WECHAT = """【{job_title} {job_salary}】\n{recruiterName} {recruiterTitle}\n{compName} {compScale} {compStage} {compIndustry}\n{jobKind} 发布时间:{job_refreshTime}\n{job_dq} {job_requireWorkYears} {job_requireEduLevel} {job_labels} \n\n{job_intro_content}\n\n""".format(
                            job_title=unpushed_job_title,
                            job_salary=unpushed_job_salary,
                            job_dq=unpushed_job_dq,
                            job_requireWorkYears=unpushed_job_requireWorkYears,
                            job_requireEduLevel=unpushed_job_requireEduLevel,
                            job_labels=unpushed_job_labels,
                            recruiterName=unpushed_recruiterName,
                            recruiterTitle=unpushed_recruiterTitle,
                            compName=unpushed_compName,
                            compScale=unpushed_compScale,
                            compStage=unpushed_compStage,
                            compIndustry=unpushed_compIndustry,
                            job_intro_content=unpushed_job_intro_content,
                            jobKind=unpushed_jobKind,
                            job_refreshTime=unpushed_job_refreshTime)
                        JOB_STR_MAIL = """【{job_title} {job_salary}】<br>{recruiterName} {recruiterTitle}<br>{compName} {compScale} {compStage} {compIndustry}<br>{jobKind} 发布时间:{job_refreshTime}<br>{job_dq} {job_requireWorkYears} {job_requireEduLevel} {job_labels} <br><br>{job_intro_content}<br><br>""".format(
                            job_title=unpushed_job_title,
                            job_salary=unpushed_job_salary,
                            job_dq=unpushed_job_dq,
                            job_requireWorkYears=unpushed_job_requireWorkYears,
                            job_requireEduLevel=unpushed_job_requireEduLevel,
                            job_labels=unpushed_job_labels,
                            recruiterName=unpushed_recruiterName,
                            recruiterTitle=unpushed_recruiterTitle,
                            compName=unpushed_compName,
                            compScale=unpushed_compScale,
                            compStage=unpushed_compStage,
                            compIndustry=unpushed_compIndustry,
                            job_intro_content=unpushed_job_intro_content,
                            jobKind=unpushed_jobKind,
                            job_refreshTime=unpushed_job_refreshTime)
                        print("""给用户 {username} 邮箱 {usermail} 推送以下信息:\njob_recommendations_3}""".format(
                            username=unpushed_username,
                            usermail=unpushed_usermail,
                            job_recommendations_3=JOB_STR_QIYE_WECHAT))
                        ALL_JOB_STR_QIYE_WECHAT += JOB_STR_QIYE_WECHAT
                        ALL_JOB_STR_MAIL += JOB_STR_MAIL
                        JOB_COUNT += 1
                        if JOB_COUNT == JOB_NUM:
                            send_flag = 1
                            Bot_1.send_text(ALL_JOB_STR_QIYE_WECHAT)
                            if unpushed_usermail == admin_mail:  # 抄送给自己
                                mailsender.sendmail('MacBot', [unpushed_usermail], [], '【个人职位推荐x3】',
                                                    content(ALL_JOB_STR_MAIL))
                            else:
                                # mailsender.sendMail('MacBot',[admin_mail],[],'{user}【个人职位推荐x3】'.format(user=unpushed_username),mailsender.content(ALL_JOB_STR_MAIL))
                                mailsender.sendmail('MacBot', [unpushed_usermail], [admin_mail],
                                                    '{user}【个人职位推荐x3】'.format(user=unpushed_username), content(ALL_JOB_STR_MAIL))
                            # quit()
                            break
                        else:
                            pass

                    else:  # 如果数据表中的推送完了,则会把当前payload请求中的职位都入库
                        pass

                currentPage += 1
                session.query(Job_Request).filter(Job_Request.id == user_id).update(
                    {Job_Request.currentPage: currentPage})  # 更新当前页
                session.commit()
                # break
                if send_flag:
                    break
            person_count += 1
            if person_count == len(job_requests):
                quit()


if __name__ == '__main__':
    # 初始化通知机器人
    Bot_1 = QiyeWeChatBot()
    mailsender = MailSender()


    liepin_searchjob = LiepinSearchjobs()
    liepin_searchjob.download_liepin_searchjob()

