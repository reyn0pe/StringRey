from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ️", url="https://t.me/reyn0pe"),
         InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/reyn0pe/46"),
        ],
    ]

    START = """
Hey Bro {}
Welcome To  {} 

Kalo Lo Ga Percaya Sama Gue,
❶ Berhenti Membaca Pesan Ini
❷ Hapus Chat Ini

🫵 Masih Lo Baca!? 
Lo Bisa Pake Gue Buat Dapetin Pyrogram V2 Baru Dan Sesi String Telethon. Pake Tombol Di Bawah Ini Buat Mempelajari Lebih Lanjut!

❏ ʀᴇʏ ᴘʀᴏᴊᴇᴄᴛ
┣ ᴄʜᴀɴɴᴇʟ : [Rey](https://t.me/reyn0pe)
┣ ғʀᴀᴍᴇᴡᴏʀᴋ : [Pyrogram](https://docs.pyrogram.org)
┗ ʟᴀɴɢᴜᴀɢᴇ : [Python](https://www.python.org)

❏ ᴅᴇᴠᴇʟᴏᴘᴇʀ ɢᴀɴᴛᴇɴɢ ━┓
┗ @xyreynld
    """
