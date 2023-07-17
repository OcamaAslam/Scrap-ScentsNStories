import pandas as pd
from sqlalchemy import create_engine


def db_table(df):
    db_username = 'root'
    db_password = 'root'
    db_host = 'localhost'
    db_port = '3306'
    db_name = 'perfumes'

    # Create the database connection string
    db_connection_str = f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'

    # Create the database engine
    engine = create_engine(db_connection_str)

    # Save the DataFrame to the database
    df.to_sql('ScentsNStories', con=engine, if_exists='replace', index=False)
