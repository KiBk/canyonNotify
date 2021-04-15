from bs4 import BeautifulSoup
import requests

# url_map = []
# url_map.append(
#     "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/grand-canyon/grand-canyon-5/2613.html?dwvar_2613_pv_rahmenfarbe=BU%2FBK")
# # url_map.append(
# #     "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/neuron/neuron-7/2627.html?dwvar_2627_pv_rahmenfarbe=BK%2FGY")


class Bike:
    def __init__(self, name, link):
        self.name = name
        self.link = link
        self.avail = False

    def update(self):
        new_avail = parse_url(self.link)
        changed = self.avail != new_avail
        self.avail = new_avail
        return changed


bike_map = []
bike_map.append(
    Bike("Grand_Canyon_5",
        "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/grand-canyon/grand-canyon-5/2613.html?dwvar_2613_pv_rahmenfarbe=BU%2FBK"
        )
)
bike_map.append(
    Bike("Neuron 7",
         "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/neuron/neuron-7/2627.html?dwvar_2627_pv_rahmenfarbe=BK%2FGY"
         )
)
    

# Return is send through telegram, return an empty string if no changes
def parse_url(url):
    # url = "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/grand-canyon/grand-canyon-5/2613.html?dwvar_2613_pv_rahmenfarbe=BU%2FBK"
    # url = "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/neuron/neuron-7/2627.html?dwvar_2627_pv_rahmenfarbe=BK%2FGY"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    # Get the list of iteams
    sizes = soup.find_all(class_="productConfiguration__sizeType")
    for size in sizes:
        # Size and availability condition
        if size.text.strip() == "L" and size.parent.name.strip() == "button":
            return True
    return False


# Parse all bikes
def update():
    changed = False
    for bike in bike_map:
        changed |= bike.update()
    return changed


def status():
    output = ""
    for bike in bike_map:
        output += f"{bike.name} is {('UNavailable','available')[bike.avail]} \n"
    return output


if __name__ == '__main__':
    update()
    print("output is: " + status())
