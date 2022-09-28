from neo4j import GraphDatabase

def demo1():
    grafo=GraphDatabase.driver(uri='bolt://localhost:7687',auth=('neo4j','miguel'))
    sesion=grafo.session()
    q1 = 'MATCH(p:Pais) RETURN p.nombre AS nombre'
    nodos=sesion.run(q1)
    for nodo in nodos:
        print(nodo['nombre'])

def demo2():
    grafo=GraphDatabase.driver(uri='bolt://localhost:7687',auth=('neo4j','miguel'))
    sesion=grafo.session()
    q1 = "MATCH(p:Persona)-[r:LE_GUSTA]->(c:Comida) WHERE p.nombre='JEREMIAS' RETURN c.nombre AS nombre"

    nodos=sesion.run(q1)
    for nodo in nodos:
        print(nodo['nombre'])


demo2()