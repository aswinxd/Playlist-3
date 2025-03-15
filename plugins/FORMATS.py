on_pic = "https://telegra.ph/file/5593d624d11d92bceb48e.jpg"
off_pic = "https://telegra.ph/file/0d9e590f62b63b51d4bf9.jpg"
files_cmd_pic = "https://telegra.ph/file/d44f46054250a73053614.jpg"
autodel_cmd_pic = "https://telegra.ph/file/a64533814021b40057ccd.jpg"

# Start message
START_MSG = """Hey {mention},  

This is nihariga 
ill send u files 
powered by @PlaylistUHD"""


FORCE_MSG = """Hey {mention},  
You haven't joined all required channels yet.  
Please join them and try again.  
"""

CMD_TXT = """Basic Admin Commands:  

- /batch: Create group messages  
- /genlink: Create a link for a post  
- /broadcast: Send a message to all users  
- /broadcast silent: Silent broadcast  
- /status: View bot statistics"""

BAN_TXT = "Sorry, you are banned from using this bot."

HELP_TEXT = """Hello {mention},  

I am a private file-sharing bot.  
I provide files and content through special links for specific channels.  

To access files, you must be subscribed to the required channels.  

For help, use: /help"""


ABOUT_TXT = """My name: {botname}
"""

SETTING_TXT = """Configurations
Total force sub channel: {total_fsub}
Total admins: {total_admin}
Total banned users: {total_ban}
Auto delete mode: {autodel_mode}
Protect content: {protect_content}
Hide caption: {hide_caption}
Channel button: {chnl_butn}
Request fsub mode: {reqfsub}"""

on_txt, off_txt = "Enabled", "Disabled"

FILES_CMD_TXT = """Files Related Settings
Protect content: {protect_content}
Hide caption: {hide_caption}
Channel button: {channel_button}
Button Name: {name}
Button Link: {link}

Click below buttons to change settings"""

AUTODEL_CMD_TXT = """Auto Delete Settings
Auto delete mode: {autodel_mode}
Delete timer: {timer}

Click below buttons to change settings"""

FSUB_CMD_TXT = """Force Sub Commands:
    
/fsub_chnl : Check/update current force-sub channels (admins)
/add_fsub : Add one or multiple force sub channels (owner)
/del_fsub : Delete one or multiple force sub channels (owner)"""

USER_CMD_TXT = """User Setting Commands:
    
/admin_list : View the available admin list (owner)
/add_admins : Add one or multiple user IDs as admin (owner)
/del_admins : Delete one or multiple user IDs from admin (owner)"""


RFSUB_CMD_TXT = """<b> REQUEST FSUB SETTINGS 🚦

<b> Request Fsub Mode: {req_mode}</b>

Click the buttons below to change settings.</b>"""

RFSUB_MS_TXT = """<b> REQUEST FSUB LIST 🚥

 expandable>{reqfsub_list}

Click the buttons below to change settings.</b>"""

CLEAR_USERS_TXT = """What is the use of Clear Users?

 Clear Users removes all user data for a specified Request ForceSub channel ID.  
Only user data is deleted; the channel remains unaffected.

<b><i>Select the Channel ID to delete user data:</i></b>"""

CLEAR_CHNLS_TXT = """expandable><b>What is the use of Clear Channels?</b>

➪ Clear Channels deletes all user data along with the Request ForceSub channel ID and link from the database.  
➪ This permanently removes all related data for the specified channel.  

<b> WARNING:</b> Only clear channel data if you are sure it is no longer needed.

<b><i>Select the Channel ID to delete:</i></b>"""

CLEAR_LINKS_TXT = """ expandable><b>What is the use of Clear Links?</b>

➪ Clears stored Request Links of a specified channel from the database and revokes the link.  
➪ Even if channel data is cleared, the stored request link may still exist in the database.  
➪ Deleting a request link revokes it from the channel, making it unusable.

<b><i>Select the Channel ID to delete stored links:</i></b>"""
