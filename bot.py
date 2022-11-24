import env
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Client(
    "bot",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="StringGenBot"),
)


if __name__ == "__main__":
    print("ᴍᴇᴍᴜʟᴀɪ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("API_ID/API_HASH ʟᴏ ᴋᴀɢᴀ ᴊᴇʟᴀs ᴋᴏɴᴛᴏʟ")
    except AccessTokenInvalid:
        raise Exception("BOT_TOKEN ʟᴏ ᴋᴀɢᴀ ᴊᴇʟᴀs ᴋᴏɴᴛᴏʟ")
    uname = app.get_me().username
    print(f"@{uname} sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ")
    idle() 
    app.stop()
    print("ʙᴏᴛ sᴛᴏᴘᴘᴇᴅ. ɢᴜᴇ ɴɢᴏᴘɪ ᴅᴜʟᴜ ʏᴀ ʙʏᴇ!")
