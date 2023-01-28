from rcon import Client
#from github import Github
import py7zr
import ntplib
import datetime
import shutil
import os
def copydirs(from_file, to_file):
    if not os.path.exists(to_file):  # 如不存在目标目录则创建
        os.makedirs(to_file)
    files = os.listdir(from_file)  # 获取文件夹中文件和目录列表
    for f in files:
        if os.path.isdir(from_file + '/' + f):  # 判断是否是文件夹
            copydirs(from_file + '/' + f, to_file + '/' + f)  # 递归调用本函数
        else:
            shutil.copy(from_file + '/' + f, to_file + '/' + f)  # 拷贝文件
# 保存世界
with Client('127.0.0.1', 25575, passwd='passwd') as client:
    response = client.run('save-all')
print(response)


# 获取ntp时间
ntp_client = ntplib.NTPClient
ntp_host = 'time.windows.com'
ntp_time = ntp_client.request(self=ntp_client,host=ntp_host,version=3,timeout=5)
# 格式化时间
time_now_from_ntp = str(datetime.datetime.fromtimestamp(ntp_time.tx_time)).partition(".")[0].replace(" ","_").replace(":","-")
# 服务器名称
server_name = "test_server"
bakup_name = (server_name + "_" + time_now_from_ntp + ".7z")
print (bakup_name)


world_path = "./test/world" # 服务器世界路径
file_passwd = "are_you_ok?" # 压缩包密码
tempdir = bakup_name + "_temp"
#if not os.path.exists("tempdir"):  # 如不存在目标目录则创建
#        os.makedirs("tempdir")
# 复制函数
def copydirs(from_file, to_file):
    if not os.path.exists(to_file):  # 如不存在目标目录则创建
        os.makedirs(to_file)
    files = os.listdir(from_file)  # 获取文件夹中文件和目录列表
    try:
        files.remove('session.lock') # 不复制session.lock
    except:
        pass
    for f in files:
        if os.path.isdir(from_file + '/' + f):  # 判断是否是文件夹
            copydirs(from_file + '/' + f, to_file + '/' + f)  # 递归调用本函数
        else:
            shutil.copy(from_file + '/' + f, to_file + '/' + f)  # 拷贝文件
# 复制world
copydirs(from_file=world_path,to_file=tempdir)
# 压缩世界
with py7zr.SevenZipFile((server_name + "_" + time_now_from_ntp + ".7z"),'w',password=file_passwd) as archive:
    archive.writeall(tempdir, 'world')
# 保存存档
saves = "saves"
if not os.path.exists(saves):  # 如不存在目标目录则创建
        os.makedirs(saves)
# 处理临时文件
shutil.copy(bakup_name,saves)
os.remove(bakup_name)
shutil.rmtree(tempdir)