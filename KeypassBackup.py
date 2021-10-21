import sys
import os
import dropbox
import contextlib
import datetime
import time
import schedule

initial=1

@contextlib.contextmanager
def stopwatch(message):
    """Context manager to print how long a block of code took."""
    t0 = time.time()
    try:
        yield
    finally:
        t1 = time.time()
        print('Total elapsed time for %s: %.3f' % (message, t1 - t0))

def performBackup():
    global initial
    environment_variables = ["DROPBOX_TOKEN", "DROPBOX_LOCATION", "LOCAL_LOCATION", "LOG_LOCATION"]
    varDict = {}
    for key in environment_variables:
        temp = os.environ[key]
        if temp is None:
            print("{} environment variable not set!".format(key))
            exit(-1)
        varDict[key] = temp
    print(varDict)
    if(initial == 1):
        initial = 0
        f = open(varDict["LOG_LOCATION"],"a")
        f.write(str(datetime.datetime.now()) + ": Service restarted\n")
        f.close()
    dbx = dropbox.Dropbox(varDict["DROPBOX_TOKEN"])
    with stopwatch('download'):
        try:
            print("Downloading...")
            beforeTime = time.time()
            md = dbx.files_download_to_file(varDict["LOCAL_LOCATION"],varDict["DROPBOX_LOCATION"])
            endTime = time.time()
            f = open(varDict["LOG_LOCATION"],"a")
            f.write(str(datetime.datetime.now()) + ": [Success] Last modified " + str(md.server_modified) + " Size: " + str(md.size) + " bytes | Took " + str(endTime-beforeTime) + " seconds\n")
            f.close()
            print(str(datetime.datetime.now()) + ": [Success] Last modified " + str(md.server_modified) + " Size: " + str(md.size) + " bytes | Took " + str(endTime-beforeTime) + " seconds\n")

        except dropbox.exceptions.ApiError as err:
            print('*** HTTP error', err)
            f = open(varDict["LOG_LOCATION"],"a")
            f.write(str(datetime.datetime.now()) + ": [Error] " + str(err) + "\n")
            f.close()

schedule.every().day.at("12:00").do(performBackup)
#schedule.every(20).seconds.do(performBackup)

if __name__ == "__main__":
    print("KeypassBackup.py performing initial backup...")
    performBackup()
    print("Next backup will be at 12:00")
    #performBackup();
    while(1):
        schedule.run_pending()
        time.sleep(1)


