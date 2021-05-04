from bs4 import BeautifulSoup
import requests
import logging

logger = logging.getLogger(__name__)

class Bike:
    def __init__(self, name, link, size="L"):
        self.name = name
        self.link = link
        self.size = size
        self.avail = False
        logging.info(f'{name} is created') 

    def update(self):
        new_avail = self.parse_url()
        changed = self.avail != new_avail
        self.avail = new_avail
        logging.info(f'{self.name} status is {("NOT changed","changed")[changed]}')
        return changed

    def parse_url(self):
        req = requests.get(self.link)
        soup = BeautifulSoup(req.text, "html.parser")

        # Get the list of iteams
        sizes = soup.find_all(class_="productConfiguration__sizeType")
        logging.info(
            f'{self.name} parse found {len(sizes)} entries')
        for size in sizes:
            # Size and availability condition
            if size.text.strip() == self.size and size.parent.name.strip() == "button":
                logging.info(f'{self.name} is available in size {self.size}')
                return True
        logging.info(f'{self.name} is NOT available in size {self.size}')
        return False
