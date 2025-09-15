# master-google-adk-cource

Udemy の ADK 講座の onboarding

## sample repository

https://github.com/theailanguage/adk_samples

## Python 側の設定

- uv を install しておいてください。
- 各 project の pyproject.toml と同階層で以下を実行してください。

```
# Pythonの仮想環境の有効化
$ uv venv
$ .venv\Scripts\activate

# project setup
$ uv sync
```

## 環境変数

### .env

各種 pyproject.toml と同じ階層に配置してください。

必要な環境変数一覧は [env_parameters.md](./env_parameters.md) を参照

### GOOGLE_API_KEY の取得方法(.env GOOGLE_API_KEY に設定)

- (1) 以下にアクセス -> Get API key を押下
  https://aistudio.google.com/prompts/new_chat

- (2) Gemini API をすばやくテスト...のページの右上の API キーを作成から API キーを生成してください。
  - 既存の Project 選択..と出てきたら一覧に出てくる Gemini API を選択しましょう。(Plan が Free になっていること。)
  - 不要になった際は API Key は削除してください。
