from database.DB_connect import DBConnect
from model.airport import Airport
from model.arco import Arco


class DAO:

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                   FROM airports a
                   order by a.AIRPORT asc"""
        cursor.execute(query)
        for row in cursor:
            result.append(Airport(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(NMin, idMapAirports):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT t.ID, t.IATA_CODE, count(*) as N
                   FROM (SELECT a.ID, a.IATA_CODE, f.AIRLINE_ID, count(*)
                         FROM airports a, flights f 
                         WHERE a.ID = f.ORIGIN_AIRPORT_ID or a.ID = f.DESTINATION_AIRPORT_ID
                         group by a.ID, a.IATA_CODE, f.AIRLINE_ID) t
                   group by t.ID, t.IATA_CODE 
                   having N >= %s
                   order by N asc"""
        cursor.execute(query, (NMin,))
        for row in cursor:
            result.append(idMapAirports[row["ID"]])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesV1(idMap):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, count(*) as n
                    FROM flights f
                    group by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID
                    order by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID"""
        cursor.execute(query)
        for row in cursor:
            if row["ORIGIN_AIRPORT_ID"] in idMap and row["DESTINATION_AIRPORT_ID"]:
                result.append(Arco(row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["n"]))
        cursor.close()
        conn.close()
        return result




