string = 'hello'
print(string.isalnum())     # 所有字符都是数字或者字母
print(string.isalpha())     # 所有字符都是字母
print(string.isdigit())     # 所有字符都是数字
print(string.islower())     # 所有字符都是小写
print(string.isupper())     # 所有字符都是大写
print(string.istitle())     # 所有单词都是首字母大写，像标题
print(string.isspace())     # 所有字符都是空白字符、\t、\n、\r
print(string.find("ll"))     # 从左开始查找， 不存在返回-1
print(string.rfind("ll"))     # 从右开始查找， 不存在返回-1
print(string.index("ll"))     # 从左开始查找， 不存在抛异常
print(string.rindex("ll"))     # 从右开始查找， 不存在抛异常
print(string.endswith("llo"))     # 结束于
print(string.startswith("hell"))     # 开始于