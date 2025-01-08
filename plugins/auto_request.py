import asyncio
from pyrogram import Client, filters, enums
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

@Client.on_chat_join_request()
async def autoapprove(client, message: ChatJoinRequest):
  try:
    chat=message.chat
    user=message.from_user
    print(f"{user.first_name} Joined 🤝")
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    print(user.id)
    photo_path = "https://envs.sh/l8h.jpg"
    caption = f"Hello {user.mention} ✨\n\nYour Request to Join {chat.title} has been Approved.\n\nSend /start to know more.\nJoin US 👇👇"
    buttons = [
        [InlineKeyboardButton("𝙅𝙊𝙄𝙉 𝘾𝙃𝘼𝙉𝙉𝙀𝙇", url="https://t.me/CinemaKalavaraTG")]
    ]
    user_m = user.id
    x=await client.send_photo(
        chat_id=user_m,
        photo=photo_path,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    await asyncio.sleep(300)
    await x.delete()
  except PeerIdInvalid:
      pass
