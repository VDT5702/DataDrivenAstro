#Lab 5a Task2:  A proper Median

import psycopg2
import numpy as np

def column_stats(table,column_name):
  conn = psycopg2.connect(dbname='db' , user='grok')
  cursor = conn.cursor()
  
  query = "SELECT " + column_name + " FROM " + table + ";" 
  cursor.execute(query)
  records = cursor.fetchall()
  
  array=np.array(records)
  
  return(np.mean(array),np.median(array))

