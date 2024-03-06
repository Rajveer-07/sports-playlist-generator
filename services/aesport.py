from helpers import get_base_url
from bs4 import BeautifulSoup
from . import BaseService


class AESport(BaseService):
    def __init__(self) -> None:
        super().__init__(
            SERVICE_NAME="AESport",
            SERVICE_URL="https://aesport.tv/live-tv.html",
        )

    def _get_data(self) -> dict:
        soup = BeautifulSoup(self._get_src(), "html.parser")

        channels_data = []

        sections_divs = soup.select(".section-focus")
        for section_div in sections_divs:
            channels_divs = section_div.select(".tv-item")
            for channel_div in channels_divs:
                channels_data.append({
                    "name": channel_div.select_one("div.channel-name").text.strip(),
                    # "logo": channel_div.select_one("img.hide").get("src"),
                    "logo": "https://i.postimg.cc/c6q46Q7v/SPIDY-LOGO-2.png",
                    # "group": section_div.select_one("div.left").text.strip(),
                    "group": "𝘼𝙀𝙎𝙥𝙤𝙧𝙩",
                    "stream-url": channel_div.select_one("img.preview-tv").get("src").replace("preview.jpg", "index.m3u8"),
                    "headers": {
                        "referer": get_base_url(channel_div.parent.get("href")) + "/",
                        "user-agent": self.USER_AGENT
                    }
                })

        return channels_data
