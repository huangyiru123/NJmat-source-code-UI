#!/bin/bash

# 检查是否安装了conda
if command -v conda &> /dev/null; then
    echo "Found conda installed"
    
    # 检查是否存在NJmat环境
    if ! conda env list | grep -q '\sNJmat\s'; then
        echo "Creating NJmat environment"
        conda create -n NJmat python
    fi
    
    # 进入当前目录
    cd "$(dirname "$(readlink -f "$0")")"
    
    # 激活NJmat环境
    source activate NJmat
    
    # 安装pyinstaller
    pip install pyinstaller
    
    # 使用pyinstaller构建应用
    pyinstaller NJmat.spec
    echo "Successfully built application using pyinstaller."
else
    echo "Conda not found, installing dependencies using pip directly."
    
    # 进入当前目录
    cd "$(dirname "$(readlink -f "$0")")"
    
    # 安装pyinstaller
    pip install pyinstaller
    
    # 使用pyinstaller构建应用
    pyinstaller NJmat.spec
    echo "Successfully built application using pyinstaller."
fi