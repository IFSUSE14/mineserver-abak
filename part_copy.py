import os
import shutil
world_path = "./test/world" # 服务器世界路径
file_passwd = "are_you_ok?" # 压缩包密码
tempdir = "bakup_name" + "_temp"

def copydirs(from_file, to_file):
    if not os.path.exists(to_file):  # 如不存在目标目录则创建
        os.makedirs(to_file)
    files = os.listdir(from_file)  # 获取文件夹中文件和目录列表
    try:
        files.remove('session.lock')
    except:
        pass
    for f in files:
        if os.path.isdir(from_file + '/' + f):  # 判断是否是文件夹
            copydirs(from_file + '/' + f, to_file + '/' + f)  # 递归调用本函数
        else:
            shutil.copy(from_file + '/' + f, to_file + '/' + f)  # 拷贝文件

copydirs(from_file=world_path,to_file=tempdir)