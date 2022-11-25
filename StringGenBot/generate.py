from data import Data
from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)


ask_ques = "**➤ Silakan Pilih Pustaka Python Yang Ingin Anda Hasilkan String. **"
buttons_ques = [
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ", callback_data="pyrogram1"),
        InlineKeyboardButton("ᴘʏʀɢᴏʀᴀᴍ ᴠ2", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ ʙᴏᴛ", callback_data="pyrogram_bot"),
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ ʙᴏᴛ", callback_data="telethon_bot"),
    ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "Telethon"
    else:
        ty = "Pyrogram"
        if not old_pyro:
            ty += "V2"
    if is_bot:
        ty += "Bot"
    await msg.reply(f"➤ Mencoba Memulai **{ty}** Session Generator...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "➤ Memulai Proses Pembuatan Sesi ⏳\n\nSilakan Kirim **API_ID** Anda Untuk Melanjutkan.", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply("**API_ID** Harus Menjadi Integer Mulai Membuat Sesi String Anda Lagi.", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, "➤ Sekarang Silakan Kirim **API_HASH** Anda Untuk Melanjutkan Proses.", filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "➤ Silakan Kirimkan **PHONE_NUMBER** Anda Dengan Kode Negara Tempat Anda Ingin Menghasilkan Sesi \nUntuk Example : `+628512345678`'"
    else:
        t = "Silakan Kirim **BOT_TOKEN** Anda Untuk Melanjutkan. \nMisalnya : `5621912727:AAFGmCfAgoODHkMWWkzew0z05svqa23l3FY`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("➤ Mencoba... Mengirim OTP ke Nomor yang Diberikan.")
    else:
        await msg.reply("➤ Mencoba... Untuk Masuk Melalui Bot Token.")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("➤ **API_ID** dan **API_HASH** Anda Tidak Cocok Dengan Server Telegram. \n\nSilakan Mulai Membuat Sesi String Anda Lagi.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("➤ **PHONE_NUMBER** yang Anda Kirim Bukan Milik Akun Telegram Saya.\n\nSilakan Mulai Membuat Sesi String Anda Lagi.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "➤ Silakan Kirimkan **OTP** Yang Telah Anda Terima Dari Telegram Di Akun Anda.\nJika OTP Adalah `'09876` Silakan Kirimkan Sebagai `0 9 8 7 6`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("➤ Batas Waktu Mencapai 10 Menit.\n\n Silakan Mulai Membuat Sesi String Anda Lagi.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("➤Error404 OTP Tidak Valid yang Anda Kirim **Salah.**\n\nSilakan Mulai Lagi.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("➤ Error404 OTP yang Anda Kirim **Sudah Kedaluwarsa.**\n\nSilakan Mulai Lagi.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "➤ Silakan Masukkan **Kata Sandi Dua Langkah** Anda Untuk Melanjutkan.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("➤ Batas Waktu Mencapai 5 Menit.\n\nSilakan Mulai Membuat Sesi String Anda Lagi.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("➤ Kata Sandi yang Anda Kirim Salah.\n\nSilakan Mulai Membuat Sesi String Anda Lagi.", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**Ini Adalah Sesi String {ty} Anda**\n\n`{string_session}` \n\n**Powered By :** @StringRey_Bot\n🚨 **Note :** Jangan Share 😒 Dan Jangan Lupa Join @reyn0pe"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "➤ Berhasil Menghasilkan Sesi String {} Anda. \n\n Harap Periksa Pesan Tersimpan Untuk Mendapatkannya.\n\n**Bot Sesi String Oleh** @StringRey_Bot".format("Telethon" if telethon else "Pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**➤ Dibatalkan Sampai jumpa! Jaga dirimu.**", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**➤ Berhasil Memulai Ulang Bot Ini Untuk Anda Temanku**", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**➤ Dibatalkan Sampai jumpa! Jaga dirimu.**", quote=True)
        return True
    else:
        return False
