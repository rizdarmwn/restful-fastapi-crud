from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

SQLALCHEMY_DATABASE_URL = "postgres://vbsmuagcjvrvne:87f76cb0a5fea312f4f4ccf81b23be4e402375db2f02badddf01e1a7de57d32e@ec2-54-159-175-113.compute-1.amazonaws.com:5432/d9di600ehr99n0"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
