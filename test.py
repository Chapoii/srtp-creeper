import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://k.sina.com.cn/article_1887344341_707e96d501901cneh.html?from=news&subch=onews"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Content-Type": "text/html; charset=utf-8"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content.decode("utf-8"), "html.parser")

# 找到需要爬取的数据所在的标签和属性
title = soup.find("h1", {"class": "main-title"}).text.encode("utf-8").decode()
content = soup.find("div", {"class": "article"})("p")

content_text = ""
for p in content:
    content_text += p.text.encode("utf-8").decode().strip() + "\n"

print("标题：", title)
print("内容：", content_text)

data = {"标题": [title], "内容": [content_text]}
df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False)

print("数据已保存到 output.xlsx 文件中。")
