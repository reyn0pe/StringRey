from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo="https://telegra.ph/file/f833324f49aefc26b0431.jpg", caption=f"➤ Lo Belum Join [Grup/Channel]({link}), Jika Lo Mau Pake Gue, Join lah ke [Grup/Channel]({link}) Kalo Udah Join Coba Mulai lagi",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ʀᴇʏ", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promosikan saya sebagai admin di obrolan MUST_JOIN : {MUST_JOIN} !")
