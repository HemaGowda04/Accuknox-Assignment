import psutil
import logging
from datetime import datetime

logging.basicConfig(filename="system_health.log", level=logging.WARNING,
                    format="%(asctime)s:%(levelname)s:%(message)s")

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def monitor_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_usage}%")
    
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"Low Disk space detected: {disk_usage}%")
    
    processes = len(psutil.pids())
    logging.info(f"Total running processes: {processes}")

if __name__ == "__main__":
    monitor_system()