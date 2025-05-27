# Parsing XML using DOM
import xml.dom.minidom
import datetime


DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term') # Find all <term> elements

# Initialize variables that record the term with the greatest number of <is_a> elements and the number of <is_a> elements it is associated with for each ontology
max_mf = 0
max_mf_term = ''
max_bp = 0
max_bp_term = ''
max_cc = 0
max_cc_term = ''

t1 = datetime.datetime.now()

# Loop through all terms and update the greatest number of <is_a> elements for each ontology
for term in terms:
    namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    is_a_list = term.getElementsByTagName('is_a')
    if namespace == 'molecular_function' and len(is_a_list) > max_mf:
        max_mf = len(is_a_list)
        max_mf_term = term.getElementsByTagName('name')[0].firstChild.nodeValue
    if namespace == 'biological_process' and len(is_a_list) > max_bp:
        max_bp = len(is_a_list)
        max_bp_term = term.getElementsByTagName('name')[0].firstChild.nodeValue
    if namespace == 'cellular_component' and len(is_a_list) > max_cc:
        max_cc = len(is_a_list)
        max_cc_term = term.getElementsByTagName('name')[0].firstChild.nodeValue

t2 = datetime.datetime.now()

# Print the results
print(f"Parsing XML using DOM")
print(f"***Molecular Function***")
print(f"Term with the greatest number of <is_a> elements: {max_mf_term}")
print(f"Number of <is_a> elements: {max_mf}")
print(f"***Biological Process***")
print(f"Term with the greatest number of <is_a> elements: {max_bp_term}")
print(f"Number of <is_a> elements: {max_bp}")
print(f"***Cellular Component***")
print(f"Term with the greatest number of <is_a> elements: {max_cc_term}")
print(f"Number of <is_a> elements: {max_cc}")
print(f"Time taken:{t2-t1}")

