from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import json


class Database:
    def __init__(self):
        with open('config.json', 'r') as file:
            db_ip, user, password, db_name = json.load(file).values()
        config = f"postgresql+psycopg2://{user}:{password}@{db_ip}/{db_name}"
        self.engine = create_engine(config, echo=True)

    def test_connection(self):
        with Session(self.engine) as session:
            print(session.info)


if __name__ == '__main__':
    database = Database()
    database.test_connection()
