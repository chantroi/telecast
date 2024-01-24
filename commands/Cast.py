from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from api import get_video, get_audio, ttlive
from app import join, play, leave
from util import albums, album
from custom import on_channel


@Client.on_message(filters.command("join"))
def join_chat_call(c, m):
    chat = m.chat.id
    try:
        m.reply(f"--**Chương trình đã bắt đầu**--", reply_markup=albums())
        join(chat)
    except Exception as e:
        print(e)
        m.reply("Có vấn đề xảy ra! Không thể mở trình phát")
    m.delete()
    
@Client.on_message(filters.command("end") & on_channel)
def leave_chat_call(c, m):
    leave(m.chat.id)
    m.reply("--**Chương trình đã kết thúc**--")
    
@Client.on_message(filters.command("play"))
def play_media_queue(c, m):
    chat = m.chat.id
    link = m.command[1]
    m.delete()
    try:
        user = m.from_user.first_name
    except:
        user = m.sender_chat.title
    st = m.reply(f"--**{user}**-- đã gửi yêu cầu phát __{link}__\nNội dung sẽ được phát sau 1 phút nữa.\nThêm vào bộ sưu tập sẽ có thể phát nhanh hơn")
    time.sleep(60)
    st.delete()
    play(chat, link)
    
@Client.on_message(filters.command('myalbum'))
def get_album(c, m):
    if m.sender_chat:
        m.reply("Album chỉ khả dụng cho tài khoản người dùng")
        return
    name = m.from_user.first_name
    try:
        album = album(name)
        m.reply(f"Bộ sưu tập của --**{name}**--", quote=True)
        m.delete()
    except:
        m.reply(f"--**{name}**-- không có bộ sưu tập, hãy bắt đầu bằng lệnh /addsong + tiêu đề + link đa phương tiện", quote=True)
    