#!/bin/bash

# 函数：实现 ROT13 加密解密
rot13() {
    echo "$1" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
}

# 读取用户输入
read -p "请输入要进行 ROT13 转换的文本: " input_text

# 调用函数并输出结果
encoded_text=$(rot13 "$input_text")
echo "转换后的文本为: $encoded_text"
