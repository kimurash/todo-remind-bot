# todo_reminder_bot
[Todoist]([Todoist]) から期限が今日に設定されているタスクを選抜して
Discordに通知するBot  
$\rightarrow$ [開発記事]([article])

## 使用しているライブラリ
- [discord.py]([discord.py])
- [todoist-api-python]([todoist-api-python])

## ディレクトリ構成
```
┬
│  .gitignore
│  poetry.lock
│  pyproject.toml
│  README.MD
│  
└─src
    │  main.py
    │  task_manager.py
    ┴
```

## 実行方法
```
python main.py
```

[Todoist]:https://todoist.com/ja
[article]:https://esa-pages.io/p/sharing/19485/posts/15/e201cf1359bd9cbc3561.html
[discord.py]:https://discordpy.readthedocs.io/ja/latest/index.html
[todoist-api-python]:https://developer.todoist.com/guides/#developing-with-todoist
