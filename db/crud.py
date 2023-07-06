from db.models import Base, JobRecommendation, JobRequest
from sqlalchemy import select, delete
from db import engine, crud


class JobRequestCrud:

    @classmethod
    @crud(is_commit=True, custom_error_msg='')
    def get_jobrequest(cls, **kwargs):  #
        cmd = select(cls.job_request)
        # session.add(job_request)
        # session.commit()
        # session.close()
        return engine.excute(cmd).fetchall()


jr = JobRequestCrud.get_jobrequest()
print(jr)
