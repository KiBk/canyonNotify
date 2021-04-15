from bs4 import BeautifulSoup
import requests
# True or false if the bike is available

class Bike:
    def __init__(self, name, link, size="L"):
        self.name = name
        self.link = link
        self.size = size
        self.avail = False

    def update(self):
        new_avail = self.parse_url()
        changed = self.avail != new_avail
        self.avail = new_avail
        return changed

    def parse_url(self):
        req = requests.get(self.link)
        soup = BeautifulSoup(req.text, "html.parser")

        # Get the list of iteams
        sizes = soup.find_all(class_="productConfiguration__sizeType")
        for size in sizes:
            # Size and availability condition
            if size.text.strip() == self.size and size.parent.name.strip() == "button":
                return True
        return False
