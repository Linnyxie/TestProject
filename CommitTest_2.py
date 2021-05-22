import time


now = time.time()
print("无格式的时间：", now)

now_format = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("格式化的时间：", now_format)

print("增加一点打印，确认提交后TAPD端的源码关联效果——1。")
