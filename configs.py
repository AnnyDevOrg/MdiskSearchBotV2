import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", ""))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "mdiskcynitebot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "")) 
    BOT_USERNAME = os.getenv("BOT_USERNAME", "")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "0"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "cyniteSupport")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", """**Hᴇʏ {}, 

I ᴀᴍ Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Rᴏʙᴏᴛ 🔍.

I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Eᴠᴇʀʏ Mᴏᴠɪᴇ Iɴ Mᴅɪsᴋ Lɪɴᴋ 🔗

Jᴜsᴛ Tʏᴘᴇ ᴀ Mᴏᴠɪᴇ Nᴀᴍᴇ 🎬**""" ) 
    START_PHOTO = os.getenv("START_PHOTO", "https://te.legra.ph/file/b7eb637edf4b2f18e92c1.png")
    HOME_TEXT = os.getenv("HOME_TEXT", """ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕

ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ.

ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ✅""" )
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-10012")
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-100182090"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 20))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 180))
    MDISK_API = os.getenv("MDISK_API", "")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", """I ᴏɴʟʏ ꜱʜᴀʀᴇ ᴛʜᴇ ᴘᴏꜱᴛ ꜰʀᴏᴍ ᴘᴇᴏᴘʟᴇ'ꜱ ᴄʜᴀɴɴᴇʟ! 

ᴡʜᴏ ᴍᴀᴅᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ, 

i ɴᴏᴛ ꜱᴛᴏʀᴇ ᴀɴʏ ꜰɪʟᴇꜱ ᴏʀ ᴛᴇxᴛ ɪɴ  ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ.

ᴅᴍ ꜰᴏʀ ᴀɴʏ Qᴜᴇʀʏ @HindFlix_Feedback_Bot 🤖""" )
    ABOUT_WATCH_TEXT = """
ʜᴇʏ ʙᴜᴅᴅʏ, 

ᴍᴅɪsᴋ - ᴀɢᴀʀ ᴀᴘᴋᴏ ɴᴀʜɪ ᴘᴀᴛᴀ ᴋɪ ᴍᴅɪsᴋ ʟɪɴᴋ sᴇ ᴍᴏᴠɪᴇ ᴋᴀɪsᴇ ᴅᴇᴋʜᴇ ᴛᴏ ɴɪᴄᴇ ᴅɪʏᴇ ɢᴀʏᴇ ᴍᴅɪsᴋ ᴡᴀʟᴇ ʙᴜᴛᴛᴏɴ ᴘᴀʀ ᴄʟɪᴄᴋ ᴋᴀʀᴇ 

ᴛᴇʀᴀ ʙᴏx - ᴀɢᴀʀ ᴀᴘᴘᴋᴏ ɴᴀʜɪ ᴘᴀᴛᴀ ᴋɪ ᴛᴇʀᴀʙᴏx sᴇ ᴍᴏᴠɪᴇs ᴋᴀɪsᴇ ᴅᴇᴋʜᴇ ᴛᴏ ɴɪᴄʜᴇ ᴅɪʏᴇ ɢᴀʏᴇ ᴛᴇʀᴀ ʙᴏx ʙᴜᴛᴛᴏɴ ᴘᴀʀ ᴄʟɪᴄᴋ ᴋᴀʀᴇ

ʀᴇɢᴀʀᴅs - @HindFlix"""
    ABOUT_MDISK_TEXT = """
How To Open MDisk Links, Watch This Video👇🔥
MX Player में देखो और मजे करो 😊👍

1) 𝘔𝘥𝘪𝘴𝘬 𝘬𝘪 𝘭𝘪𝘯𝘬 𝘱𝘦𝘳 𝘤𝘭𝘪𝘤𝘬 𝘬𝘢𝘳𝘦 𝘶𝘴𝘬𝘦 𝘣𝘢𝘢𝘥 1 𝘱𝘢𝘨𝘦 𝘬𝘩𝘶𝘭𝘦𝘨𝘢. 💜

2) 𝘞𝘢𝘩𝘢 𝘱𝘢𝘳 4 𝘉𝘶𝘵𝘵𝘰𝘯 𝘏𝘰𝘨𝘢 𝘴𝘗𝘭𝘢𝘺 𝘞𝘪𝘵 𝘔𝘹 𝘗𝘭𝘢𝘺𝘦𝘳 𝘈𝘯𝘥 𝘚𝘱 𝘗𝘭𝘢𝘺𝘦𝘳.😉

