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
zone = EPlusDB()
print(zone)
