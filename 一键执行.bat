@echo off
REM 设置 Python 可执行文件路径
set PYTHON_EXEC=python


REM 执行 headpdf.py，添加页眉
%PYTHON_EXEC% headpdf.py

REM 执行 mergepdf.py，合并 PDF 文件
%PYTHON_EXEC% mergepdf.py

echo 合并完成。

@echo off
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



echo 所有操作已完成！
pause


