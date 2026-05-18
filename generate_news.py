import os
import json
from datetime import datetime, timezone, timedelta

# 设置为东八区时间 (北京/香港时间)
tz = timezone(timedelta(hours=8))
now = datetime.now(tz)
date_str = now.strftime('%Y-%m-%d')
time_str = now.strftime('%Y-%m-%d %H:%M:%S')

# 1. 模拟的今日新闻数据
news_data = {
    "date": date_str,
    "update_time": time_str,
    "title": f"今日头条：{date_str} 新闻简报",
    "content": "这是由 GitHub Actions 每天自动执行 Python 脚本抓取/生成的今日新闻内容。你可以在这里接入真实的 API 来替换这段文本！",
    "author": "GitHub 自动化机器人"
}

# 2. 确保 docs 文件夹存在
os.makedirs('docs', exist_ok=True)

# 3. 将数据保存为 latest.json
json_path = os.path.join('docs', 'latest.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(news_data, f, ensure_ascii=False, indent=4)

# 4. 生成简单的网页 index.html
html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>每日新闻 - {date_str}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; background-color: #f4f4f9; color: #333; }}
        .card {{ background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
        .meta {{ color: #7f8c8d; font-size: 0.9em; margin-bottom: 20px; }}
        .content {{ font-size: 1.1em; line-height: 1.6; }}
        .footer {{ text-align: center; margin-top: 30px; color: #aaa; font-size: 0.8em; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{news_data['title']}</h1>
        <div class="meta">
            <span>📅 更新时间: {news_data['update_time']}</span> | 
            <span>🤖 作者: {news_data['author']}</span>
        </div>
        <div class="content">
            <p>{news_data['content']}</p>
        </div>
    </div>
    <div class="footer">
        本页面由 GitHub Actions + Python 自动构建并部署至 GitHub Pages
    </div>
</body>
</html>
"""

html_path = os.path.join('docs', 'index.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ 成功生成文件: {html_path} 和 {json_path}")
