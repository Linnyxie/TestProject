import time


now = time.time()
print("无格式的时间：", now)

now_format = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("格式化的时间：", now_format)

print("测试任务关联源码提交-1。")
print("测试缺陷关联源码提交-1。")
