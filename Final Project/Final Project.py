#This Program will print out the required data provided by a file and process given variables.
    #https://stackabuse.com/reading-and-writing-xml-files-in-python/
    
    
from xml.dom import minidom


def main():
    mydoc = minidom.parse('plants.xml')
    plants = mydoc.getElementsByTagName('COMMON')
    print(plants[1].attributes['COMMON'].value)


main()
