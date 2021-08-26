import sqlite3


con = sqlite3.connect('db/eplusout.sql')
cursor = con.cursor()
cursor.execute("SELECT * FROM Zones") 
zones = cursor.fetchall()
print("There are " + str(len(zones)) + " zones in this DB")
heat_per_zone = []
for zone in zones:
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
    print("Number of record for " + zone[1] + " is: " + str(len(timed_data)) + " entries")
    heat_sum = 0
    for row in timed_data:
        heat_sum += float(row[2])
    print(heat_sum)
    heat_per_zone.append(heat_sum)
print(heat_per_zone)
print(sum(heat_per_zone))

