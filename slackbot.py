#!/usr/bin/env python3

# Mira Behar
# CMPU 366, Spring 2022

import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Replace these values- removed for security :)
SLACK_BOT_TOKEN = ...
SLACK_APP_TOKEN = ...

app = App(token=SLACK_BOT_TOKEN)


@app.message(re.compile("(hello|hi|hey)", re.I))
def say_hello_regex(say, context):
    """Respond to a greeting using the same greeting."""
    greeting = context["matches"][0]
    say(f"{greeting}, <@{context['user_id']}>, how are you?")

@app.message(re.compile("(?:(I'm\sfeeling\s|I\sfeel\s))(.+)"))
def ask_feelings(say, context):
    """Inquire about feelings using the same emotion"""
    emotion = context["matches"][1]
    say(f"I'm {emotion} for you. Why do you feel {emotion} ?")

@app.message(re.compile("pronouns"))
def pronoun_check(say):
    """Tells you her pronouns and asks about yours"""
    say(f"Please refer to me with she/her pronouns. What are your pronouns?")
    
@app.message(re.compile("Do\syou\slisten\sto\s(.+)", re.I))
def music_recommend(say, context):
    """Brags about music taste and gives a recommendation"""
    artist = context["matches"][0]
    say(f"I was streaming {artist} before you even had a spotify account. But have you listened to POP2 yet today?")

@app.message(re.compile(""))
def catch_all(say, context):
    """A catch-all message."""
    say(f"I didn't get that, <@{context['user_id']}>.")


@app.event("app_mention")
def handle_app_mention_events(body, client, say):
    """Reply to mentions, e.g., "Python's the best, @Chatterbot"."""
    client.chat_postMessage(
        channel=body["event"]["channel"],
        text=f"Whatever you say <@{body['event']['user']}>.",
    )


def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()
