
''' import LAZYCOOK
import asyncio
import os
from LAZYCOOK import RichMultiAgentCLI  # or MultiAgentAssistantConfig

config=LAZYCOOK.create_assistant(api_key="AIzaSyD7ebIM0FrCgiIgseVF4lwcWjTaPyz4r4M",conversation_limit=70)
# Run CLI
asyncio.run(config.run_cli())


# Or create assistant instance directly
assistant=config.create_assistant()


import asyncio
from demo10 import MultiAgentAssistantConfig
import os

api_key = os.getenv("AIzaSyDxlwcteTa6hqaD6J7Yn6b4SIpzNByph6Y")
config = MultiAgentAssistantConfig(api_key, conversation_limit=70)
asyncio.run(config.run_cli())
'''

import LazyCook7
import asyncio

# Create configured assistant factory
config = LazyCook7.create_assistant("AIzaSyDxlwcteTa6hqaD6J7Yn6b4SIpzNByph6Y", conversation_limit=0)



# Run CLI - config is a MultiAgentAssistantConfig, not AutonomousMultiAgentAssistant
from rich.console import Console
from rich.prompt import Prompt

console = Console()
console.print("\n[bold cyan]🤖 Select LLM Backend:[/bold cyan]")
console.print("1. Gemini (Cloud-based, requires API key)")
console.print("2. Gemma 2.2B (Local, requires GPU/CPU)")

backend_choice = Prompt.ask("Choose backend (1 or 2)", choices=["1", "2"], default="1")

llm_config = LazyCook7.LLMConfig()
if backend_choice == "2":
    llm_config.backend = "gemma"
    console.print("[bold yellow]⚠️ Loading Gemma 2.2B model...[/bold yellow]")
else:
    llm_config.backend = "gemini"

# Pass llm_config to CLI
cli = config.create_cli()
cli.assistant.multi_agent_system = LazyCook7.MultiAgentSystem(
    "AIzaSyDxlwcteTa6hqaD6J7Yn6b4SIpzNByph6Y",
    llm_config
)

asyncio.run(config.run_cli())


