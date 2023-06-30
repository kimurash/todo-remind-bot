# todo_reminder_bot
[Todoist](https://todoist.com/ja)から
期限が今日に設定されているタスクを選抜してDiscordに通知するBot  
$\rightarrow$ 
[開発記事](https://esa-pages.io/p/sharing/19485/posts/15/e201cf1359bd9cbc3561.html)

## 使用しているライブラリ
- [discord.py](https://discordpy.readthedocs.io/ja/latest/index.html)
- [todoist-api-python](https://developer.todoist.com/guides/#developing-with-todoist)

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