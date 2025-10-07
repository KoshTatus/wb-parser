from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from src.database.models import Base
from src.settings import settings

db_name = settings.db_name
db_user = settings.db_user
db_password = settings.db_password
db_host = settings.db_host
db_port = settings.db_port

DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)

local_session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def create_tables():
    Base.metadata.create_all(engine)

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()