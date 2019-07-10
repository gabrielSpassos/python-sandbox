from datetime import datetime
import schedule
import time

def task():
    print(datetime.now())


schedule.every().minute.at(":21").do(task)


def run():
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    run()
