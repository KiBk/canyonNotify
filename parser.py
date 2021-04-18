from config import bike_map
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger("Parser")


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
        output += f"{bike.name} is {('UNavailable','available')[bike.avail]} \n"
    return output


if __name__ == '__main__':
    update()
    print("output is: " + status())
