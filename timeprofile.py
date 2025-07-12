from pyrubi import Client
from PIL import Image, ImageDraw
from datetime import datetime
import math
import time

bot = Client("acc")

OWNER_GUID = "u0H9jHc0fa5596fb820e2df1e879db37"
GROUP_GUID = "g0F3Kj30ad949d2c2ab97ff036386cff"
CLOCK_BASE = "clock.jpg"
CLOCK_OUTPUT = "clock_with_hands.png"

def draw_clock():
    now = datetime.now()
    hour = now.hour % 12
    minute = now.minute

    img = Image.open(CLOCK_BASE).convert("RGBA")
    draw = ImageDraw.Draw(img)

    center = (img.width // 2, img.height // 2)
    radius = img.width // 2 - 20

    def point(angle, length):
        rad = math.radians(angle - 90)
        return (
            center[0] + length * math.cos(rad),
            center[1] + length * math.sin(rad)
        )

    minute_angle = (minute / 60) * 360
    hour_angle = ((hour + minute / 60) / 12) * 360

    draw.line([center, point(hour_angle, radius * 0.5)], fill="black", width=8)
    draw.line([center, point(minute_angle, radius * 0.8)], fill="blue", width=4)

    img.save(CLOCK_OUTPUT)

print(" اتصال به روبیکا...")
bot.send_text(OWNER_GUID, "✅ ربات با موفقیت روشن شد")

while True:
    now = datetime.now()
    if now.second == 0:
        try:
            draw_clock()
            bot.upload_avatar(GROUP_GUID, CLOCK_OUTPUT)
            print(f"✅ آپدیت شد: {now.strftime('%H:%M:%S')}")
        except Exception as e:
            print(f"⚠️ خطا: {e}")
        time.sleep(1.5)
    else:
        time.sleep(0.5)