from rdflib import Graph, URIRef, Literal, Namespace

# Create an RDF Graph
g = Graph()

# define a custom namespace for entities
ns = Namespace("http://xxxx.com/")

# example entity extracted from text
person_name = "xx xx"
birth_date = "2000-01-01"

# identify key attributes (e.g., name)
key_attribute = person_name

# query the knowledge graph to check if the node already exists
existing_node = g.value(subject=None, predicate=ns.name, object=Literal(key_attribute))

if existing_node:
    # node already exists, retrieve its identifier
    person_node = existing_node
else:
    # node doesn't exist, create a new node
    person_node = ns.Person + URIRef(str(hash(person_name)))
    g.add((person_node, ns.name, Literal(person_name)))
    g.add((person_node, ns.birthDate, Literal(birth_date)))

# 'person_node' is linked to the relevant node in the knowledge graph
print(g.serialize(format="turtle").decode())
