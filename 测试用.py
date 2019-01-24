import pymysql
conn = pymysql.connect(host='120.78.129.89', port=3306, user='root', password='mysql', db='tcmkbdata',
                                       charset="utf8")

cursor = conn.cursor()
title='胃寒'
select_sql = """select * from test where title = %s"""
select_sql2 = """select * from test where title = %s"""
print(cursor.execute( select_sql,title))
print(cursor.execute( select_sql2,title))
result = cursor.fetchone()
print(result)
print(result)
conn.commit()
cursor.close()