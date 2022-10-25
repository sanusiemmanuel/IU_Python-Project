from sqlalchemy import Column, Float
from sqlalchemy.ext.declarative import declarative_base

IdealBase = declarative_base()

class IdealDataset(IdealBase):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'ideal'
    #tell SQLAlchemy the name of column and its attributes:
    X = Column(Float, primary_key=True) 
    Y1 = Column(Float); Y2 = Column(Float) 
    Y3 = Column(Float); Y4 = Column(Float); 
    Y5 = Column(Float); Y6 = Column(Float) 
    Y7 = Column(Float); Y8 = Column(Float)  
    Y9 = Column(Float); Y10 = Column(Float) 
    Y11 = Column(Float); Y12 = Column(Float)  
    Y13 = Column(Float); Y14 = Column(Float)  
    Y15 = Column(Float); Y16 = Column(Float) 
    Y17 = Column(Float) ; Y18 = Column(Float) 
    Y19 = Column(Float) ; Y20 = Column(Float)
    Y21 = Column(Float) ; Y22 = Column(Float)  
    Y23 = Column(Float) ; Y24 = Column(Float)  
    Y25 = Column(Float) ; Y26 = Column(Float)  
    Y27 = Column(Float) ; Y28 = Column(Float)  
    Y29 = Column(Float) ; Y30 = Column(Float)
    Y31 = Column(Float) ; Y32 = Column(Float) 
    Y33 = Column(Float) ; Y34 = Column(Float) 
    Y35 = Column(Float) ; Y36 = Column(Float)  
    Y37 = Column(Float) ; Y38 = Column(Float) 
    Y39 = Column(Float) ; Y40 = Column(Float)
    Y41 = Column(Float) ; Y42 = Column(Float)  
    Y43 = Column(Float) ; Y44 = Column(Float)  
    Y45 = Column(Float) ; Y46 = Column(Float)  
    Y47 = Column(Float) ; Y48 = Column(Float)  
    Y49 = Column(Float) ; Y50 = Column(Float)