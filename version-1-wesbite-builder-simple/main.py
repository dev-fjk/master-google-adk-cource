import asyncio
import json
from typing import Any

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from rich import print as rprint
from rich.syntax import Syntax

from agents.website_builder.agent import root_agent

load_dotenv()

APP_NAME = "website_builder_app"
USER_ID = "user_12345"
SESSION_ID = "session_chat_loop_1"

async def chat_loop():
    """ Agentとセッションを初期化するチャットループ
    1. セッションを作成し、会話履歴を保持する
    2. ユーザーからの問い合わせを受け付ける
    3. エージェントに問い合わせを送り、イベントストリームを受け取る
    """

    print("エージェントチャットセッションを開始しました。")
    print("終了するには 'quit', 'exit', または ':q' と入力してください。\n")

    # --- セッションのセットアップ（1回だけ） ---
    # InMemorySessionService は会話履歴を保持します
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    # Runner はエージェントの処理を実行するエンジンです
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    while True:
        user_query = input("問い合わせを入力してください: ")
        if user_query.lower() in ["quit", "exit", ":q"]:
            print("チャットセッションを終了します。さようなら！")
            break

        # --- エージェントへの問い合わせ ---
        # ユーザーの入力をエージェントが理解できる形式に変換
        new_message = Content(role="user", parts=[Part(text=user_query)])
        events = runner.run_async(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=new_message
        )

        final_response = ""
        i = 0
        async for event in events:
            i += 1
            print_json_response(event, f"============イベント #{i}=============")
            if hasattr(event, "author") and event.author == "code_writer_agent":
                if event.is_final_response():
                    # 最終応答を取り出す
                    final_response = event.content.parts[0].text
                    # 見やすく表示
                    print(f"\nエージェントの応答:\n------------------------\n{final_response}\n")
                    break


def print_json_response(response: Any, title: str) -> None:
    """ レスポンスをJSON形式で色付き表示するユーティリティ

    Args:
        response (Any): 表示するレスポンスオブジェクト
        title (str): 表示タイトル
    """
    print(f"\n=== {title} ===")
    try:
        if hasattr(response, "root"):
            data = response.root.model_dump(mode="json", exclude_none=True)
        else:
            data = response.model_dump(mode="json", exclude_none=True)

        json_str = json.dumps(data, indent=2, ensure_ascii=False)
        syntax = Syntax(json_str, "json", theme="monokai", line_numbers=False)
        rprint(syntax)
    except Exception as e:
        rprint(f"[red bold]JSON表示中にエラー:[/red bold] {e}")
        rprint(repr(response))


# --- プログラム起点 ---
if __name__ == '__main__':
    asyncio.run(chat_loop())
