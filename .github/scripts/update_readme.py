import yaml
from datetime import datetime

# 遍历博客目录,解析每个post的日期
posts = [] 

for post in get_posts("content/post"):
  date = parse_date(post)
  posts.append({'date': date, 'title': post['title']})

# 按日期排序  
posts.sort(key=lambda x: x['date'], reverse=True)

# 取最近10篇
posts = posts[:10] 

# 生成Markdown表格
table = """
| Date | Title |
|-|-| 
"""

for post in posts:
  table += f"| {post['date']} | {post['title']} |\n"
  
# 插入README.md  
readme = read_file('README.md')  
readme = insert_after(readme, "<!-- BLOG_DIARY -->", table)
write_file('README.md', readme)