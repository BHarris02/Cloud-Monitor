from sqlalchemy import Column, Integer, Float, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Metrics(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    cpu_usage = Column(Float)
    mem_usage = Column(Float)
    disk_usage = Column(Float)

db_url = "mysql+mysqlconnector://admin:password@localhost/cloudmonitor"
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)