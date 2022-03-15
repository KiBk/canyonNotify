from .config import bike_map
from .config import log_level
from time import sleep
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=log_level
)

logger = logging.getLogger(__name__)


# Parse all bikes
def update():
    changed = False
    for bike in bike_map:
        changed |= bike.update()
    logging.info(f'Status of the bikes was {("NOT changed","changed")[changed]}')
    return changed


# Show the info about all bikes
def status():
    output = ""
    for bike in bike_map:
        output += f"{('NO','YES')[bike.avail]} - {bike.name} is {('UNavailable','available')[bike.avail]} in size {bike.size} \n"
    return output


if __name__ == '__main__':
    while True:
        if update():
            print(status())
        else: 
            print(".", end="")
        sleep(60)
