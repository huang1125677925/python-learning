import logging
import threading
import time

def worker(arg):
    while not arg['stop']:
        logging.debug('Hi from myfunc')
        time.sleep(0.5)
DATE_FORMAT = "%m/%d/%Y %H:%M:%S"
def main():
    logging.basicConfig(level=logging.DEBUG, format='%('
	'created)f %(asctime)s %(levelname)s %(process)d %(relativeCreated)6d %(threadName)s %(message)s',datefmt=DATE_FORMAT)
    info = {'stop': False}
    thread = threading.Thread(target=worker, args=(info,))
    thread.start()
    while True:
        try:
            logging.debug('Hello from main')
            time.sleep(0.75)
        except KeyboardInterrupt:
            info['stop'] = True
            break
    thread.join()

if __name__ == '__main__':
    main()