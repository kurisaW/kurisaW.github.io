import os
import re

# 读取博客目录下的所有二级目录
blog_directory = 'content/post'  # 替换为你的博客目录路径
subdirectories = [dir for dir in os.listdir(blog_directory) if os.path.isdir(os.path.join(blog_directory, dir))]

# 从每个博客目录的index.md文件中提取日期和标题
blog_posts = []
for dir in subdirectories:
    index_path = os.path.join(blog_directory, dir, 'index.md')
    with open(index_path, 'r', encoding='utf-8') as file:
        content = file.read()
        date_match = re.search(r'data:\s*(\d{4}-\d{2}-\d{2})', content)
        title_match = re.search(r'# (.+)', content)
        date = date_match.group(1) if date_match else 'N/A'
        title = title_match.group(1) if title_match else 'Untitled'
        link = f'https://github.com/yourusername/yourrepo/blob/main/blogs/{dir}/index.md'
        blog_posts.append({'date': date, 'title': title, 'link': link})

# 排序博客文章并选择最近的10篇
sorted_posts = sorted(blog_posts, key=lambda x: x['date'], reverse=True)[:10]

# 生成Markdown表格
markdown_table = f"""
| UpdateTime | Title | Summary |
| ---------- | ----- | ------- |
{''.join([f"| {post['date']} | [{post['title']}]({post['link']}) |  |\n" for post in sorted_posts])}

# 更新README.md文件
readme_path = 'README.md'  # 替换为你的README.md路径
with open(readme_path, 'r', encoding='utf-8') as file:
    readme_content = file.read()
    updated_readme = re.sub(r'(## `✍️ Recent Posts`)([\s\S]*?)(\n##)', rf'\1{markdown_table}\3', readme_content)

with open(readme_path, 'w', encoding='utf-8') as file:
    file.write(updated_readme)
