import pymysql
from root_analyse.config import server_config
import time


class Mysql_Helper(object):
    """
    读取mongodb数据
    """
    
    # logger = log_helper.get_logger()
    def __init__(self):
        
        self.mysql_dic = server_config.SERVER_DIC.get('mysql')
        self.server = self.mysql_dic.get("server")
        self.port_name = self.mysql_dic.get("port")
        self.user_name = self.mysql_dic.get("user")
        self.passwd_ = self.mysql_dic.get("passwd")
        self.db_name = self.mysql_dic.get("db")
        self.simple_table_id = {}
    
    def get_connection(self):
        try:
            db = pymysql.connect(host="10.1.11.14", port=3307, user="aiops", password="aiops", database="aiops_monitor",
                                 charset='utf8')
            # connection = pymysql.connect(db=self.db_name, user=self.user_name, passwd=self.passwd_, host=self.server, port=self.port_name)
            return db
        except Exception as e:
            # self.logger.error('MySQL Error, %s' % e)
            print('链接失败')
    
    def delete_simple(self, db, list_data):
        
        cursor = db.cursor()
        
        print("要删除的数据", list_data)
        
        try:
            for item in list_data:
                sql1 = "DELETE FROM t_ci_simple_info WHERE category='%s' and object='%s'" % (item[0], item[1])
                sql2 = "DELETE FROM t_ci_simple_info WHERE category='%s' and object='%s'" % (item[1], item[0])
                cursor.execute(sql1)
                cursor.execute(sql2)
            
            db.commit()
            cursor.execute(sql1)
            db.commit()
        except:
            print('删除数据失败!')
            db.rollback()
    
    # 往节点表插入
    def insert_simple(self, db, list_data):
        cursor = db.cursor()
        
        try:
            for item in list_data:
                sql = "INSERT INTO t_ci_simple_info(category, object) VALUES ('%s', '%s')" % (item[0], item[1])
                
                cursor.execute(sql)
                self.simple_table_id[item[0] + '_' + item[1]] = int(cursor.lastrowid)
                print(self.simple_table_id)
                db.commit()
        except:
            print('插入数据失败!')
            db.rollback()
    
    # 往关系表插入
    def insert_relation(self, db, list_data):
        cursor = db.cursor()
        try:
            for item in list_data:
                print(item)
                sql = "INSERT INTO t_ci_relation(source,target,relation,build_type) VALUES ('%d', '%d','%s','%d')" % (
                item[0], item[1], str(item[2]), 0)
                cursor.execute(sql)
                print('insert success')
                db.commit()
        except:
            print('插入数据失败!')
            db.rollback()
    
    def delete_relation(self, db):
        
        cursor = db.cursor()
        sql = "DELETE FROM t_ci_relation WHERE build_type=0"
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print('删除数据失败!')
            db.rollback()
    
    def covert_objectcategory_to_id(self, list_data):
        temp = []
        for item in list_data:
            temp1 = []
            temp1.append(self.simple_table_id[item[0]])
            temp1.append(self.simple_table_id[item[1]])
            temp1.append(item[2])
            temp.append(temp1)
        
        return temp
    
    def covert_relate_data_to_2(self, list_data):
        temp = set()
        result = []
        
        for item in list_data:
            temp.add(item[0])
            temp.add(item[1])
        
        for element in temp:
            temp_list = element.split('_')
            result.append(temp_list)
        
        return result
    
    def read_metric_key(self, db, id):
        
        cursor = db.cursor()
        sql = "SELECT metric_key,`host`,platform FROM metric_key WHERE id=%d" % (id)
        
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            
            return data
        except:
            print('删除数据失败!')
            db.rollback()
    
    def closedb(self, db):
        db.close()
    
    def update_mysql_db(self, relate_data):
        
        db = self.get_connection()
        relation_data_to_2 = self.covert_relate_data_to_2(relate_data)
        self.delete_simple(db, relation_data_to_2)
        self.insert_simple(db, relation_data_to_2)
        
        # self.delete_relation(db)
        relation_data = self.covert_objectcategory_to_id(relate_data)
        print(relation_data)
        self.insert_relation(db, relation_data)
        self.closedb(db)


if __name__ == "__main__":
    '''
    relation =[[11, 13, '0.938'], ['cpu_10.1.10.35 主机', 'cpu_10.1.11.44 主机', 0.941], ['cpu_10.1.11.44 主机', 'cpu_10.1.11.42 主机', 1.0], ['cpu_10.1.11.44 主机',
                                                                                                                                       'cpu_10.1.10.35 主机', 1.0], ['cpu_10.1.11.16 主机', 'cpu_10.1.11.42 主机', 1.0], ['cpu_10.1.11.16 主机', 'cpu_10.1.10.40 主机', 1.0], ['cpu_10.1.11.44 主机', 'cpu_10.1.10.131 主机', 1.0], ['cpu_10.1.10.36 主机', 'cpu_10.1.11.44 主机', 0.941], ['cpu_10.1.11.44 主机', 'cpu_10.1.10.40 主机',
                                                                                                                                                                                                                                                                                                                                                                  1.0], ['cpu_10.1.11.44 主机', 'cpu_Zabbix server 主机', 1.0], ['cpu_10.1.11.41 主机', 'cpu_10.1.11.44 主机', 0.941], ['cpu_10.1.11.44 主机', 'cpu_10.1.10.113 主机', 1.0], ['cpu_10.1.11.44 主机', 'cpu_10.1.11.41 主机', 1.0], ['cpu_10.1.11.44 主机', 'cpu_10.1.11.16 主机', 1.0], ['cpu_10.1.11.44 主机', 'cpu_10.1.11.31 主机', 1.0], ['cpu_10.1.11.16 主机', 'cpu_10.1.11.44 主机', 1.0], ['cpu_10.1.11.44 主机', 'cpu_10.1.10.36 主机', 1.0], ['cpu_10.1.11.44 主机', 'cpu_10.1.10.144 主机', 0.938], ['cpu_10.1.11.31 主机', 'cpu_10.1.11.44 主机', 0.842], ['cpu_Zabbix server 主机', 'cpu_10.1.11.44 主机', 0.842], ['cpu_10.1.10.40 主机', 'cpu_10.1.11.16 主机', 0.9], ['cpu_10.1.11.42 主机', 'cpu_10.1.11.16 主机', 0.857]]
    Mysql_Helper().update_mysql_db(relation)

    '''
    import pandas as pd
    
    itemid = pd.read_csv('选中指标.csv', names=['id'])
    mysql = Mysql_Helper()
    db = mysql.get_connection()
    key_data = []
    for id in itemid['id']:
        temp = []
        temp.append(id)
        data = mysql.read_metric_key(db, id)
        temp.append(data[0][0])
        temp.append(data[0][1])
        temp.append(data[0][2])
        key_data.append(temp)
    mysql.closedb(db)
    
    pd.DataFrame(data=key_data, columns=['id', 'metric_key', 'host', 'platform']).to_csv('演示环境指标.csv')