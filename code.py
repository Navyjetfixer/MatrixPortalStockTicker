import time
import board
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal
from adafruit_display_text import label

# Testing getting back Quotes
#Real Time https://finnhub.io/docs/api#quote
#https://api.iextrading.com/1.0/tops/last?symbols=wso
#Demo link for testing wihtouth a key "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=Demo"
DATA_SOURCE = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=Demo"
DATA_Price = ["Global Quote","05. price"]
DATA_VOL = ["Global Quote","06. volume"]
DATA_CHG = ["Global Quote","10. change percent"]
DATA_CO = ["Global Quote","01. symbol"]


# the current working directory (where this file is)
cwd = ("/" + __file__).rsplit("/", 1)[0]

FONT = "/fonts/IBMPlexMono-Medium-24_jep.bdf"
FONT2 = "/fonts/helvB12.bdf"
FONT3 = "/fonts/helvR10.bdf"
FONT4 = "/fonts/6x10.bdf"


matrixportal = MatrixPortal(
    url=DATA_SOURCE, json_path=(DATA_Price,DATA_VOL,DATA_CHG,DATA_CO), status_neopixel=board.NEOPIXEL,debug=True
)

#Price
matrixportal.add_text(
    text_font=FONT,
    text_position=(1, 12),
    text_color=(0xC0C0C0),
    text_scale=1.3,
    scrolling=True,
)

#Vol
matrixportal.add_text(
    text_font=FONT,
    #text_font=terminalio.FONT,
    text_position=(1, 23),
    text_color=(0x0000AA),
    scrolling=True,
)

#Change
matrixportal.add_text(
    text_font=FONT2,
    #text_font=terminalio.FONT,
    text_position=(1, 17),
    text_color=(0x00FFFF),
    text_scale=2,
    scrolling=True,
)

#Ticker
matrixportal.add_text(
    #text_font=terminalio.FONT,
    text_font=FONT,
    text_position=(1, 19),
    text_color=(0xFF6600),
    text_scale=1.4,
    scrolling=True,
)

last_check = None

while True:
    if last_check is None or time.monotonic() > last_check + 340:
        try:
            value = matrixportal.fetch()
            print("Response is",value)
            last_check = time.monotonic()
        except (ValueError, RuntimeError) as e:
            print("Some error occured, retrying! -", e)
    matrixportal.scroll()
    time.sleep(.0155)