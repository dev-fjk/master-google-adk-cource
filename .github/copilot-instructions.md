# Copilot Instructions for master-google-adk-cource

## プロジェクト概要

- Google ADK (Agent Development Kit) を活用したエージェント開発の学習リポジトリ。
- `agents/` ディレクトリに各種エージェント（code_writer, designer, query_generator など）がサブディレクトリ単位で実装されている。
- `agent_runner.py` で CLI 実行、`adk web ./agents` で Web UI 実行が可能。

## 主要構成・ファイル

- `main.py` : プロジェクトのエントリーポイント（主に Web UI 用）。
- `agent_runner.py` : CLI 実行用のランナー。
- `agents/` : 各エージェントの実装。各サブディレクトリに `agent.py`、説明・指示ファイル（description.txt, instructions.txt）が存在。
- `tools/` : 補助ツール（例: file_writer.py）。
- `utils/` : ユーティリティ（例: file_loader.py）。
- `output/` : 生成された HTML ページ等の成果物。
- `images/` : 実行例や生成物のスクリーンショット。

## 開発・実行フロー

- Python 仮想環境は `uv` を利用（`uv venv` → `.venv\Scripts\activate` → `uv sync`）。
- CLI 実行: `python agent_runner.py`
- Web UI 実行: `adk web ./agents` → `http://127.0.0.1:8000/dev-ui/` でアクセス。
- 環境変数は `.env` ファイルで管理。`GOOGLE_API_KEY` は自身で払い出した Key を設定してください。

## コーディング規約・パターン

- 各エージェントは `agent.py` にクラス/関数として実装。指示・説明は txt ファイルで分離。
- ディレクトリ構成・命名はエージェント名で統一。
- 外部サービス（Google Gemini API 等）との連携は環境変数で制御。
- 生成物（HTML 等）は `output/` に保存。

## 重要なワークフロー例

- 新規エージェント追加: `agents/新エージェント名/` を作成し、`agent.py`・説明・指示ファイルを配置。
- 依存管理: `pyproject.toml` と `uv.lock` で管理。`uv sync` でセットアップ。
- デバッグ: CLI 実行時は `agent_runner.py`、Web UI 実行時は `adk web` のログを参照。

## 各エージェントの説明

### code_writer

自動化されたフロントエンド開発者として機能し、設計仕様・機能要件を CSS/JavaScript 込みの単一 HTML ファイルに変換します。細部まで配慮した HTML 生成が特徴。

### designer

自動 UI/UX デザイナー。機能要件を詳細なビジュアルブループリント（色・タイポグラフィ・レイアウト・コンポーネントスタイル）に変換し、Markdown 形式で定義します。

### query_generator

5 つの質問リサーチャーエージェント全てからのリサーチ出力を取得し、要件ライターエージェント向けに統合クエリを生成します。

### questions_generator

ユーザーからトピックを受け取り、Google 検索を使って調査し、理解を深めるための重要な 5 つの質問のみを生成します（回答は提供しません）。

### questions_researcher

questions_generator で生成された質問に対し、5 つの専門調査エージェントが並行して回答。各エージェントは Google 検索を活用し、特定質問の調査・回答に注力します。

### requirements_writer

ウェブページ構築に関連するユーザークエリを受け取り、詳細な要件セットに変換します。

### root_website_builder

指定された順序でサブエージェントを実行するシーケンシャルエージェント。

## 注意点

- 各エージェントの設計思想や役割は description.txt/instructions.txt を必ず参照。
- ルート直下の .env, pyproject.toml, uv.lock の整合性を保つこと。
- 生成物やログは output/・images/ に保存される。

---

このドキュメントは AI コーディングエージェント向けのガイドです。不明点や追加情報が必要な場合は、README.md も参照してください。
