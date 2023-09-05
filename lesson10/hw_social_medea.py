from time import time
from typing import Union


class SocialChannel:
    def __init__(self, channel_type: str, followers: int):
        self.channel_type = channel_type
        self.followers = followers


class Post:
    def __init__(self, message: str, timestamp: int):
        self.message = message
        self.timestamp = timestamp


class YouTube(SocialChannel):
    def post_message(self, message: str):
        print(f"Posting on YouTube: {message}")


class Telegram(SocialChannel):
    def post_message(self, message: str):
        print(f"Posting on Telegram: {message}")


class Twitter(SocialChannel):
    def post_message(self, message: str):
        print(f"Posting on Twitter: {message}")


def post_a_message(channel: SocialChannel, message: str):
    channel.post_message(message)


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    current_time = time()
    for post in posts:
        if post.timestamp <= current_time:
            message = post.message
            for channel in channels:
                post_a_message(channel, message)


# Само использованик:

youtube = YouTube("youtube", 1000000)
telegram = Telegram("facebook", 500000)
twitter = Twitter("twitter", 200000)

channels = [youtube, telegram, twitter]

posts = [
    Post("Hello, youTube!", 1679817600),
    Post("Yo, Telegram!", 1679817600),
    Post("Hello, twitter!", 1679817600),
]

process_schedule(posts, channels)
