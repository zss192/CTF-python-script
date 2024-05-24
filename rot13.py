# 导入所需库
import string

def rot13(text):
    """
    实现ROT13加密解密的函数。
    
    参数:
    text (str): 需要进行ROT13转换的文本。
    
    返回:
    str: 经过ROT13转换的文本。
    """
    # 定义ROT13转换表，大小写字母分别处理
    rot13_trans = str.maketrans(
        string.ascii_uppercase + string.ascii_lowercase,
        string.ascii_uppercase[13:] + string.ascii_uppercase[:13] +
        string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    )
    # 使用转换表进行转换
    return text.translate(rot13_trans)

# 读取用户输入
input_text = input("请输入要进行 ROT13 转换的文本: ")

# 调用函数并输出结果
encoded_text = rot13(input_text)
print("转换后的文本为:", encoded_text)
