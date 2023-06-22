from sqlalchemy import create_engine,text

db_connect = 'mysql+pymysql://sa6ji2nrxyecqki7po5g:pscale_pw_b7w7pCdqqzLghNXbE1yKQaheUX3yj5IFfl9lrTilt3d@aws.connect.psdb.cloud/careereasy?charset=utf8mb4'

engine = create_engine(db_connect,
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