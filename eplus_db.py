import sqlite3

class EPlusDB():
    '''
    Implements a class that abstacts EnergyPlus/OpenStudio databases tables as
    simple variables and arrays and abstract SQL queries as simple methods.
    '''

    def query_zones(self):
        '''
        Queries the DB for the zones, returns the zones as a list.
        '''
        if self.is_connected:
            cursor = self.con.cursor()
            cursor.execute("select * from zones") 
            self.zones = cursor.fetchall()
            self.zones_len = len(self.zones)
            return self.zone
        else:
            raise NameError("DB is not connected") #TODO not the best way to handle this
    
    def connect_db()
        ''' 
        Creates the connect object, handles connection exceptions.
        '''
        try:
            self.con = sqlite3.connect(self.db_path)
            self.is_connected = True
        except:
            self.is_connected = False

    def __init__(self):
        self.is_connected = False
        self.con = None 
        self.db_path = None
        self.zones_len = None
        self.zones = None

    def __str__(self):
        return("EnergyPlus Database\nZones:%d" % self.zones_len)
'''
con = sqlite3.connect('db/eplusout.sql')
cursor = con.cursor()
cursor.execute("select * from zones") 
zones = cursor.fetchall()
print("There are " + str(len(zones)) + " zones in this DB")
heat_per_zone = []
zone_data = []
for i, zone in enumerate(zones):
    print("Gathering information on zone: " + zone[1] + ".")
    cursor.execute("""SELECT ReportData.ReportDataDictionaryIndex, ReportData.TimeIndex, ReportData.Value, ReportDataDictionary.ReportDataDictionaryIndex, ReportDataDictionary.KeyValue, ReportDataDictionary.Name, Time.TimeIndex, Time.DayType
    FROM ReportData
    JOIN ReportDataDictionary
    ON ReportData.ReportDataDictionaryIndex = ReportDataDictionary.ReportDataDictionaryIndex
    JOIN Time
    ON ReportData.TimeIndex = Time.TimeIndex
    WHERE ReportDataDictionary.KeyValue = (?) AND ReportDataDictionary.Name = 'Zone Air System Sensible Cooling Rate' AND Time.DayType != 'SummerDesignDay' AND Time.DayType != 'WinterDesignDay'
    """, (zone[1],))
    timed_data = cursor.fetchall()
    zone_data.append(timed_data)
    print("Number of record for " + zone[1] + " is: " + str(len(timed_data)) + " entries")
    heat_sum = 0
    for row in timed_data:
        heat_sum += float(row[2])
    print(heat_sum)
    heat_per_zone.append(heat_sum)
    if i > 2: # Only analyses the first 3 iterations.
        break
building_heat_per_hour = []
for i in range(len(zone_data[0])): # TODO Change this to numpy
    heat = 0
    for zone in zone_data:
        heat += zone[i][2]
    building_heat_per_hour.append(heat)

print(len(building_heat_per_hour))
print(sum(building_heat_per_hour))
print(building_heat_per_hour[0])
print(heat_per_zone)
print(sum(heat_per_zone))
print(heat_per_zone[0])
'''
zone = EPlusDB()
print(zone)
