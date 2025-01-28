import re

def extract_sources_and_contents(text):
    # Split the text by the delimiter
    entries = text.split('***** /n')
    
    # Skip the first empty entry if it exists
    entries = entries[1:] if entries[0].strip() == '' else entries
    
    # Formatting result directly as a string
    result = []
    for entry in entries:
        # Extract source
        source_match = re.search(r"source='(\w+)'", entry)
        source = source_match.group(1) if source_match else 'Unknown'
        
        # Extract content
        content_match = re.search(r"content=(['\"].*?['\"])", entry, re.DOTALL)
        if content_match:
            # Remove surrounding quotes and handle potential multiline content
            content = content_match.group(1).strip("'\"")
            
            # Use replace to convert escaped newlines to actual newlines
            content = content.replace('\\n', '\n')
            
            # Append to result list
            result.append(f"Source: {source}\nContent: {content}")
    
    return '\n\n'.join(result)


def parse_last_content(text_string):
    """
    Parse the last content from the given string and convert markdown to formatted text.
    
    Args:
        text_string (str): Input string containing the content
    
    Returns:
        str: Formatted text without markdown
    """
    # Find all content fields
    content_pattern = r"content='(.*?)',"
    matches = re.findall(content_pattern, text_string, re.DOTALL)
    
    if not matches:
        return "No content found"
    
    # Get the last content
    last_content = matches[-1]


    # if last_content:
    #     # Remove surrounding quotes and handle potential multiline content
    #     text = last_content.group(1).strip("'\"")
        
    #     # Use replace to convert escaped newlines to actual newlines
    #     text = text.replace('\\n', '\n')
        
    
    # Convert markdown headers to plain text
    # Replace ### with newline and bold
    text = re.sub(r'###\s*(.*?)\n', r'\n\1:\n', last_content)
    
    # Convert markdown bullet points to proper format
    text = re.sub(r'-\s*(.*?):\s*€', r'  • \1: €', text)
    
    # Use replace to convert escaped newlines to actual newlines
    text = text.replace('\\n', '\n')
    
    # Remove any remaining markdown symbols
    text = text.strip()
    
    return text


# import os
# import sys
# import asyncio
# from autogen_agentchat.base import Response, TaskResult
# from autogen_core import Image
# from autogen_agentchat.messages import AgentEvent, ChatMessage, MultiModalMessage
# from typing import List


# def _is_running_in_iterm() -> bool:
#     return os.getenv("TERM_PROGRAM") == "iTerm.app"

# def _is_output_a_tty() -> bool:
#     return sys.stdout.isatty()

# render_image_iterm = _is_running_in_iterm() and _is_output_a_tty() 

# # iTerm2 image rendering protocol: https://iterm2.com/documentation-images.html
# def _image_to_iterm(image: Image) -> str:
#     image_data = image.to_base64()
#     return f"\033]1337;File=inline=1:{image_data}\a\n"

# def _message_to_str(message: AgentEvent | ChatMessage, *, render_image_iterm: bool = False) -> str:
#     if isinstance(message, MultiModalMessage):
#         result: List[str] = []
#         for c in message.content:
#             if isinstance(c, str):
#                 result.append(c)
#             else:
#                 if render_image_iterm:
#                     result.append(_image_to_iterm(c))
#                 else:
#                     result.append("<image>")
#         return "\n".join(result)
#     else:
#         return f"{message.content}"

# def format_stream(stream):
#     last_processed = None  # Initialize to avoid UnboundLocalError

#     for message in stream:
#         if isinstance(message, TaskResult): 
#             # mypy ignore
#             last_processed = message  # type: ignore

#         elif isinstance(message, Response):
#             # Print final response.
#             output = f"{'-' * 10} {message.chat_message.source} {'-' * 10}\n{_message_to_str(message.chat_message, render_image_iterm=render_image_iterm)}\n"

#             # mypy ignore
#             last_processed = message  # type: ignore
#         # We don't want to print UserInputRequestedEvent messages, we just use them to signal the user input event.
#         # elif isinstance(message, UserInputRequestedEvent):
#         #     if user_input_manager is not None:
#         #         user_input_manager.notify_event_received(message.request_id)
#         else:
#             # Cast required for mypy to be happy
#             message = cast(AgentEvent | ChatMessage, message)  # type: ignore
#             output = f"{'-' * 10} {message.source} {'-' * 10}\n{_message_to_str(message, render_image_iterm=render_image_iterm)}\n"

#     if last_processed is None:
#         raise ValueError("No TaskResult or Response was processed.")

#     return last_processed