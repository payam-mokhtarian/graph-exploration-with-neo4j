# -*- coding: utf-8 -*-
"""graph_analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ap6aaRaWghVHES7aV1GfxVi2g0QrJw_v
"""

!pip install neo4j graphdatascience

import pandas as pd
from neo4j import GraphDatabase
from graphdatascience import GraphDataScience
from neo4j.exceptions import ServiceUnavailable

host = "" 
user = "neo4j"
password = ""

gds = GraphDataScience(host, auth=(user, password))
gds.set_database("neo4j")

# Test and verification

query = 'MATCH (country:Country) RETURN country.name AS country_name'
gds.run_cypher(query)

"""## Analytics"""

# Convert string amount to float and remove "$"
query = """
MATCH (c:Card)-[t:TRANSACTED]->(m:Merchant)
SET t.amount = toFloat(substring(t.amount,1))
RETURN t.amount;
"""
gds.run_cypher(query)

# Persons with amount spending
query = """
MATCH (p:Person)-[HAS_CARD]->(c:Card)-[t:TRANSACTED]->(m:Merchant)
RETURN SUM(t.amount) AS total_amount, p.name AS person_name
ORDER BY total_amount DESC;
"""
gds.run_cypher(query)

# Persons with amount spending
query = """
MATCH (p:Person) -[TRAVELLED]-> (c:Country)
RETURN count(c.name) AS number_of_trips, p.name AS person, c.name AS country;
"""
gds.run_cypher(query)

# MATCH (c:Country {name: 'London'})
# SET c.name = 'UK'
# RETURN c.name;

query = """
MATCH (p:Person) -[TRAVELLED]-> (c:Country)
RETURN count(c.name) AS number_of_trips, p.name AS person, c.name AS country;
"""
gds.run_cypher(query)

query = """
MATCH (p:Person)-[e:ENROLLED]->(c:Course)<-[g:GRADUATED]-(p:Person)
RETURN p.name AS person,
 toInteger(e.year) AS enrolment_year,
 toInteger(g.year) AS graduation_year,
 toInteger(g.year) - toInteger(e.year) AS length_of_course
ORDER BY length_of_course DESC;
"""
gds.run_cypher(query)
