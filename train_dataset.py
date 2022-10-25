from sqlalchemy import Column, Float
from sqlalchemy.ext.declarative import declarative_base

TrainBase = declarative_base()

class TrainDataset(TrainBase):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'train'
    #tell SQLAlchemy the name of column and its attributes:
    X = Column(Float, primary_key=True) 
    Y1 = Column(Float)
    Y2 = Column(Float)
    Y3 = Column(Float)
    Y4 = Column(Float)