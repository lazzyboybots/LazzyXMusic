from LazzyXMusic import Lazzy
from LazzyXMusic.core.dir import dirr
from LazzyXMusic.core.git import git
from LazzyXMusic.core.userbot import Userbot
from LazzyXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
