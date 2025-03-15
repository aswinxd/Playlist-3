import asyncio
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from datetime import datetime, timedelta

def convert_time(duration_seconds: int) -> str:
    periods = [
        ('Year', 60 * 60 * 24 * 365),
        ('Month', 60 * 60 * 24 * 30),
        ('Day', 60 * 60 * 24),
        ('Hour', 60 * 60),
        ('Minute', 60),
        ('Secound', 1)
    ]

    parts = []
    for period_name, period_seconds in periods:
        if duration_seconds >= period_seconds:
            num_periods = duration_seconds // period_seconds
            duration_seconds %= period_seconds
            parts.append(f"{num_periods} {period_name}{'s' if num_periods > 1 else ''}")

    if len(parts) == 0:
        return "0 Sᴇᴄᴏɴᴅ"
    elif len(parts) == 1:
        return parts[0]
    else:
        return ', '.join(parts[:-1]) +' ᴀɴᴅ '+ parts[-1]



DEL_MSG = """⚠️ Due to ban some issues
Files will be deleted within <a href="https://t.me/{username}">{time}</a>. So forward this to another group"""

async def auto_del_notification(bot_username, msg, delay_time, transfer): 
    temp = await msg.reply_text(DEL_MSG.format(username=bot_username, time=convert_time(delay_time)), disable_web_page_preview = True) 

    await asyncio.sleep(delay_time)
    try:
        if transfer:
            try:
                name = "Get Again"
                link = f"https://t.me/{bot_username}?start={transfer}"
                button = [[InlineKeyboardButton(text=name, url=link), InlineKeyboardButton(text="Close ", callback_data = "close")]]

                await temp.edit_text(text=f"Files was deleted \n If you want files again click here [<a href={link}>{name}</a>] Click below message or close with message", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)

            except Exception as e:
                await temp.edit_text(f"Previous message was deleted")
                print(f"Error occured while editing the Delete message: {e}")
        else:
            await temp.edit_text(f"Previous message was deleted")

    except Exception as e:
        print(f"Error occured while editing the Delete message: {e}")
        await temp.edit_text(f"Previous message was deleted")

    try: await msg.delete()
    except Exception as e: print(f"Error occurred on auto_del_notification() : {e}")


async def delete_message(msg, delay_time): 
    await asyncio.sleep(delay_time)
    
    try: await msg.delete()
    except Exception as e: print(f"Error occurred on delete_message() : {e}")