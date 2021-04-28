from xml.dom import minidom
import simplejson as json


def parse_element(element):
    dict_data = dict()
    if element.nodeType == element.TEXT_NODE:
        dict_data['data'] = element.data
    if element.nodeType not in [element.TEXT_NODE, element.DOCUMENT_NODE, element.DOCUMENT_TYPE_NODE]:
        for item in element.attributes.items():
            dict_data[item[0]] = item[1]
    if element.nodeType not in [element.TEXT_NODE, element.DOCUMENT_TYPE_NODE]:
        for child in element.childNodes:
            if "\\" not in str(child):
                child_name, child_dict = parse_element(child)
                if child_name in dict_data:
                    try:
                        dict_data[child_name].append(child_dict)
                    except AttributeError:
                        dict_data[child_name] = [dict_data[child_name], child_dict]
                else:
                    dict_data[child_name] = child_dict
    return element.nodeName, dict_data
