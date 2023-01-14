#! /usr/local/bin/python3
from datetime import datetime

# HTTPレスポンスヘッダーを指定.
print('Content-Type: text/html')
print('')

# HTML本文の作成と送信.
html = """
<html>
    <body>
        <h1>ようこそ! Python x CGI</h1>
        <p>現在時刻は「{0}」です。</p>
    </body>
</html>
""".format(datetime.now().strftime("%Y/%m/%d(%A) %H:%M:%S"))
print(html)
