""" ファイル読み込み用のUtls"""


def load_instructions_file(filename: str, default: str = "") -> str:
    """
    指定されたファイルパスからテキストを読み込みます。

    主にLLMエージェント用の指示文や説明文などを外部ファイルから
    取り込む際に利用するユーティリティ関数です。
    ファイルが存在しない場合や読み込みに失敗した場合は、
    フォールバックとして指定されたデフォルト文字列を返します。

    引数:
        filename (str): 読み込むファイルのパス（相対パスまたは絶対パス）。
        default (str): 読み込みに失敗した場合に返す文字列。

    戻り値:
        str: ファイルの内容（成功時）、またはデフォルト文字列（失敗時）。
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[WARNING] File not found: {filename}. Using default.")
    except Exception as e:
        print(f"[ERROR] Failed to load {filename}: {e}")

    return default
