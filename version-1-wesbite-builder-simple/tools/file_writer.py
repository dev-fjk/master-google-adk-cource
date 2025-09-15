""" HTMLファイル出力用のMCP Tools """

from datetime import datetime
from pathlib import Path


def write_to_file(content: str) -> dict:
  """ HTMLファイルを生成しoutputディレクトリに保存する

  Args:
      content (str): contents

  Returns:
      dict: dict
  """
  timestamp: str = datetime.now().strftime("%y%m%d_%H%M%S")
  filepath: str = f"output/{timestamp}_generated_page.html"

  Path("output").mkdir(exist_ok=True)
  Path(filepath).write_text(content, encoding="utf-8")

  return {
    "status": "success",
    "file": filepath,
  }
