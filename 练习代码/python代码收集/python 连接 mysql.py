import MySQLdb
try:
   connection = MySQLdb.connect(user="user",passwd="password",host="xxx",db="test")
except:
   print "Could not connect to MySQL server."
   exit( 0 )
 
try:
   cursor = connection.cursor()
   cursor.execute( "SELECT note_id,note_detail FROM note where note_id = 1" )
   print "Rows selected:", cursor.rowcount
    
   for row in cursor.fetchall():
       print "note : ", row[0], row[1]
   cursor.close()
