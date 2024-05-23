import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #name of the log file based on time and date

log_path=os.path.join(os.getcwd(),"logs") #in the cwd make one folder called logs

os.makedirs(log_path,exist_ok=True) 


LOG_FILEPATH=os.path.join(log_path,LOG_FILE)


logging.basicConfig(level=logging.INFO,   #specific levels till which it will capture the logs
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    
)
            #[2024-01-10 15:57:26,997] 6 root - INFO -  this my second tesgting