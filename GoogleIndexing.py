from google.oauth2.service_account import Credentials
from google.auth.transport.requests import AuthorizedSession
import time

# Replace the JSON content with your actual JSON key
json_key = {
    "type": "service_account",
    "project_id": "code-gamer",
    "private_key_id": "1bbee77c07dfb6c9dfd032f1599c5599cd135aa7",
    "private_key": """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC3c6GJCc8ySYS7
kTbTsgM4zViMW7n1vGxEFmtNKfCVor1fkGphz4mex7mfd4cDY1zWlslNKnnKPXxL
oZnJIjgNOQdMDdPP98xzc+vmyyjQBdQCxDNWtv+LwqbADasamPtK430o2GdmMuLN
5W7jOrepVDDcNF7XORk+YDtT3GbYmvtG5JD35e8g3LEfIeCD1V3B89+GXEJl24P0
1cVlL4E+ysMzihE+izfCLkb+4uS6iCX/Fp0lzsu+MxBFDhonJbZ1roacJUzE5tu4
waoRz6CUaJEVNjREERNuQBDybUiJ4Gmvx7i7tAuJE+O5TlatcrRacWJEuUbtindM
oQXCrDwdAgMBAAECggEAOohn5ZAeLobblXc3XaNCOOj4FEyeEGSOzMi0ctnrW+sh
bjDnaI7t8535QYLDLtcQw5033Gmtk1Q76OvGZDEJXlqwU9ljmEsRzlKR1cFDo+AA
LePJF6Vq8v5n8wZJbkKah2H/SL2HfEnHKPfIAjN1b08gCdqh2hzrS4Yr182OeRSr
pUvMIVD3baWmMhw5xWpImZCEAFRPmEqnie/kF0kaZHA1SKlQx1XFzb1s/eLHj0bu
Lj1SW8dkGct297MwZd0gefXU8GSog3CxT2Jj2tlCkF13BUKWoEpjG1SJBFdaMkiN
cpof8E3L5F1VyGXQvBiVio00JYhWXk3/klfpfONL1wKBgQDiSsKjjPANcN42gUjO
6TD55z1wpK92uqsPseBg5JBBufLvd69qrfk+A/O9++zWcw82i0WaniD4qq7Z99Gp
ERZGllmXuaFaUYRzbx5pEpc3LYSUQ5KAXCTIk6BTNf0/YAXx1kA1OOTbVMapvKrb
QGGyryxRNvB7xlrvR+5X637gNwKBgQDPiRbJmb0MVujRSQgjGNtrrFLkuA7yI9Zq
6cWN1/1IIZDwfL30YI9dvazH4tIkgtsDA5s7mqCotVCGy43LAG7wEfzz2kM+7Fn+
XP88c7bDWnB/dq/9WeIzGC829U5t42TU8OMvqwR3Ru0TuDgmMAn9Y3hBwJH0LSyI
i/YL3EXUSwKBgD/n9QfTKYfiNB8Ya8NjP52TnFpPZ+4T0XNhPIigg8zMArt2BWgP
MbA91Xv1xXDalZVFx6Zeudj/+tk7j047sRrGIw8iMVscYldnLiNmSKYgiKyGWL0/
SHQMnN5jBN389DDT3NYq9xap3mDZEzdP+0dHCTD2XvvVjKC+o6TYsMAJAoGAFOGU
O2COluk/r58LhIyBt0m1ZXHnfxGAB23SBL2QrGtELA5BBo+YnTPyaII35piL9Leu
LMcYFyF3IrjkYWJ/xwPoUZjKX1BklaVBwRFbeDhnTUvh1Tnv+ngaeAsigwf4IzzB
fxBT+LRYMj282IrI1ofll6gKh2jsLCj47qSRGhUCgYEAjyT27nVPH1kkAt80oE76
OdGtdQfOuze2XqaFZ+rS0JCq4zw7zhuXasXtOauJOQeVhZHOFfkEAeudJLZ0rRkJ
kHi/izvjcdCvAIdaWiQe95AFoVun7nW+O/KUU2VlxFY4YayoqEfztYYfUBwAdojx
VhzpFS/rOxR1kfISiDiHYoM=
-----END PRIVATE KEY-----""",
    "client_email": "code-gamer@code-gamer.iam.gserviceaccount.com",
    "client_id": "100674627607929197470",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/code-gamer%40code-gamer.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# Authenticate using the JSON key
credentials = Credentials.from_service_account_info(json_key, scopes=["https://www.googleapis.com/auth/indexing"])
authed_session = AuthorizedSession(credentials)

def indexURL(url):
    ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    content = {'url': url.strip(), 'type': "URL_UPDATED"}
    response = authed_session.post(ENDPOINT, json=content)

    if response.status_code == 200:
        result = response.json()
        print(f"Indexed URL: {result['urlNotificationMetadata']['url']}")
        print(f"Notification Type: {result['urlNotificationMetadata']['latestUpdate']['type']}")
        print(f"Notify Time: {result['urlNotificationMetadata']['latestUpdate']['notifyTime']}")
    else:
        print(f"Error {response.status_code}: {response.json()}")

# List of URLs to index
urls = [
   "https://codegamer.online/g/imposter-battle-z-dragon-warriors",
"https://codegamer.online/g/color-ball-smack",
"https://codegamer.online/g/crowd-city-3d",
"https://codegamer.online/g/wacky-run-3d",
"https://codegamer.online/g/high-heels-2-",
"https://codegamer.online/g/mega-ramp-car-stunt-race",
"https://codegamer.online/g/drawing-christmas-for-kids",
"https://codegamer.online/g/fish-jumping",
"https://codegamer.online/g/tic-tac-toe-14-player",
"https://codegamer.online/g/water-sort-online",
"https://codegamer.online/g/singer-escape",
"https://codegamer.online/g/guess-the-song--music-quiz",
"https://codegamer.online/g/princess-coloring-game-for-girls--paint-color-boo",
"https://codegamer.online/g/princess-cool--coloring-street-book-paint-game",
"https://codegamer.online/g/among-us-car-race",
"https://codegamer.online/g/baby-granny-2021",
"https://codegamer.online/g/jungle-dash-run-3d--game-online-",
"https://codegamer.online/g/retro-racing-3d--free-mobile-game-online-",
"https://codegamer.online/g/ninja-jump-force--game-online-",
"https://codegamer.online/g/snake-vs-balls",
"https://codegamer.online/g/pull-the-pin-2021",
"https://codegamer.online/g/light-it-up--glow",
"https://codegamer.online/g/mazy-maze-%C3%A2%C2%AD%C2%90-labyrinth-puzzle-%28rotate-the-maze%21%29",
"https://codegamer.online/g/city-hero-vs-street-love",
"https://codegamer.online/g/flowers-blocks-collapse",
"https://codegamer.online/g/mario-jigsaw-puzzle-collection",
"https://codegamer.online/g/math-pipes",
"https://codegamer.online/g/mr-block",
"https://codegamer.online/g/helix-rotate",
"https://codegamer.online/g/cars-paint-3d-2021",
"https://codegamer.online/g/connect-the-light",
"https://codegamer.online/g/circle-collector",
"https://codegamer.online/g/unicorn-runner-3d",
"https://codegamer.online/g/poke-among-us",
"https://codegamer.online/g/ladder-run",
"https://codegamer.online/g/rolling-balls",
"https://codegamer.online/g/knockout-fall-guys-3d-run--royale-race",
"https://codegamer.online/g/among-us-night-race",
"https://codegamer.online/g/among-us-online-player",
"https://codegamer.online/g/mx-offroad-mountain-bike",
"https://codegamer.online/g/old-car-stunt",
"https://codegamer.online/g/perfect-sniper-3d-2",
"https://codegamer.online/g/spot-the-differences",
"https://codegamer.online/g/army-sniper",
"https://codegamer.online/g/diamond-painting-asmr-coloring",
"https://codegamer.online/g/ferrari-car-jigsaw",
"https://codegamer.online/g/pin-the-needle",
"https://codegamer.online/g/muscle-cars-coloring",
"https://codegamer.online/g/rescue-helicopter",
"https://codegamer.online/g/farm-merge-pop",
"https://codegamer.online/g/extreme-car-paint-",
"https://codegamer.online/g/find-fruits-names",
"https://codegamer.online/g/twisty-hit",
"https://codegamer.online/g/tank-war-",
"https://codegamer.online/g/perfect-slices",
"https://codegamer.online/g/head-ball-2",
"https://codegamer.online/g/slice-peeler-corn",
"https://codegamer.online/g/block-puzzle-lego-pro",
"https://codegamer.online/g/shortcut-run-2021",
"https://codegamer.online/g/foxob--run-run%21",
"https://codegamer.online/g/animal-coloring-book-gamesfree-online",
"https://codegamer.online/g/dora-the-explorer-coloring",
"https://codegamer.online/g/shooter-bubble-",
"https://codegamer.online/g/paint-my-car",
"https://codegamer.online/g/candy-filler-2",
"https://codegamer.online/g/guitarist-hero-free-guitar-hero-battle-music-gam",
"https://codegamer.online/g/gumball-soccer-game",
"https://codegamer.online/g/spongebob--bikini-bottom-bungle",
"https://codegamer.online/g/light-bulb-puzzle-game",
"https://codegamer.online/g/horror-baby-in-yellow-vs-granny-scary-simulator",
"https://codegamer.online/g/princess-coloring-book-glitter",
"https://codegamer.online/g/educational-games-for-kids",
"https://codegamer.online/g/red-hero-ball-4",
"https://codegamer.online/g/samurai-king",
"https://codegamer.online/g/dragon-ball-z-kakarot-fight",
"https://codegamer.online/g/galactic-traffic",
"https://codegamer.online/g/do-not-fall-online",
"https://codegamer.online/g/blue-and-red-%C3%84%C2%B0mpostor",
"https://codegamer.online/g/blue-morpho-butterfly-jigsaw",
"https://codegamer.online/g/paper-animals-pair",
"https://codegamer.online/g/hidden-wrench-in-trucks",
"https://codegamer.online/g/room-escape",
"https://codegamer.online/g/perfect-fruit-slicer-",
"https://codegamer.online/g/super-race-3d-running-game",
"https://codegamer.online/g/smiley-face-emoji-jigsaw",
"https://codegamer.online/g/mr-noob-vs-1000-zombies--lucky-block-story",
"https://codegamer.online/g/super-ryan-toys",
"https://codegamer.online/g/tattoo-drawing--online-game",
"https://codegamer.online/g/stick-killer-online",
"https://codegamer.online/g/hockey-goal-legends",
"https://codegamer.online/g/penguin-battle-royale",
"https://codegamer.online/g/cowboy-jungle-adventures",
"https://codegamer.online/g/sudoku-pro",
"https://codegamer.online/g/egirls-hairstyle-makeover",
"https://codegamer.online/g/masha-happy-dentist-2",
"https://codegamer.online/g/bunny-angel",
"https://codegamer.online/g/shortcut-race3dnew",
"https://codegamer.online/g/match-object-3d",
"https://codegamer.online/g/climber-draw-2021",
"https://codegamer.online/g/muaythai-fighters-jigsaw",
"https://codegamer.online/g/basket-king-pro",
"https://codegamer.online/g/bottle-stars-destroyer",
"https://codegamer.online/g/wedding-beauty-salon",
"https://codegamer.online/g/cat-escape",
"https://codegamer.online/g/impossible-car-stunt-mega-ramp-3d-",
"https://codegamer.online/g/draw-puzzle-sketch-it",
"https://codegamer.online/g/jelly-world",
"https://codegamer.online/g/ben-10-alien",
"https://codegamer.online/g/ertugrul-gazi-horse-sim",
"https://codegamer.online/g/popcorn-pop",
"https://codegamer.online/g/candy-2021-game-2021-gratuit",
"https://codegamer.online/g/hero-rescue-3",
"https://codegamer.online/g/jackie-chan-adventures",
"https://codegamer.online/g/thriving-boy-escape",
"https://codegamer.online/g/foxu--run-run%21",
"https://codegamer.online/g/trophy-escape",
"https://codegamer.online/g/waiter-escape",
"https://codegamer.online/g/dr.-driving",
"https://codegamer.online/g/jumping-puzzle-master",
"https://codegamer.online/g/zuxar-deluxe-2021",
"https://codegamer.online/g/happy-spongy",
"https://codegamer.online/g/sling-race-drift",
"https://codegamer.online/g/snaky.io",
"https://codegamer.online/g/shoot-up-3d-2021",
"https://codegamer.online/g/game-cars-paint",
"https://codegamer.online/g/paint-roller-3d",
"https://codegamer.online/g/among-us-online-new-v2-",
"https://codegamer.online/g/shooting-color-2021",
"https://codegamer.online/g/stickman-killer",
"https://codegamer.online/g/stickman-swing-rope-hero",
"https://codegamer.online/g/pull-him-out-save-daddy-game",
"https://codegamer.online/g/hero-rescue-2--free-puzzle-games",
"https://codegamer.online/g/clean-road",
"https://codegamer.online/g/higher-heels",
"https://codegamer.online/g/super-mario-run-race-online",
"https://codegamer.online/g/blocks-match-game",
"https://codegamer.online/g/draw-spinning",
"https://codegamer.online/g/speed-drag-race-2022"

]

# Process each URL
for url in urls:
    indexURL(url)
    time.sleep(1)  # Avoid hitting rate limits
