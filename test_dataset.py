from sqlalchemy import Column, Float
from sqlalchemy.ext.declarative import declarative_base

TestBase = declarative_base()

class TestDataset(TestBase):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'test'
    #tell SQLAlchemy the name of column and its attributes:
    X = Column(Float) 
    Y = Column(Float)
    Delta_Y = Column(Float)
    Y_Deviation = Column(Float, primary_key=True)
    