import subprocess
from eplus_db import EPlusDB, Zone

subprocess.run(["bash", "/home/octavio/hintedis_bash/hintedis_bash", "user1", "project1"])
subprocess.run(["echo", "test"], capture_output = True)
db = EPlusDB()
db.connect_db("/home/octavio/files/user1/project1/result/eplusout.sql")
db.get_all_zones_data()
db.get_all_zones_hourly()
db.get_all_zones_monthly()
print(db.all_zones_monthly)
