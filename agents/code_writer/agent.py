import os
import sys

from google.adk.agents import LlmAgent

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))

from tools.file_writer import write_to_file
from utils.file_loader import load_instructions_file

code_writer_agent = LlmAgent(
    name = "code_writer_agent",
    model = "gemini-2.5-flash",
    instruction=load_instructions_file("agents/code_writer/instructions.txt"),
    description=load_instructions_file("agents/code_writer/description.txt"),
    tools=[write_to_file],
)
