import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from google.adk.agents import LlmAgent

from tools.file_writer import write_to_file
from utils.file_loader import load_instructions_file

root_agent = LlmAgent(
  name = "website_builder_agent",
  model="gemini-2.0-flash-001",
  instruction=load_instructions_file("agents/website_builder/instructions.txt"),
  description=load_instructions_file("agents/website_builder/description.txt"),
  tools=[write_to_file],
)
