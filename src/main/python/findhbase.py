import traceback
import  happybase


def connect2Hbase(port=9090, timeout = None, autoconnect = True, table_prefix = None,
                  table_prefix_separator = b'_', compat = '0.96', transport = 'buffered', protocol = 'binary'
):
    try:
        c = happybase.Connection('10.66.206.203', port = 9090, timeout = 60000, autoconnect = True, table_prefix = None, table_prefix_separator = b'_', compat = '0.96', transport = 'buffered',protocol = 'binary')
    except:
        raise traceback.print_exc()
    return c


connection = connect2Hbase()
print (connection.tables())
table = connection.table('t_push_quality_vid')
print (connection.tables())

for key, value in table.scan():
    print key, value

    # 通过row_prefix参数来设置需要扫描的row key
for key, value in table.scan(row_prefix='www.test'):
    print key, value


# 通过row_start和row_stop参数来设置开始和结束扫描的row key
for key, value in table.scan(row_start='www.test2.com', row_stop='www.test3.com'):
    print key, value

    # 检索一行数据
row = table.row('16519501299619044599')
print row

# 检索多行数据，返回字典
rows_dict = dict(table.rows(['www.test1.com', 'www.test4.com']))
print rows_dict

