from bs4 import BeautifulSoup
import requests

def check():
    url = "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/grand-canyon/grand-canyon-5/2613.html?dwvar_2613_pv_rahmenfarbe=BU%2FBK"
    # url = "https://www.canyon.com/en-no/mountain-bikes/trail-bikes/neuron/neuron-7/2627.html?dwvar_2627_pv_rahmenfarbe=BK%2FGY"
    req = requests.get(url)
    # print (req.text)
    soup = BeautifulSoup(req.text, "html.parser")
    # print(soup.prettify())

    # productConfiguration__optionListItem
    # productConfiguration__selectFrameSize
    options = soup.find_all(class_="productConfiguration__selectFrameSize")
    # print (len(options))

    for option in options:
        if option.name.strip() == "button":
            print ("Hey, available")
        return True
    return False

if __name__ == '__main__':
    check()
