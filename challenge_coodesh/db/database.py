from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://pgxdmopnfgypeb:47a47dfd40d363698ecd938e80eecbce5c83101ff607e7cdc29ad5f3529a5aea@ec2-44-193-188-118.compute-1.amazonaws.com/d9nqc80d3a42ha"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()
