# Parsing XML using DOM
import xml.dom.minidom
import datetime

t1 = datetime.datetime.now()

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
print(f"Parsing XML using DOM\n")
print(f"***Molecular Function***")
print(f"Term with the greatest number of <is_a> elements: {max_mf_term}")
print(f"Number of <is_a> elements: {max_mf}\n")
print(f"***Biological Process***")
print(f"Term with the greatest number of <is_a> elements: {max_bp_term}")
print(f"Number of <is_a> elements: {max_bp}\n")
print(f"***Cellular Component***")
print(f"Term with the greatest number of <is_a> elements: {max_cc_term}")
print(f"Number of <is_a> elements: {max_cc}\n")
print(f"Time taken:{t2-t1}\n")


# Parsing XML using SAX
print("********************")

import xml.sax
import datetime

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.namespace = ""
        self.term_name = ""
        self.is_a_count = 0
        # Record the term with the greatest number of <is_a> elements for each ontology in these dictionaries
        self.max_mf = {'count': 0, 'name': ''}
        self.max_bp = {'count': 0, 'name': ''}
        self.max_cc = {'count': 0, 'name': ''}
    
    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == "is_a":
            self.is_a_count += 1
        elif tag == "name":
            self.in_name = True
            self.term_name = ""
        elif tag == "namespace":
            self.in_namespace = True
            self.namespace = ""
    
    def characters(self, content):
        if self.current_data == 'name' and self.in_name == True:
            self.term_name = content
        elif self.current_data == 'namespace' and self.in_namespace == True:
            self.namespace = content
    
    def endElement(self, tag):
        if tag == "name":
            self.in_name = False
        elif tag == "namespace":
            self.in_namespace = False
        elif tag == "term":
            if self.namespace == 'molecular_function' and self.is_a_count > self.max_mf['count']:
                self.max_mf = {'count': self.is_a_count,'name': self.term_name}
            elif self.namespace == 'biological_process' and self.is_a_count > self.max_bp['count']:
                self.max_bp = {'count': self.is_a_count,'name': self.term_name}
            elif self.namespace == 'cellular_component' and self.is_a_count > self.max_cc['count']:
                self.max_cc = {'count': self.is_a_count,'name': self.term_name}
            # Reinitialize
            self.is_a_count = 0
            self.term_name = ""
            self.namespace = ""

# Open the file go_obo.xml
t3 = datetime.datetime.now()

parser = xml.sax.make_parser() # Create an XMLReader
parser.setFeature(xml.sax.handler.feature_namespaces,0) # Turn off namespaces
handler = GOHandler() # Set ContentHandler called 'GOHandler'
parser.setContentHandler(handler)
parser.parse("go_obo.xml")

t4 = datetime.datetime.now()

# Print results
print(f"\nParsing XML using SAX\n")
print(f"***Molecular Function***")
print(f"Term with the greatest number of <is_a> elements: {handler.max_mf['name']}")
print(f"Number of <is_a> elements: {handler.max_mf['count']}\n")
print(f"***Biological Process***")
print(f"Term with the greatest number of <is_a> elements: {handler.max_bp['name']}")
print(f"Number of <is_a> elements: {handler.max_bp['count']}\n")
print(f"***Cellular Component***")
print(f"Term with the greatest number of <is_a> elements: {handler.max_cc['name']}")
print(f"Number of <is_a> elements: {handler.max_cc['count']}\n")
print(f"Time taken: {t4-t3}\n")

# Compare the time taken for each API to complete its task
if (t2 - t1) < (t4 - t3):
    print(f"DOM is faster than SAX.")
elif (t2 - t1) > (t4 - t3):
    print(f"SAX is faster than DOM.")
elif (t2 - t1) == (t4 - t3):
    print(f"DOM and SAX took the same time.")

# Parsing with SAX is faster than parsing with DOM