from rcon.source import Client
#from github import Github
import py7zr
import ntplib
import datetime
import shutil
import os
import configparser
#初始化配置
conf_n = "bak.conf"
# 创建配置文件
if not os.path.exists(conf_n):
    print("初始化配置...")
    with open(conf_n, "w+", encoding="utf-8") as wf:
        wf.write("[conf]\n#当该选项为 false 时,程序不会运行\nrun=false\n[rcon]\n# rcon 服务端信息\nhost=127.0.0.1\nport=25575\npassword=passwd\n[compression]\n# 服务器名称\nserver_name=server_name\n# 服务器存档路径\nworld_path=/path/to/saves\n# 压缩密码\nfile_password=passwd")
config = configparser.ConfigParser()
config.read(conf_n, encoding="utf-8")
conf = config.get
# 检测配置是否被更改
if conf("conf", "run") == "false":
    print("请更改bak.conf以运行该程序")
    exit()
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
# 保存世界
with Client(host=conf("rcon", "host"), port=int(conf("rcon", "port")), passwd=conf("rcon", "password")) as client:
    response = client.run('save-all')
if response == "Saving the game (this may take a moment!)Saved the game":
    print("保存中")


# 获取ntp时间
ntp_client = ntplib.NTPClient
ntp_host = 'time.windows.com'
ntp_time = ntp_client.request(self=ntp_client,host=ntp_host,version=3,timeout=5)
# 格式化时间
time_now_from_ntp = str(datetime.datetime.fromtimestamp(ntp_time.tx_time)).partition(".")[0].replace(" ","_").replace(":","-")
bakup_name = (conf("compression", "server_name") + "_" + time_now_from_ntp + ".7z")
print ("备份名: ", bakup_name)

tempdir = bakup_name + "_temp"
#if not os.path.exists("tempdir"):  # 如不存在目标目录则创建
#        os.makedirs("tempdir")
# 复制world
copydirs(from_file=conf("compression", "world_path"),to_file=tempdir)
# 压缩世界
with py7zr.SevenZipFile((conf("compression","server_name") + "_" + time_now_from_ntp + ".7z"),'w',password=conf("compression", "file_password")) as archive:
    archive.writeall(tempdir, 'world')
# 保存存档
saves = "saves"
if not os.path.exists(saves):  # 如不存在目标目录则创建
        os.makedirs(saves)
# 处理临时文件
shutil.copy(bakup_name,saves)
os.remove(bakup_name)
shutil.rmtree(tempdir)