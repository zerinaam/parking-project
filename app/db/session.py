from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL, create_engine

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="password",
    host="localhost",
    database="parking",
    port=5432
)


engine = create_engine(url)

Session = sessionmaker(bind=engine)
session = Session()
