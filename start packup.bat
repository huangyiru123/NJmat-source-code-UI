@echo off

rem 检查是否安装了conda
set conda_loc=
where conda > nul 2>&1
if %ERRORLEVEL% EQU 0 (
    rem conda存在
    echo Found conda installed
    rem 检查是否存在NJmat环境
    conda env list | findstr /C:" NJmat" > nul 2>&1
    if %ERRORLEVEL% NEQ 0 (
        echo Creating NJmat environment
        conda create -n NJmat python
    )
    rem 进入当前目录
    cd /d %~dp0
    rem 激活NJmat环境
    call conda activate NJmat
    rem 安装pyinstaller
    pip install pyinstaller
    rem 使用pyinstaller构建应用
    pyinstaller NJmat.spec
    echo Successfully built application using pyinstaller.
) else (
    rem conda不存在
    echo Conda not found, installing dependencies using pip directly.
    rem 进入当前目录
    cd /d %~dp0
    rem 安装pyinstaller
    pip install pyinstaller
    rem 使用pyinstaller构建应用
    pyinstaller NJmat.spec
    echo Successfully built application using pyinstaller.
)