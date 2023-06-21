from sqlalchemy import create_engine,text
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()

configure()

engine = create_engine(os.getenv('db_connect'),
                       connect_args={
                        "ssl": {
                                 "ssl_ca": "/etc/ssl/cert.pem"
                                }
                        }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        jobs = []

        for row in result.all():
            jobs.append(row._asdict())
        return jobs