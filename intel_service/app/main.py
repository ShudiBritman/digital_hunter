from consumers.consumer_intel import ConsumerCon
from db.database import DataBase


def main():
    DataBase.init_db()
    ConsumerCon.consumer_loop()



if __name__ == "__main__":
    main()