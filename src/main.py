import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv

from task_manager import TaskManager

# .envから環境変数を取得する
load_dotenv()

# Intentsを設定すると受け取るイベントを制限できる
intents = discord.Intents.default()
# 接続に必要なオブジェクトを生成
client = discord.Client(intents=intents)

task_manager = TaskManager()

@client.event
async def on_ready(): # 起動時に動作する処理
    print('Login')
    send_reminder.start() # ループ処理実行

@tasks.loop(hours=24)
async def send_reminder():
    embed = discord.Embed(  # 埋め込みテキストを定義
        title='Todoist',
        color=0xFF4500, # フレーム色
        description='Today\'s Task(s)', # Embedの説明文
        url='https://todoist.com/ja' # タイトルが指定URLへのリンクになる
    )

    # サムネイルとして小さい画像を設定
    embed.set_thumbnail(url='https://www.python.org/static/img/python-logo@2x.png')

    tasks = task_manager.get_today_task()
    for task in tasks:
        # フィールドを追加
        embed.add_field(
            name=f':ballot_box_with_check: {task.content}',
            value=f'{task.due.datetime}',
            inline=False
        )

    # フッターに開発者の情報を入れる
    embed.set_footer(text='made by shunsei',)

    channel_id = os.getenv('DISCORD_TEST_CHANNEL_ID')
    channel = client.get_channel(int(channel_id))
    await channel.send(embed=embed)

# Botの起動とDiscordサーバーへの接続
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
client.run(TOKEN)