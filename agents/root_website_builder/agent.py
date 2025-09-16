import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from google.adk.agents import SequentialAgent

from agents.code_writer.agent import code_writer_agent
from agents.designer.agent import designer_agent
from agents.requirements_writer.agent import requirements_writer_agent
from utils.file_loader import load_instructions_file

root_agent = SequentialAgent(
  name = "root_website_builder_agent",
  description=load_instructions_file("agents/root_website_builder/description.txt"),
  sub_agents=[
    requirements_writer_agent,
    designer_agent,
    code_writer_agent
  ],
)
