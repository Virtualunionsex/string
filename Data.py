from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}

Selamat datang di {}

Jika kamu tidak percaya bot ini, 
1) Mati aja lo ngentod!!!
2) blokir bot atau delete chat

Bot ini Bekerja Untuk Membantu Kamu Mendapatkan String Session Via Bot. Rekomendasi Jika Ingin Mengambil String Gunakan Akun Lain, Agar Tidak Delay. Terimakasih
By @RAM_UBOT
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ​", callback_data="generate")],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ​", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton("ᴍᴀɪɴᴛᴀɴᴇᴅ ʙʏ​", url="https://t.me/userbotch")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ​​", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ​", callback_data="about")
        ],
        [InlineKeyboardButton("ɪɴꜰᴏ ʙᴏᴛ ʟᴀɪɴɴʏᴀ​", url="https://t.me/Ramsupportt")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - Tentang Bot ini
/help - This Message
/start - Mulai Bot
/generate - Mulai Generating Session
/cancel - Membatalkan process
/restart - Membatalkan process
"""

    # About Message
    ABOUT = """
**About This Bot** 

Sebuah telegram bot untuk mengambil pyrogram dan telethon string session by @SkyStringBot

DONASI : [Traktir Kopi Tipis²](https://t.me/userbotch/9)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @RAM_UBOT
    """
