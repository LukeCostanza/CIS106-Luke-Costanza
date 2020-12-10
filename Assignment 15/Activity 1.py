from xml.dom import minidom


def main():
    mydoc = minidom.parse('plants.xml')
    plants = mydoc.getElementsByTagName('COMMON')
    print(plants[1].attributes['COMMON'].value)


main()
