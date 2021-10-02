# © @AvishkarPatil [ Telegram ]

from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)

START_TEXT = """
<i>👋 Oye,</i>{}\n
<i>Soy un Bot de la aplicación DH-HD COMPLETOS y mi trabajo es generar enlaces directos 😁</i>\n
<i>Haga clic en Ayuda para obtener más información</i>\n
<i><u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u></i>
<b>🔞 Subir contenidos nopor conduce a una delicioso BAN permanente.</b>\n\n
<i><b>🍃Bot Mantenido Por :</b>@CLAY_MODS</i>"""

HELP_TEXT = """
<i>- Envíame cualquier archivo (o) reenvialo desde telegram.</i>
<i>- ¡Proporcionaré un enlace de descarga directa externo!.</i>
<i>- Los Links generados serán reenviado al grupo para ser controlado por los administradores y para marcar tus aportes 😁</i>
<i>- Los Links generados son permanente con la velocidad más rápida</i>\n
<u>🔸 𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸</u>\n
<b>🔞 Subir contenidos nopor conduce a una delicioso BAN permanente.</b>\n
<i>Póngase en contacto con el desarrollador (o) informe de errores</i> <b>: <a href='https://t.me/CLAY_MODS'>[ Haga clic aquí ]</a></b>"""

ABOUT_TEXT = """
<b>⚜ Mi Nombre : DH-HD STREAM 👻</b>\n
<b>🔸Vᴇʀꜱɪᴏɴ : <a href='https://t.me/CLAY_MODS'>2.0.7</a></b>\n
<b>🔹Desarrollador : <a href='https://t.me/CLAY_MODS'>GuChiDevStudio.Ltda</a></b>\n
<b>🔸Última actualización : <a href='https://t.me/CLAY_MODS'>[ 11-septiembre-21 ] 04:35 PM</a></b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Ayuda', callback_data='help'),
        InlineKeyboardButton('Acerca de', callback_data='about'),
        InlineKeyboardButton('Cerrar', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Inicio', callback_data='home'),
        InlineKeyboardButton('Acerca de', callback_data='about'),
        InlineKeyboardButton('Cerrar', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Inicio', callback_data='home'),
        InlineKeyboardButton('Ayuda', callback_data='help'),
        InlineKeyboardButton('Cerrar', callback_data='close')
        ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nuevo usuario unido:** \n\n__Mi nuevo amigo__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Comenzó usted Bᴏᴛ !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__Lo siento, señor Estás Suspendido para Usarme.__\n\n  **Contactar con el desarrollador @CLAY_MODS Te ayudará**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Únete a mi grupo de DH-HD COMPLETOS para usarme 🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Únete ahora 🔓", url=f"https://t.me/joinchat/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Algo anda mal, contacta con el desarrollador</i> <b><a href='https://t.me/CLAY_MODS'>[ Haga clic aquí  ]</a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text=START_TEXT.format(m.from_user.mention),
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
              )                                                                         
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**Lo siento, señor Estás Suspendido para Usarme.Contactar con el desarrollador** @CLAY_MODS",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Únase a mi grupo de DH-HD COMPLETOS para usar el Bᴏᴛ**!\n\n**Debido a la sobrecarga, solo los miembros del grupo pueden usar el Bᴏᴛ**!",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("🤖 Únete al grupo", url=f"https://t.me/joinchat/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Algo salió mal. Contáctame** [GuChiDevStudio.Ltda](https://t.me/CLAY_MODS).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text ="""
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Nombre del archivo :</b> <i>{}</i>\n
<b>📦 Tamaño del archivo  :</b> <i>{}</i>\n
<b>🔗 Link del archivo :</b> <i>{}</i>\n
<b>🚸 Nota : El Link caduca en 24 hora</b>\n
<i>🍃 Bᴏᴛ Mantenido por:</i> <b>@CLAY_MODS</b>
"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Descarga ahora 📥", url=stream_link)]])
        )


@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nuevo usuario unido:** \n\n__Mi nuevo amigo__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Comenzó usted Bᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. Cᴏɴᴛᴀᴄᴛ ᴛʜᴇ Dᴇᴠᴇʟᴏᴘᴇʀ</i>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Únase a mi grupo de DH-HD COMPLETOS para usar el Bᴏᴛ**!\n\n**Debido a la sobrecarga, solo los miembros del grupo pueden usar el Bᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("🤖 Unete ahora", url=f"https://t.me/joinchat/{Var.UPDATES_CHANNEL}")
                        ]]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Algo salió mal. Contáctame** [GuChiDevStudio.Ltda](https://t.me/CLAY_MODS).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text=HELP_TEXT,
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
        )
