import sqlite3

class Zone():
    '''
    Abstracts zone information
    '''

    def __init__(self):
        return

    def __str__(self):
        return(self.zone_name)
        
class EPlusDB():
    '''
    Implements a class that abstacts EnergyPlus/OpenStudio databases tables as
    simple variables and arrays and abstract SQL queries as simple methods.
    '''
    def query_zone_info(self, zone_name):

        cursor = self.con.cursor()

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

    def query_zones_names(self):
        '''
        Queries the DB for the zones, returns the zones as a list.
        '''
        if self.is_connected:
            cursor = self.con.cursor()
            cursor.execute("select * from zones") 
            self.zones_names = cursor.fetchall()
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

    def __str__(self):
        #TODO be more descriptive
        return("EnergyPlus Database\nZones:%d" % self.zones_len)

eplusdb = EPlusDB()
eplusdb.connect_db("db/eplusout.sql")
names = eplusdb.query_zones_names()
print(names[0][1])
zone1 = eplusdb.query_zone_info(names[0][1])
print(zone1)
