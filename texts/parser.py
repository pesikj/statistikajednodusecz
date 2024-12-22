import re
from markdownify import markdownify as md

regex = re.compile(r"<!--[ \w:\-\/\{\}\"]*-->")

with open("temp.md", encoding="utf-8") as file:
    content = file.read()
    content = regex.sub("", content)
    content = md(content)
    content = content.replace("$latex", "$")

with open("temp_converted.md", "w", encoding="utf-8") as file:
    file.write(content)
