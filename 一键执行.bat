@echo off
REM ���� Python ��ִ���ļ�·��
set PYTHON_EXEC=python


REM ִ�� headpdf.py�����ҳü
%PYTHON_EXEC% headpdf.py

REM ִ�� mergepdf.py���ϲ� PDF �ļ�
%PYTHON_EXEC% mergepdf.py

echo �ϲ���ɡ�

@echo off
REM ������Ҫ��յ��ļ���·��
set HEADED_DIR=./headed


REM ɾ�� headed �ļ����е���������
if exist "%HEADED_DIR%" (
    echo ����ɾ�� %HEADED_DIR% �е���������...
    rd /s /q "%HEADED_DIR%"
    mkdir "%HEADED_DIR%"
    echo %HEADED_DIR% ����ա�
) else (
    echo %HEADED_DIR% �ļ��в����ڡ�
)



echo ���в�������ɣ�
pause


