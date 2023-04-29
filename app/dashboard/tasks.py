from threading import Thread
import random, psutil, time
from dashboard.models import SystemData, CustomUser
from storage_drive.models import get_space_available

MAX_SAVE_NUMBER = 20
def save_system_data():
    global MAX_SAVE_NUMBER
    while True:
        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent
        cpu_temp = float(random.randint(40,60))
        timestamp = int(time.time())
 
        system_data = SystemData(cpu_percent=cpu_percent, mem_percent=mem_percent, disk_percent=disk_percent, timestamp=timestamp, cpu_temp=cpu_temp)
        system_data.save()
        current_count = SystemData.objects.count()
        
        if current_count > MAX_SAVE_NUMBER:
            first_n_records = SystemData.objects.order_by('id').filter(id__lt = (system_data.pk - MAX_SAVE_NUMBER))
            first_n_records.delete()

         
        time.sleep(7)

def save_user_storage_drive():
    global MAX_SAVE_NUMBER
    while True:
        users = CustomUser.objects.all()
        for user in users:
            used_space_by_user = get_space_available(user)
            user.used_space = round(used_space_by_user,4)
            user.save()
        
        time.sleep(14)




def save_db():
    t1 = Thread(target=save_system_data, daemon=True)
    t1.start()
    t2 = Thread(target=save_user_storage_drive, daemon=True)
    t2.start()
    print("start parallel data saving")
    t1.join()
    t2.join()
