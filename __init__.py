from Corona_Music.core.bot import Spotify
from Corona_Music.core.dir import dirr
from Corona_Music.core.git import git
from Corona_Music.core.userbot import Userbot
from Corona_Music.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Spotify()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "Gaana_MusicBot"  # connect music api key "Dont change it"