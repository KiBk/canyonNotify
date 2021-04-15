from bs4 import BeautifulSoup
import requests


class Bike:
    def __init__(self, name, link, size="L"):
        self.name = name
        self.link = link
        self.size = size
        self.avail = False

    def update(self):
        new_avail = parse_url(self.link, self.size)
        changed = self.avail != new_avail
        self.avail = new_avail
        return changed


bike_map = []
# bike_map.append(
#     Bike("Grand_Canyon_5",
#         "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/grand-canyon/grand-canyon-5/2613.html?dwvar_2613_pv_rahmenfarbe=BU%2FBK"
#         )
# )
bike_map.append(
    Bike("Neuron 7 black",
         "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/neuron/neuron-7/2627.html?dwvar_2627_pv_rahmenfarbe=BK%2FGY"
         )
)
bike_map.append(
    Bike("Neuron 7 orange",
         "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/neuron/neuron-7/2627.html?dwvar_2627_pv_rahmenfarbe=GY%2FOG"
         )
)
bike_map.append(
    Bike("Neuron 8 red",
         "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/neuron/neuron-cf-8/2629.html?dwvar_2629_pv_rahmenfarbe=GY%2FRD"
         )
)
bike_map.append(
    Bike("Neuron 8 brown",
         "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/neuron/neuron-cf-8/2629.html?dwvar_2629_pv_rahmenfarbe=GN%2FBK"
         )
)
bike_map.append(
    Bike("Stoic 2",
        "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/stoic/stoic-2/2659.html?dwvar_2659_pv_rahmenfarbe=WH%2FMC"
        )
)
bike_map.append(
    Bike("Stoic 3",
         "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/stoic/stoic-3/2660.html?dwvar_2660_pv_rahmenfarbe=GY"
         )
)
bike_map.append(
    Bike("Spectral 6 black",
         "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/spectral/spectral-6/2675.html?dwvar_2675_pv_rahmenfarbe=BK%2FGY"
         )
)
bike_map.append(
    Bike("Spectral 6 green",
         "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/spectral/spectral-6/2675.html?dwvar_2675_pv_rahmenfarbe=TQ%2FBK"
         )
)
bike_map.append(
    Bike("Spectral 5 green",
         "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/spectral/spectral-5/2674.html?dwvar_2674_pv_rahmenfarbe=TQ%2FBK"
         )
)
bike_map.append(
    Bike("Spectral 5 black",
         "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/spectral/spectral-5/2674.html?dwvar_2674_pv_rahmenfarbe=BK%2FGY"
         )
)


# True or false if the bike is available
def parse_url(url, size):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    # Get the list of iteams
    sizes = soup.find_all(class_="productConfiguration__sizeType")
    for size in sizes:
        # Size and availability condition
        if size.text.strip() == size and size.parent.name.strip() == "button":
            return True
    return False


# Parse all bikes
def update():
    changed = False
    for bike in bike_map:
        changed |= bike.update()
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
