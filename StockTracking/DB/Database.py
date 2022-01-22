
import psycopg2

#Connect the db
con = psycopg2.connect(
    host = "localhost",
    database = "StockTrackingDB",
    user = "postgres",
    password = "031100")