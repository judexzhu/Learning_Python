# encoding = utf-8  
import MySQLdb  
import xlrd  
import time  
import sys  
reload(sys)  
sys.setdefaultencoding("utf-8")  
  
# 从users.xls文件获取10000条用户数据  
# 该文件由create_users.py生成  
def get_table():  
    FILE_NAME = 'owner.xls'  
    data = xlrd.open_workbook(FILE_NAME)  
    table = data.sheets()[0]  
    return table  

# 批量插入executemany  
def insert_by_many(table):  
    nrows = table.nrows  
    param=[]  
    for i in xrange(1,nrows):  
        # 第一列username，第二列salt，第三列pwd  
        param.append([table.cell(i, 0).value, table.cell(i, 1).value])  
    try:  
        #sql = 'INSERT INTO user values(%s,%s,%s)' 
        sql = 'UPDATE AttributeValue JOIN Object ON AttributeValue.object_id = Object.id SET AttributeValue.string_value = %s WHERE AttributeValue.attr_id=14 and Object.name = %s' 
        # 批量插入  
        cur.executemany(sql, param)  
        conn.commit()  
    except Exception as e:  
        print e  
        conn.rollback()   
    print '[insert_by_many executemany] total:',nrows-1   
  
  
# 连接数据库  
conn = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="PASSWORD", db="racktables")  
cur = conn.cursor()  

# 从excel文件获取数据  
table = get_table()  
  
# 使用循环插入  
start = time.clock()  
insert_by_loop(table)  
end = time.clock()  
print '[insert_by_loop execute] Time Usage:',end-start  
  
# 使用批量插入  
start = time.clock()  
insert_by_many(table)  
end = time.clock()  
print '[insert_by_many executemany] Time Usage:',end-start  
  
# 释放数据连接  
if cur:  
    cur.close()  
if conn:  
    conn.close()  


INSERT INTO AttributeValue (object_id,object_tid, attr_id,string_value, uint_value, float_value) VALUES(1, "A", 19) ON DUPLICATE KEY UPDATE AttributeValue JOIN Object ON AttributeValue.object_id = Object.id SET AttributeValue.string_value = %s WHERE AttributeValue.attr_id=14 and Object.name = %s


INSERT INTO AttributeValue (object_id,object_tid, attr_id,string_value, uint_value, float_value)
SELECT a,b,c FROM tbl_b 
ON DUPLICATE KEY UPDATE c = tbl_b.c 



insert into AttributeValue (object_id, object_tid, attr_id, string_value) select id, objtype_id, '14', %s from Object where name=%s on duplicate key update AttributeValue.string_value=%s 


insert into AttributeValue (object_id, object_tid, attr_id, string_value) select id, objtype_id, '14', 'testowner' from Object where name = 'test1' on duplicate key update AttributeValue.string_value= 'testonwer';
