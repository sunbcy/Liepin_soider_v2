# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, Text,ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import func

engine = create_engine("mysql+pymysql://root:passwd@127.0.0.1:3306/t1", 
                       encoding='utf-8',
                       echo=True, 
                       max_overflow=5)# 
Base = declarative_base()

# 建工作需求单
class Job_Request(Base):
    __tablename__ = 'job_request'
    id=Column(Integer, primary_key=True)#，autoincrement=True , index=True, nullable=False , unique=True  , default=18
    username=Column(String(32))
    usermail=Column(String(50))
    # userqywx=Column(String(32))
    city=Column(String(32))
    dq=Column(String(32))
    pubTime=Column(String(50))
    currentPage=Column(Integer)
    pageSize=Column(Integer)
    Key=Column(String(32))
    suggestTag=Column(String(50))
    workYearCode=Column(String(10))
    compId=Column(String(20))
    compName=Column(String(50))
    compTag=Column(String(32))
    industry=Column(String(50))
    salary=Column(String(10))
    jobKind=Column(String(5))
    compScale=Column(String(32))
    compKind=Column(String(32))
    compStage=Column(String(32))
    eduLevel=Column(String(32))
    ctime=Column(DateTime(timezone=True), server_default=func.now())
    mtime=Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
    UniqueConstraint('id', 'username', name='uix_id_username'),
    )

# 建工作推荐表
class Job_Recommendation(Base):
    __tablename__ = 'job_recommendation'
    id=Column(Integer, primary_key=True)
    dataInfo=Column(String(256))
    dataParams=Column(Text)
    job_title=Column(String(50))
    job_salary=Column(String(10))
    job_dq=Column(String(20))
    job_requireWorkYears=Column(String(10))
    job_requireEduLevel=Column(String(32))
    job_labels=Column(String(50))
    job_link=Column(String(256))
    
    jobId=Column(Integer,unique=True)
    topJob=Column(String(10))
    job_advViewFlag=Column(String(10))
    job_dataPromId=Column(String(100))
    
    recruiterName=Column(String(10))
    recruiterTitle=Column(String(10))

    recruiter_imId=Column(String(32))
    recruiter_imUserType=Column(String(5))
    recruiter_chatted=Column(String(5))
    recruiterId=Column(String(32))
    recruiterPhoto=Column(String(50))

    compId=Column(Integer)
    compName=Column(String(50))
    compScale=Column(String(10))
    compStage=Column(String(10))
    compIndustry=Column(String(20))

    compLogo=Column(String(50))
    comp_link=Column(String(256))
    
    job_intro_content=Column(Text())
    jobKind=Column(String(10))
    job_refreshTime=Column(String(20))
    job_origin=Column(String(10))
    push_flag=Column(String(10),default='false')

    username=Column(String(20))
    usermail=Column(String(50))
    
    utime=Column(DateTime(timezone=True), server_default=func.now())
    mtime=Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
    UniqueConstraint('id', 'jobId', name='uix_id_jobId'),
    )

#定义初始化数据库函数
def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__=='__main__':
    init_db()
    #创建mysql操作对象
    Session = sessionmaker(bind=engine)
    session = Session()

    # self.self_payload={"data":{"mainSearchPcConditionForm":{"city":"050090","dq":"050090","currentPage":0,"pageSize":40,"key":"爬虫","suggestTag":"","workYearCode":"1$3","salary":"10$20","jobKind":"2","compScale":"080","compKind":"","eduLevel":"040"}}}
    bcy_job_need1=Job_Request(username='bcy',usermail='saintbcy@163.com',city='050090',dq='050090',pubTime='',currentPage=0,pageSize=40,Key='爬虫',suggestTag='',workYearCode='1$3',compId='',compName='',compTag='',industry='',salary='10$20',jobKind='2',compScale='070',compKind='',compStage='',eduLevel='040')

    zanzan_job_need1=Job_Request(username='赞赞',usermail='769355987@qq.com',city='070020',dq='070020',pubTime='',currentPage=0,pageSize=40,Key='会计',suggestTag='',workYearCode='1$3',compId='',compName='',compTag='',industry='',salary='10$20',jobKind='2',compScale='080',compKind='',compStage='',eduLevel='040')
    
    session.add(bcy_job_need1)
    session.add(zanzan_job_need1)

    #提交
    session.commit()
    
    # unpushed_jobs=session.query(Job_Recommendation).filter(Job_Recommendation.push_flag=='false').first()
    # push_id=unpushed_jobs.id
    # session.query(Job_Recommendation).filter_by(id=push_id).update({Job_Recommendation.push_flag:'true'})
    # session.commit()
    # # unpushed_jobs.update({Job_Recommendation.push_flag:'true'})
    # print(unpushed_jobs.job_title)