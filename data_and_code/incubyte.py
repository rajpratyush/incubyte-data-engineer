import pandas as pd
import numpy as np
from sqlalchemy import create_engine, inspect, Column, String, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base




Base = declarative_base()


def createTable(tablename):
    class CountryName(Base):
        __tablename__ = tablename
        customerName = Column(String(255),primary_key=True)
        id = Column(String(18),nullable=False)
        customerOpenDate = Column(Date, nullable=False)
        lastConsultedDate = Column(Date)
        vaccinationType = Column(String(5))
        doctorConsulted = Column(String(255))
        state = Column(String(5))
        country = Column(String(5))
        dateOfBirth = Column(Date)
        activeCustomer = Column(String(1))
    return CountryName


def createTables(engine, inspector, db, distinct_countries, existing_tables):
    for tbl in distinct_countries:
        if tbl not in existing_tables:
            print("trying to create " + tbl)
            try:
                createTable(tbl).__table__.create(bind=engine)
                print("Created")
            except Exception as e:
                print(e)
        else:
            print(tbl + " already exists")
            

def getTables(engine):
    inspector = inspect(engine)
    
    all_tables = [tbl for tbl in inspector.get_table_names(schema=db)]

    return all_tables, inspector


df = pd.read_csv('patients.txt', sep="|", header=None)

is_header = df.iloc[0, 1]

if is_header == 'H':
    df.drop(df.head(1).index, inplace=True)


df.columns = ["N","D",
              "customerName", "customerID",
              "customerOpenDate", "lastConsultedDate",
              "vaccinationType", "doctorConsulted",
              "state", "country","dateofBirth",
              "activeCustomer"]

del df['D']
del df['N']

df['customerID'] = df['customerID'].apply(np.int64)

df.set_index('customerID')

print(df.info(), end="\n\n")

try:
    df['customerOpenDate'] = pd.to_datetime(
        df['customerOpenDate'], format='%Y%m%d')
    df['lastConsultedDate'] = pd.to_datetime(
        df['lastConsultedDate'], format='%Y%m%d')
    df['dateofBirth'] = pd.to_datetime(
        df['dateofBirth'], format='%d%m%Y')
except Exception as e:
    print(e)

print(df.info(), end="\n\n")
print(df)

df['country'] = df['country'].str.lower()

distinct_countries = df['country'].drop_duplicates()

print("\nDistinct Countries:/n",distinct_countries)

print()
db = "queries"
try:
    engine = create_engine(
        "mysql+mysqlconnector://root:root@localhost:3306/" + db)
    engine.connect()
    print("Database Connected")
except Exception as e:
    print(e)

existing_tables, inspector = getTables(engine)
print("Existing Tables:", existing_tables)

createTables(engine, inspector, db, distinct_countries, existing_tables)

existing_tables, inspector = getTables(engine)
print("Existing Tables:", existing_tables)

for country in distinct_countries:
    my_filt = (df['country'] == country)
    try:
        print("Inserting Records in " + country)

        if country in existing_tables:
            df[my_filt].to_sql(name=country, con=engine,
                               if_exists='replace', index=False)
            print("Inserted")
        else:
            print(country + " table does Not exists")
    except Exception as e:
        print(e)



