import requests
import mysql.connector
from datetime import datetime
import json

# 获取当前时间
now_time = datetime.now()  
# print(now_time)

#获取 api
url = "https://devapi.qweather.com/v7/weather/now?location=101220307&key=fb7f4e2fb9a348bcaee410b2e46d439f"
response = requests.get(url) 
data_dict = response.json()
# print(data_dict)

# 提取数据
obs_time = data_dict["now"]['obsTime']
temp = data_dict["now"]['temp']
feels_like = data_dict["now"]['feelsLike']
icon = data_dict["now"]['icon']
text = data_dict["now"]['text']
wind_360 = data_dict["now"]['wind360']
wind_dir = data_dict["now"]['windDir']
wind_scale = data_dict["now"]['windScale']
wind_speed = data_dict["now"]['windSpeed']
humidity = data_dict["now"]['humidity']
precip = data_dict["now"]['precip']
pressure = data_dict["now"]['pressure']
vis = data_dict["now"]['vis']
cloud = data_dict["now"]['cloud']
dew = data_dict["now"]['dew']

# 打印解析后的数据
# print("Now Data:")
# print("  Obs Time:", obs_time)
# print("  Temp:", temp)
# print("  Feels Like:", feels_like)
# print("  Icon:", icon)
# print("  Text:", text)
# print("  Wind 360:", wind_360)
# print("  Wind Dir:", wind_dir)
# print("  Wind Scale:", wind_scale)
# print("  Wind Speed:", wind_speed)
# print("  Humidity:", humidity)
# print("  Precip:", precip)
# print("  Pressure:", pressure)
# print("  Vis:", vis)
# print("  Cloud:", cloud)
# print("  Dew:", dew)


# 连接MySQL数据库
cnx = mysql.connector.connect(
    host='mysql.sqlpub.com',
    user='userlys',
    password='b7b573ab3e2a2ed0',
    database='lysupload'
)

# 创建游标对象
cursor = cnx.cursor()

# 执行插入操作
insert_query  = "INSERT INTO wendu (temp, feelsLike, icon, text, wind360, windDir, windScale, windSpeed, humidity, precip, pressure, vis, cloud, dew, now_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
data = (temp, feels_like, icon, text, wind_360, wind_dir, wind_scale, wind_speed, humidity, precip, pressure, vis, cloud, dew, now_time)
cursor.execute(insert_query, data)

# 提交事务并关闭连接
cnx.commit()
cursor.close()
cnx.close()
