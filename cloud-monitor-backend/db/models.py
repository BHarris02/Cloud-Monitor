from sqlalchemy import Column, Integer, Float, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from config import DATABASE_URI

Base = declarative_base()

class Metrics(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    cpu_usage = Column(Float)
    mem_usage = Column(Float)
    disk_usage = Column(Float)

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)