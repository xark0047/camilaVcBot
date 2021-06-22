from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi there, This is a music assistant service @assista_r0bot  .\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **DON'T SEND GROUP ANY LINK OR USERNAME.**\n\n ⚠️ Disclamer: If you are sending a message here it means @CAT047NOIR will see your message \n    - Don't add this user to secret groups.\n   - Don't Share private info here\n\n **FEEL FREE TO JOIN @Asiansworld**")
  return
