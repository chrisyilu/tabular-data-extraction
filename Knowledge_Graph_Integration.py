from rdflib import Graph, URIRef, Literal, Namespace

# create an RDF Graph
g = Graph()

# define a custom namespace for entities
# just an example
ns = Namespace("http://company.com/")

# example entities and relationships
person_entity = ns.person
organization_entity = ns.organization
birth_date_relation = ns.hasBirthDate

# populate the Knowledge Graph
g.add((person_entity, ns.name, Literal("XX XX")))
g.add((person_entity, birth_date_relation, Literal("2000-01-01")))
g.add((organization_entity, ns.name, Literal("company")))
g.add((person_entity, ns.worksFor, organization_entity))

# Serialize and print the Knowledge Graph
print(g.serialize(format="turtle").decode())