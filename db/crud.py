from db.models import Base, JobRecommendation, JobRequest
from . import session


class JobRequestCrud:
    def __init__(self):
        pass

    @classmethod
    def add_jobrequest(cls):  # , **kwargs
        job_request = JobRequest()
        session.add(job_request)
        session.commit()
        session.close()
        return
