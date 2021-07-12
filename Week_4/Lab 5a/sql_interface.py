# Lab 5a Task1: Taking it all in

import psycopg2

def select_all(tname):  
  
  conn = psycopg2.connect('dbname=db user=grok')
  cursor = conn.cursor()
  
  s ='SELECT * FROM ' + tname + ';'
  
  cursor.execute(s)
  reocrds = cursor.fetchall()
  
  return records