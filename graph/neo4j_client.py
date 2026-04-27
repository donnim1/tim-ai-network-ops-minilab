from neo4j import GraphDatabase

uri = "neo4j://127.0.0.1:7687"
user = "neo4j"
password = "Iamnimesh1#"

driver = GraphDatabase.driver(uri, auth=(user, password))

def load_graph(tx):
    tx.run("""
        MERGE (t1:Tower {name:'Tower_Rome_1'})
        MERGE (t2:Tower {name:'Tower_Milan_1'})
        MERGE (r1:Router {name:'Router_Rome'})
        MERGE (r2:Router {name:'Router_Milan'})
        MERGE (c:Core {name:'Core_Node_1'})

        MERGE (t1)-[:CONNECTS_TO]->(r1)
        MERGE (t2)-[:CONNECTS_TO]->(r2)
        MERGE (r1)-[:CONNECTS_TO]->(c)
        MERGE (r2)-[:CONNECTS_TO]->(c)
    """)

with driver.session() as session:
    session.execute_write(load_graph)

print("Topology loaded.")
driver.close()