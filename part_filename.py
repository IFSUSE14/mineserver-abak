import ntplib
import datetime
# 获取ntp时间
ntp_client = ntplib.NTPClient
ntp_host = 'time.windows.com'
ntp_time = ntp_client.request(self=ntp_client,host=ntp_host,version=3,timeout=5)
# 格式化时间
time_now_from_ntp = str(datetime.datetime.fromtimestamp(ntp_time.tx_time)).partition(".")[0].replace(" ","_")
#time_now_from_ntp = str(time_now_from_ntp)
#time_now_from_ntp = (time_now_from_ntp.partition(".")[0].replace(" ","_"))
# 服务器名称
server_name = "test_server"
bakup_name = server_name + "_" + time_now_from_ntp
print (bakup_name)