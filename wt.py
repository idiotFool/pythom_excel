import xlwt

# 创建工作簿
wb = xlwt.Workbook()
# 创建工作表
ws = wb.add_sheet('orders')
# 填充数据
ws.write_merge(0,1,0,4,'陕中旅合作酒店订单')

# 写入数据
data=(
    ('XCL1972','西安曲江国际饭店','张小平 张佳仪',30,2),
    ('XCL1977',	'西安曲江国际饭店',	'李永刚',30,2),
    ('XCL1993',	'西安海景国际酒店',	'徐爱君',28,2),
    ('XCL2141',	'莱卡酒店(西安西工大店)','屈素梅',39,2),
    ('XCL2257',	'汉阴东尚柏悦酒店',	'张宏国',34,2)
)
for r, item in enumerate(data):
    for c, val in enumerate(item):
        ws.write(r+2, c, val)

# 保存
wb.save('liuna_order.xls')