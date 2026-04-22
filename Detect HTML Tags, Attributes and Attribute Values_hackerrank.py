from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")
n = int(input())
html_content = ""
for _ in range(n):
    html_content += input().rstrip() + "\n"
parser = MyHTMLParser()
parser.feed(html_content)
