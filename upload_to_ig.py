from instagrapi import Client
import os
from generate_caption import get_caption
from dotenv import load_dotenv

load_dotenv()
username = os.getenv("IG_USERNAME")
password = os.getenv("IG_PASSWORD")

def post_reel(video_path):
    cl = Client()
    cl.login(username, password)
    caption = get_caption()
    cl.clip_upload(video_path, caption=caption)