3) 𝘈a𝘱𝘬𝘰 𝘔𝘹 𝘗𝘭𝘢𝘺𝘦𝘳 𝘗𝘢𝘳 Likhe 𝘏𝘶𝘦 𝘒𝘰 𝘊𝘩𝘰𝘰𝘴𝘦 𝘒𝘢𝘳𝘯𝘢 𝘏𝘢𝘪😍

4) 𝘐𝘴𝘬𝘦 𝘉𝘢𝘢𝘥 𝘈𝘨𝘢𝘳 𝘈𝘱𝘬𝘰 𝘖𝘯𝘭𝘪𝘯𝘦 𝘋𝘦𝘬𝘩𝘯𝘢 𝘏𝘢𝘪 𝘛𝘰 𝘞𝘢𝘵𝘤𝘩 𝘖𝘯𝘭𝘪𝘯𝘦 𝘗𝘳 𝘊𝘭𝘪𝘤𝘬 𝘒𝘢𝘳𝘦 💻

5) 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘒𝘢𝘳𝘯𝘦 𝘒𝘦 𝘓𝘪𝘺𝘦 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘉𝘶𝘵𝘵𝘰𝘯 𝘗𝘢𝘳 𝘊𝘭𝘪𝘤𝘬 𝘒𝘢r Sakte Hai"""

    ABOUT_DIRECT_DOWNLOAD_TEXT = """
How To Open Our Direct Downloading Links, Watch This Video 👇🔥
(डायरेक्ट डोनलोडिंग कैसे करते है, इसका विडिओ देखने के लिए इस लिंक पर क्लिक करे)

https://t.me/hindflix_help/2

Contact Us On @HindFlix_Feedback_Bot"""

    ABOUT_HELP_TEXT = """

🍓 RᴇQᴜɪʀᴇᴍᴇɴᴛ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ!

🍓 Sᴛᴇᴘ 1 - Aᴘᴋᴏ ᴇᴋ ɢʀᴏᴜᴘ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴍᴇᴍʙᴇʀꜱ ʙʜɪ ʜᴏ, ᴀᴜʀ ᴇᴋ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴀᴘᴋᴇ ꜱᴀʀᴇ ᴘᴏꜱᴛ ʜᴏɴɢᴇ!

🍓 Sᴛᴇᴘ 2 - ʙᴏᴛ ᴋᴏ ᴀᴘɴᴇ ɢʀᴏᴜᴘ ᴀᴜʀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋᴀ ᴀᴅᴍɪɴ ʙᴀɴᴀɴᴀ ʜᴏɢᴀ.

🍓 Sᴛᴇᴘ 3 - ɢʀᴏᴜᴘ ᴍᴇ "/License" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ!

ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ. 

🍓 Sᴛᴇᴘ 4 - ɢʀᴏᴜᴘ ᴍᴇ "/database - ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ɪᴅ" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ.

ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ʙʜɪ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ 

🍓 Sᴛᴇᴘ 5 - ᴀʙ ᴀᴘᴋᴏ ᴀᴘɴᴇ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴘᴏꜱᴛ ᴅᴀʟɴɪ ʜᴏɢɪ,

ᴊɪꜱꜱᴇ ᴋɪ ᴀɢᴀʀ ɢʀᴏᴜᴘ ᴍᴇ ᴋᴏɪ ᴜꜱᴇʀ ꜱᴇᴀʀᴄʜ ᴋᴀʀᴇ ᴛᴏ ʏᴇ ʙᴏᴛ ᴜɴ ᴜꜱᴇʀ ᴋᴇ Qᴜᴀʀʏ ᴋᴏ ꜱᴀᴍᴀᴊʜ ᴋᴇ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ꜱᴇ ᴘᴏꜱᴛ ᴜᴛʜᴀ ᴋᴇ ᴜɴʜᴇ ᴅᴇ ᴘᴀʏᴇ.

🍓 Nᴏᴛᴇ : Bᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴊᴏɪɴ ʜᴏɴᴇ ᴄʜᴀʜɪʏᴇ,

ᴀɢᴀʀ ʙᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴀ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ɴʜɪ ᴋᴀʀ ʀᴀʜᴇ ʜᴀɪɴ ᴛᴏ ᴜɴʜᴇ ᴘᴇʀꜱᴏɴᴀʟ ᴍꜱɢ ᴋᴀʀᴇɴ.

👉 Powered By - @HindFlix

"""
