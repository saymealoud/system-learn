from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 使用 lxml 作为解析器
soup = BeautifulSoup(html, 'lxml')

# 查看整个文档，格式化输出
print(soup.prettify())

# 获取并打印 <title> 标签的内容
print("Title tag:", soup.title)
print("Title string:", soup.title.string)

# 获取并打印第一个 <p> 标签
print("First p tag:", soup.p)

# 获取并打印 <title> 标签的名称
print("Title tag name:", soup.title.name)

# 获取并打印第一个 <p> 标签的所有属性
print("Attributes of first p tag:", soup.p.attrs)

# 打印特定属性
print("Name attribute of p:", soup.p['name'])
print("Class attribute of p:", soup.p['class'])
