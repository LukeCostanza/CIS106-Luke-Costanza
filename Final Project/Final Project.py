# This Program will print out the required data provided by a file and process given variables.
# https://pymotw.com/3/xml.etree.ElementTree/parse.html

from xml.etree import ElementTree


#with open('plants.xml', 'rt') as f:
tree = ElementTree.parse("plants.xml")


def get_common():
    common_arr = []
    for x in tree.findall('PLANT'):
        common = x.find('COMMON').text
        common_arr.append(common)
    return common_arr


def get_botanical():
    botanical_arr = []
    for x in tree.findall('PLANT'):
        botanical = x.find('BOTANICAL').text
        botanical_arr.append(botanical)
    return botanical_arr


def get_zone():
    zone_arr = []
    for x in tree.findall('PLANT'):
        zone = x.find('ZONE').text
        zone_arr.append(zone)
    return zone_arr


def get_light():
    light_arr = []
    for x in tree.findall('PLANT'):
        light = x.find('LIGHT').text
        light_arr.append(light)
    return light_arr


def get_price():
    price_arr = []
    for x in tree.findall('PLANT'):
        price = x.find('PRICE').text
        price_arr.append(price)
    return price_arr


#for node in tree.iter():
    #print(node.tag)


def main():
    common_arr = get_common()
    botanical_arr = get_botanical()
    zone_arr = get_zone()
    light_arr = get_light()
    price_arr = get_price()
    print (common_arr[8])
    print (botanical_arr[8])
    print (zone_arr[8])
    print (light_arr[8])
    print (price_arr[8])


main()
