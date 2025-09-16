import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from google.adk.agents import LlmAgent

from utils.file_loader import load_instructions_file

designer_agent = LlmAgent(
  name = "designer_agent",
  model="gemini-2.5-flash",
  instruction=load_instructions_file("agents/designer/instructions.md"),
  description=load_instructions_file("agents/designer/description.txt"),
  output_key="designer_output"
)
