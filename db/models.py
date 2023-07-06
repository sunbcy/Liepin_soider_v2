from sqlalchemy import (MetaData, Table, Column, Integer, String, Float, Boolean, DECIMAL, Enum, Date,
                        DateTime, Time, Text, ForeignKey, UniqueConstraint, Index)
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy.sql import func



# 建工作需求单
class JobRequest(Base):
    __tablename__ = 'job_request'
    id = Column(Integer(), primary_key=True)  # autoincrement=True, index=True, nullable=False, unique=True, default=18
    username = Column(String(32), index=True)
    usermail = Column(String(50))
    city = Column(String(32))
    dq = Column(String(32))
    pubTime = Column(String(50))
    currentPage = Column(Integer)
    pageSize = Column(Integer)
    Key = Column(String(32))
    suggestTag = Column(String(50))
    workYearCode = Column(String(10))
    compId = Column(String(20))
    compName = Column(String(50))
    compTag = Column(String(32))
    industry = Column(String(50))
    salary = Column(String(10))
    jobKind = Column(String(5))
    compScale = Column(String(32))
    compKind = Column(String(32))
    compStage = Column(String(32))
    eduLevel = Column(String(32))
    ctime = Column(DateTime(timezone=True), server_default=func.now())
    mtime = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('id', 'username', name='uix_id_username'),
    )


# 建工作推荐表
class JobRecommendation(Base):
    __tablename__ = 'job_recommendation'
    id = Column(Integer, primary_key=True)
    dataInfo = Column(String(256))
    dataParams = Column(Text)
    job_title = Column(String(50))
    job_salary = Column(String(10))
    job_dq = Column(String(20))
    job_requireWorkYears = Column(String(10))
    job_requireEduLevel = Column(String(32))
    job_labels = Column(String(50))
    job_link = Column(String(256))

    jobId = Column(Integer, unique=True)
    topJob = Column(String(10))
    job_advViewFlag = Column(String(10))
    job_dataPromId = Column(String(100))

    recruiterName = Column(String(10))
    recruiterTitle = Column(String(10))

    recruiter_imId = Column(String(32))
    recruiter_imUserType = Column(String(5))
    recruiter_chatted = Column(String(5))
    recruiterId = Column(String(32))
    recruiterPhoto = Column(String(50))

    compId = Column(Integer)
    compName = Column(String(50))
    compScale = Column(String(10))
    compStage = Column(String(10))
    compIndustry = Column(String(20))

    compLogo = Column(String(50))
    comp_link = Column(String(256))

    job_intro_content = Column(Text())
    jobKind = Column(String(10))
    job_refreshTime = Column(String(20))
    job_origin = Column(String(10))
    push_flag = Column(String(10), default='false')

    username = Column(String(20))
    usermail = Column(String(50))

    utime = Column(DateTime(timezone=True), server_default=func.now())
    mtime = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('id', 'jobId', name='uix_id_jobId'),
    )
