from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from more_itertools import chunked
import os, shelve

db = shelve.open("channels.db")
def playlist():
    allkeys = list(db.keys())
    chunked_keys = list(chunked(allkeys, 6))
    playlist = []
    for chunk in chunked_keys:
        row_buttons = [InlineKeyboardButton(pre, callback_data=pre) for pre in chunk]
        playlist.append(row_buttons)
    return InlineKeyboardMarkup(playlist)