import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6248192306:AAFda_rBruIYJ-Ylbz2U8bvGeAg93Hcs8oY)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOH8Bu6xci531Lrv2PQr4eObQf5Tc7FdP-KsrEVHDq3Jiz15bk93cfv14X4rChdx8nsQXcxmCeTKzqPq1wvfYOC7Ek5PHbtMDRYrSf6gg-iiawwT-g_Je2eLkrS1k4MdtI-oAcyQqS0W77JXdEA3Cbv4F1LItqEgfeDL-GvPxpOzIeAXqgchKOgirCzz62_TUj06WmLLr7-ZPfdwtvVqW825yNfrGgdR_z5wJVn-Sb6NBsGZfWAWu8jmBFu_BarxHu-Z7cUMEJVfI9ewomYxnHoYhyB-xz8hUpI-ScHuOBb-ZaK5mgyOnzmg8_f4ZCb1-EQhIjxMHvBJLV4Fx7OaZc00K4MU=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
