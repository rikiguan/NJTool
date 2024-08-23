@echo off
set PDF_DIR=./pdf
REM 删除 pdf 文件夹中的所有内容
if exist "%PDF_DIR%" (
    echo 正在删除 %PDF_DIR% 中的所有内容...
    rd /s /q "%PDF_DIR%"
    mkdir "%PDF_DIR%"
    echo %PDF_DIR% 已清空。
) else (
    echo %PDF_DIR% 文件夹不存在。
)
REM 设置需要清空的文件夹路径
set HEADED_DIR=./headed
REM 删除 headed 文件夹中的所有内容
if exist "%HEADED_DIR%" (
    echo 正在删除 %HEADED_DIR% 中的所有内容...
    rd /s /q "%HEADED_DIR%"
    mkdir "%HEADED_DIR%"
    echo %HEADED_DIR% 已清空。
) else (
    echo %HEADED_DIR% 文件夹不存在。
)

REM 删除当前目录下的 merged_output.pdf 文件
if exist "merged_output.pdf" (
    echo 正在删除当前目录下的 merged_output.pdf 文件...
    del /q "merged_output.pdf"
    echo merged_output.pdf 已删除。
) else (
    echo merged_output.pdf 文件不存在。
)

echo 所有操作已完成！
pause
