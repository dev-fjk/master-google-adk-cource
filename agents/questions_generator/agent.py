import os
import sys

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..","..")))

from utils.file_loader import load_instructions_file

questions_generator_agent = LlmAgent(
    name = "questions_generator_agent",
    model = "gemini-2.0-flash",
    instruction=load_instructions_file("agents/questions_generator/instructions.txt"),
    description=load_instructions_file("agents/questions_generator/description.txt"),
    tools=[google_search],
    output_key="questions_generator_output"
)
