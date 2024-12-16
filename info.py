import re
from os import getenv, environ
from Script import script 
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
PORT = int(environ.get('PORT', 8080))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "http://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'radhe-radhe'))
MULTI_CLIENT = False
name = str(environ.get('name', 'bisal-ki-bot'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)
REPO_OWNER = "Biisal"

# Bot information
SESSION = environ.get('SESSION', 'radhe-radhe2')
API_ID = int(environ.get('API_ID', '25467916'))
API_HASH = environ.get('API_HASH', '57c177242d037099793c265d0e6457c9')
BOT_TOKEN = environ.get('BOT_TOKEN', "7126708211:AAEn4R1ktcDeqNecaSnM-jjbQ9M8QcIgv7E") #if you are going to bot token here make sure your repo is private..
STICKERS_IDS = ('CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME').split()

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/7d585c21d1ae0ca897e25.mp4')).split() #use a gif video 🫠
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/eeb567c455fc94ec95d38.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://te.legra.ph/file/6f55d902f9bf2d0afd4bb.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://te.legra.ph/file/15c1ad448dfe472a5cbb8.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6246830040').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002075903430').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '6941610925 6246830040').split()]
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP', '-1006985314569')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1006954757017')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002075903430')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://immortal:5412ascs@immortal.jehlw9n.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "bisal-ki-bot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'ziplinker.net')
SHORTLINK_API = environ.get('SHORTLINK_API', '6a54929939ce53733fc891b96914eb017c2492a3') #use my api so i can make some money 🤣..just kidding guys..mai already aamir hoon🥱 
SECOND_SHORTLINK_URL = environ.get('SECOND_SHORTLINK_URL', 'omnifly.in.net')
SECOND_SHORTLINK_API = environ.get('SECOND_SHORTLINK_API', 'a4e51c34131981f818b74426021ab0303f7db439')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002080693695').split()] #Add a channel ID here. When you send any file to this channel, the bot will delete the file details from the MongoDB 
MAX_B_TN = environ.get("MAX_B_TN", "20")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/kungfupanda4_movies')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/hdhindibackup')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/desidude4u_open/129')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', '')

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002080693695'))
VERIFY_REQ_CHNL = int(environ.get('VERIFY_REQ_CHNL', '-1002080693695'))
NEW_USER_LOG = int(environ.get('NEW_USER_LOG', '-1002080693695'))
BIN_CHNL = int(environ.get('BIN_CHNL', '-1002080693695'))

SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'bisal_files')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
CLOSE_IMG = (environ.get('CLOSE_IMG', 'https://telegra.ph/file/d44eba716dde5861ec41c.jpg')).split()

LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan" , "bengali" , "ben"]
SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10" , "season 11" , "season 12"]
QUALITIES = ["HdRip","360p","480p","720p","1080p","1440p",'2160p', "4k"]
YEARS = ["2023","2022","2021","2020","2019","2018",'2017', "2016","2015", "2014" , "2013" , "2012" , "2011","2010","2009","2008","2007","2006","2005","2004"]

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
