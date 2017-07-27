@ECHO OFF
PUSHD %~DP0
TITLE Sublime Text (添加/删除右键菜单)
echo.&echo 添加 Sublime Text 右键菜单
echo.&echo 删除 Sublime Text 右键菜单
echo.&echo.
set /p a= 输入数字回车：
if "%a%"=="y" Goto AddWebDetect
if "%a%"=="n" Goto AddYunShell
SET /P ST=输入y添加右键菜单，输入n删除右键菜单：
if /I "%ST%"=="y" goto Add
if /I "%ST%"=="n" goto Remove
:Add
reg add "HKEY_CLASSES_ROOT\*\shell\SublimeText3" /ve /t REG_SZ /d "用 &SublimeText 打开" /f
reg add "HKEY_CLASSES_ROOT\*\shell\SublimeText3\command" /ve /t REG_SZ /d "\"%~dp0sublime_text.exe\" ""%%1""" /f
SET E=完成!&GOTO MSGBOX
:Remove
reg delete "HKLM\SOFTWARE\Classes\*\shell\SublimeText3" /f
reg delete "HKLM\SOFTWARE\Classes\Directory\shell\SublimeText3" /f
reg delete "HKLM\SOFTWARE\Classes\Directory\shell\SublimeText3" /f
reg delete "HKEY_CLASSES_ROOT\*\shell\SublimeText3" /f
SET E=完成!&GOTO MSGBOX
:MsgBox
if "%1"=="" mshta VBScript:MsgBox("%e%",vbSystemModal,"")(close)& Cls&Goto Menu