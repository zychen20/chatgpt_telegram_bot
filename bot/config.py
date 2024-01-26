import yaml
from pathlib import Path
import os

config_dir = Path(__file__).parent.parent.resolve() / "config"

# config parameters
openai_api_base = None
new_dialog_timeout = 600  # new dialog starts after timeout (in seconds)
enable_message_streaming = True # SSE
return_n_generated_images = 1
image_size = "512x512"
n_chat_modes_per_page = 5

def getEnv(key):
    value = os.getenv(key)
    # if no such environment variable, return empty string
    return value if value else ""

# api keys, tokens and DB url
telegram_token = getEnv("telegram_token")
openai_api_key = getEnv("openai_api_key")
mongodb_uri = getEnv("mongodb_uri")
# if `allowed_telegram_usernames` & `allowed_telegram_ids` are empty, the bot is available to anyone. 
# pass a username string to allow him/her
allowed_telegram_usernames = getEnv("username_whitelist").split(',')
# pass user ids as positive integers and/or channel ids as negative integers to allow them
allowed_telegram_ids = getEnv("id_whitelist").split(',')

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
