import time
from celery import task

@task
def show_():
    print('hello ...')
    time.sleep(10)
    print('world ...')
