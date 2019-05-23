@ECHO off

Set DateCheck
START C:\xamp\apache\bin\httpd.exe
START C:\xamp\mysql\bin\mysqld.exe --defaults-file=C:\xamp\mysql\bin\my.ini --standalone --console
python E:\CameraHealthManagementSystem\TamperProof.py

PAUSE