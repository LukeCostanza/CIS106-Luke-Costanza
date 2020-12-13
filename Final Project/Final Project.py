##This Program processes values form file plant_catalog.xml and displays adequate results.
##https://pymotw.com/3/xml.etree.ElementTree/parse.html
##https://www.askpython.com/python/string/trim-a-string-in-python


def get_file():
    from xml.etree import ElementTree
    try:
        file = ElementTree.parse("plant_catalog.xml")
    except IOError:
        print ("File not found!")
    except ElementTree.ParseError:
        print ("No elements found!")
    return file


def get_array(tree, type):
    my_array = []
    for x in tree.findall('PLANT'):
        try:
            value = x.find(type).text
            my_array.append(value)
        except ValueError:
            my_array.append(" ")
    return my_array


def print_file(array1, array2, array3, array4, array5):
    size = len(array1)
    for i in range(0, size):
        print (array1[i], "(", array2[i], ") -", array3[i], "-", array4[i], "-", array5[i])
#Prints each required variable from the file.


def print_average(array):
    sum = 0
    count = 0
    size = len(array)
    for i in range(0, size):
        try:
            index = array[i].find("$")
            val_alpha = (array[i])
            value = (val_alpha[index + 1:])
            value = value.strip()
            sum = sum + float(value)
            count = count + 1
        except ValueError:
            pass
    if count != 0:
        average = sum / count
        rounded_average = round(average, 2)
        #To clean up the final answer.
    else:
        rounded_average = 0
    print()
    print ((size), "items - $", (rounded_average), "average price")
#Extra print statement to provide a space between the two sections.


def main():
    tree = get_file()
    common_array = get_array(tree, 'COMMON')
    botanical_array = get_array(tree, 'BOTANICAL')
    zone_array = get_array(tree, 'ZONE')
    light_array = get_array(tree, 'LIGHT')
    price_array = get_array(tree, 'PRICE')
    print_file(common_array, botanical_array, zone_array, light_array, price_array)
    print_average(price_array)

main()
