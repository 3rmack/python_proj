from xml.etree import ElementTree

result = {"red": 0,
          "blue": 0,
          "green": 0}

xml = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
# tree = ElementTree.parse("xml_example.xml")
# tree = ElementTree.parse(xml)
# root = tree.getroot()
root = ElementTree.fromstring(xml)
result[root.attrib['color']] += 1


def get_child(root, result, i=1):
    i += 1
    for child in root:
        result[child.attrib['color']] += i
        get_child(child, result, i)


get_child(root, result)
# print(result)
print("{} {} {}".format(result["red"], result["green"], result["blue"]))
