#!/usr/bin/env python3

import json
import os

from linkedin_api import Linkedin


api = Linkedin(
    os.environ["LINKEDIN_USERNAME"],
    os.environ["LINKEDIN_PASSWORD"],
)

posts = api.get_profile_posts(
    "edthewlis",
    post_count=10_000,
)

with open("eds-posts-raw.json", "w") as o:
    json.dump(posts, o, indent=2)


output = [
    {"text": post["commentary"]["text"]["text"]}
    for post in posts
    if "commentary" in post
]

with open("eds-posts-text.json", "w") as o:
    json.dump(output, o, indent=2)

# TODO: api.get_post_comments?
