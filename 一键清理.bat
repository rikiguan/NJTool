@echo off
set PDF_DIR=./pdf
REM ɾ�� pdf �ļ����е���������
if exist "%PDF_DIR%" (
    echo ����ɾ�� %PDF_DIR% �е���������...
    rd /s /q "%PDF_DIR%"
    mkdir "%PDF_DIR%"
    echo %PDF_DIR% ����ա�
) else (
    echo %PDF_DIR% �ļ��в����ڡ�
)
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

REM ɾ����ǰĿ¼�µ� merged_output.pdf �ļ�
if exist "merged_output.pdf" (
    echo ����ɾ����ǰĿ¼�µ� merged_output.pdf �ļ�...
    del /q "merged_output.pdf"
    echo merged_output.pdf ��ɾ����
) else (
    echo merged_output.pdf �ļ������ڡ�
)

echo ���в�������ɣ�
pause
