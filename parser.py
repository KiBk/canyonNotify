from config import bike_map


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
