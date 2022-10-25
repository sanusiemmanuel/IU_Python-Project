from numpy import genfromtxt
from time import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from train_dataset import TrainDataset, TrainBase
from ideal_function_dataset import IdealDataset, IdealBase
from test_dataset import TestDataset, TestBase
import ideal_mapping
import bokeh_graph

#Load CSV File
def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1)
    return data.tolist()


if __name__ == "__main__":
    t = time()
    ideal_mapping.GenrateIdealFuntion()
    ideal_mapping.MappingOfTestData()
    #Create the database
    engine = create_engine('sqlite:///Database.db')
    TrainBase.metadata.create_all(engine)
    IdealBase.metadata.create_all(engine)
    TestBase.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "train.csv" 
        data = Load_Data(file_name) 

        for i in data:
            
            record = TrainDataset(**{
                'X' : i[0],
                'Y1' : i[1],
                'Y2' : i[2],
                'Y3' : i[3],
                'Y4' : i[4],    
                })

            s.add(record) #Add all the records
        s.commit() #Attempt to commit all the records
        

    except Exception as e:
        s.rollback() #Rollback the changes on error
        print(f"It didn't safe here is why {e}")
    finally:
        s.close() #Close the connection
    print("Time elapsed: " + str(time() - t) + " s." + " Created Database... \nCreated Test Table In The Database...") #0.091s


    try:
        file_name = "ideal.csv" 
        data = Load_Data(file_name) 
        y = [f"Y{i}" for i in range(0, 51)]
        for i in data:
            
            record = IdealDataset(**{
                'X' : i[0],
                y[1] : i[1], y[2] : i[2], y[3] : i[3], y[4] : i[4], y[5] : i[5],
                y[6] : i[6], y[7] : i[7], y[8] : i[8], y[9] : i[9], y[10] : i[10],
                y[11] : i[11], y[12] : i[12], y[13] : i[13], y[14] : i[14], y[15] : i[15],
                y[16] : i[16], y[17] : i[17], y[18] : i[18], y[19] : i[19], y[20] : i[20],
                y[21] : i[21], y[22] : i[22], y[23] : i[23], y[24] : i[24], y[25] : i[25],
                y[26] : i[26], y[27] : i[27], y[28] : i[28], y[29] : i[29], y[30] : i[30],
                y[31] : i[31], y[32] : i[32], y[33] : i[33], y[34] : i[34], y[35] : i[35],
                y[36] : i[36], y[37] : i[37], y[38] : i[38], y[39] : i[39], y[40] : i[40],
                y[41] : i[41], y[42] : i[42], y[43] : i[43], y[44] : i[44], y[45] : i[45],
                y[46] : i[46], y[47] : i[47], y[48] : i[48], y[49] : i[49], y[50] : i[50],
                    
                })

            s.add(record) #Add all the records            
        s.commit() #Attempt to commit all the records
        

    except Exception as e:
        s.rollback() #Rollback the changes on error
        print(f"It didn't safe here is why {e}")
    finally:
        s.close() #Close the connection
    print("Time elapsed: " + str(time() - t) + " s." + " Created Ideal Function Table In The Database...") #0.091s

    try:
        file_name = "assigned_dataset.csv" 
        data = Load_Data(file_name) 

        for i in data:
            
            record = TestDataset(**{
                'X' : i[0],
                'Y' : i[1],
                'Delta_Y' : i[2],
                'Y_Deviation' : i[3]
                })

            s.add(record) #Add all the records
        s.commit() #Attempt to commit all the records
        

    except Exception as e:
        s.rollback() #Rollback the changes on error
        print(f"It didn't safe here is why {e}")
    finally:
        s.close() #Close the connection
    print("Time elapsed: " + str(time() - t) + " s." + " Created Test Table In The Database... \n Displaying Graph...")

    bokeh_graph.PlotGraph()

