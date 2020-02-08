import psutil

def get_disk_info():
    content = ""
    for disk in psutil.disk_partitions():
        if 'cdrom' in disk.opts or disk.fstype =='':
            continue 
        disk_name_arr = disk.device.split(":")
        disk_name = disk_name_arr[0]
        disk_info = psutil.disk_usage(disk.device)
        free_disk_size = disk_info.free//1024//1024//1024
        info = "%s盘使用率:%s%%，剩余空间：%iG \n" % (disk_name,str(disk_info.percent) ,free_disk_size)
        content = content + info 
    print(content)

get_disk_info()