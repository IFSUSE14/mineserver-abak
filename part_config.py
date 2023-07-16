from rcon import Client
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
print(conf("rcon", "host"), conf("rcon", "port"), conf("rcon", "password"))