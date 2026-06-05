import xml.etree.ElementTree as ET

xml_data = """
<user>
    <id>1</id>
    <first_name>John Doe</first_name>
    <age>30</age>
    <email>John.doe@gmail.com</email>
</user>
"""

root = ET.ElementTree(ET.fromstring(xml_data))

print("User ID:", root.find('id').text)
print("User name:", root.find('first_name').text)
print("User Email:", root.find('email').text)