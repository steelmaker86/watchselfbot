@echo off
chcp 65001
echo.
pushd %~dp0

::Attempts to start py launcher without relying on PATH
%SYSTEMROOT%\py.exe --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO attempt
%SYSTEMROOT%\py.exe -3 bot.py
PAUSE
GOTO end
