"""
    instabot example

    Workflow:
        Follow user's following by username.
"""

import sys
import os
import time
import random
from tqdm import tqdm

sys.path.append(os.path.join(sys.path[0],'../'))
from instabot import Bot

if len(sys.argv) != 2:
    print ("USAGE: Pass username")
    print ("Example: python %s ohld" % sys.argv[0])
    exit()

bot = Bot()
bot.login()
bot.follow_following(sys.argv[1])
