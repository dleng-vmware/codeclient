@echo off&setlocal enabledelayedexpansion
rem 读取index1.txt所有内容
for /f "eol=* tokens=*" %%i in (D:\l10ntest\PythonClient\8.0.0\about\messages_de.json) do (
rem 设置变量a为每行内容
set a=%%i
rem 如果该行有0:0，则将其改为4:0
set "a=!a:1234="test de key"!"
rem 把修改后的全部行存入$
echo !a!>>$ )
rem 用$的内容替换原来index1.txt内容
move $ D:\l10ntest\PythonClient\8.0.0\about\messages_de.json