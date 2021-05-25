:: Windows环境
::
:: 本文件用于拷贝commit-msg文件至.git\hooks目录

@echo off
xcopy commit-msg ..\.git\hooks\
exit
