import sqlite3

class Zone():
    '''
    Abstracts zone information
    '''
    def get_timed_data(self):
        print(self.timed_data)

    def __init__(self, zone_data=None):
        self.zone_data = zone_data #TODO assure this is an array
        self.zone_name = zone_data[0][4]
        self.timed_data = [row[2] for row in zone_data] 
        self.timed_data_len = len(self.timed_data)
        return

    def __str__(self):
        return("EnergyPlus Zone: %s\nNumber of entries: %d" % (self.zone_name, self.timed_data_len))
        
class EPlusDB():
    '''
    Implements a class that abstacts EnergyPlus/OpenStudio databases tables as
    simple variables and arrays and abstract SQL queries as simple methods.
    '''
    def query_zone_info(self, zone_name):

        cursor = self.con.cursor()
        print("Requesting data for %s..." % zone_name)
        cursor.execute("""SELECT ReportData.ReportDataDictionaryIndex, ReportData.TimeIndex, ReportData.Value, ReportDataDictionary.ReportDataDictionaryIndex, ReportDataDictionary.KeyValue, ReportDataDictionary.Name, Time.TimeIndex, Time.DayType
        FROM ReportData
        JOIN ReportDataDictionary
        ON ReportData.ReportDataDictionaryIndex = ReportDataDictionary.ReportDataDictionaryIndex
        JOIN Time
        ON ReportData.TimeIndex = Time.TimeIndex
        WHERE ReportDataDictionary.KeyValue = (?) AND ReportDataDictionary.Name = 'Zone Air System Sensible Cooling Rate' AND Time.DayType != 'SummerDesignDay' AND Time.DayType != 'WinterDesignDay'
        """, (zone_name,))
        timed_data = cursor.fetchall()
        return timed_data 

    def get_all_zones_data(self):
        self.query_zones_names()
        print("Requested zones: %d" % self.zones_len) #TODO Implement a logger
        for name in self.zones_names:
            self.zones.append(Zone(self.query_zone_info(name)))
        return  

    def query_zones_names(self):
        '''
        Queries the DB for the zones, returns the zones as a list.
        '''
        if self.is_connected:
            cursor = self.con.cursor()
            cursor.execute("select * from zones") 
            self.zones_names = [row[1] for row in cursor.fetchall()]
            self.zones_len = len(self.zones_names)
            return self.zones_names
        else:
           #TODO not the best way to handle this
           raise NameError("DB is not connected")     

    def connect_db(self, db_path):
        ''' 
        Creates the connect object, handles connection exceptions.
        '''
        self.db_path = db_path #TODO Test if db_path and self.db_path is None
        try:
            self.con = sqlite3.connect(self.db_path)
            self.is_connected = True
        except:
            self.is_connected = False
            print("No DB found")

    def __init__(self):
        self.is_connected = False
        self.con = None 
        self.db_path = None
        self.zones_len = 0
        self.zones_names = None
        self.zones = []

    def __str__(self):
        #TODO be more descriptive
        return("EnergyPlus Database\nZones:%d" % self.zones_len)

eplusdb = EPlusDB()
eplusdb.connect_db("db/eplusout.sql")
eplusdb.get_all_zones_data()
for zone in eplusdb.zones:
    print(zone)
'''
names = eplusdb.query_zones_names()
print(names[0][1])
zone1 = Zone(eplusdb.query_zone_info(names[0][1]))
print(zone1)
#zone1.get_timed_data()
'''
