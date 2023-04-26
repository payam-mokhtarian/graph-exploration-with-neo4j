# Graph Exploration with Neo4j

This repository demostraits an overview on tabular data ingestion to Neo4j graph database following some graph analytics and visualition. In addition, it shows how to buid a RESTfull API endpoint to execute Cypher query estatement. In this exercise, we build application based on Neo4j python driver on Neo4j sandbox environment. This exercise can be done locally using Neo4j Desktop.

The Knowledge Grapgh Game dataset from [KG Game Neo4j]() is used for this exercise. There are four separate tabular datasets as follow:

- [Education](./data/sng_education.csv)
- [Work](./data/sng_work.csv)
- [Trips](./data/sng_trips.csv)
- [Transactions](./data/sng_transaction.csv)

## Tabular to Graph Data Modelling

The firt step prior to create an ingestion pipeline is to understand data model and relationships. Using the structure and accossation in tabular datasets, we can start creating a visual data model. To create a visual data model, we used [arrows.app](https://arrows.app/). Below is the visual representation of the graph with it's nodes, relationships, and their properties:

![Graph Data Model](./data_model/graph_explorer.png)

We can also export the data model as a JSON file. Here is the exported data model [file](./data_model/graph_exploere.josn) in JSON.

## Data Ingestion to a Graph

To ingest the above CSV files to Neo4j Graph Databse using a python application, there are some prerequisites that need to be setup.

### Prerequisites

#### Neo4j GraphDB
To perform this exercise, we need to have Neo4j graph database (GraphDB) on an instance. There are a few ways to set an instance for this purpose; using Neo4j Desktop, Neo4j Sandbos, Neo4j AuraDB and AuraDS. In this exercise, we use Neo4j sandbox. Once a snadbox is set up, it provides Connection Details for remote access as below: 

![Connection Details](./images/connection_details.png)

#### Python Environment
Python 3 is required to create an application to enable a graph and connect to the Neo4j sandbox for execution. In this exercise, we use Google Colab Jupyter Notebook for coding and execution. Note that, we can use any other Python environmen and client. The Colab runtime needs some python modules to prepare the environment for connection to sandbxo and execution. Once a Jupyter notebook on Colab connects to runtime and is running,we install Neo4j modules:

```bash
pip install neo4j
```

Follwoing the execution of modules import:

```python
import pandas as pd
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
```

#### Setup Connection and Driver
To setup connection from python application to Neo4j sandbox and creation driver, we need connection details in the below command:

```python
host = "<BOLT_URL>" 
user = "neo4j" # default
password = "<PASSWORD>"  # default generated

with GraphDatabase.driver(host, auth=(user, password)) as driver:
  driver.verify_connectivity()

session = driver.session(database="neo4j") # default database
```

#### Data Ingestion
Once the python application connects to the sandbox and create deriver, we can execute Cypher queries that load CSV files from the urls to the selected database in the sandbox. The details of creating constraints, index and load statement are in the [Graph Ingestion](./src/graph_ingestion.ipynb) source files and notebooks.


## Graph Analytics
For any further exploration and analytics, we use graph data science (GraphDS) module and Bloom visualisation. 

### Prerequisites
To setup python application to connect for the GraphDS driver, we need the below module installation:

```bash
pip install graphdatascience
```

and create deriver:

```python
host = "<BOLT_URL>" 
user = "neo4j" # default
password = "<PASSWORD>"  # default generated

gds = GraphDataScience(host, auth=(user, password))
gds.set_database("neo4j")
```

### Graph Data Science


### Visual Analytics


## RESTfull API to Execute Cypher Queris
Neo4j Developer API provides a series of HTTP edpoint that allows to perform several actions using Cypher transaction. Using the Connection Details provided in the Neo4j sandbox, we can create an HTTP endpoint host with basic authentication. Below are the detals to establish a Cypher transaction API:

- **POST** `http://{host}:7474/db/{dbname}/tx`
- **Accept:** `application/json;charset=UTF-8`
- **Content-Type:** `application/json`

As this is a POST request, it requires a body to post to the endpoint. For example, the format of the body is:

```json
{
  "statements": [
    {
      "statement": "CREATE (n) RETURN n"
    }
  ]
}
```

The expected result given `200: OK` response looks like:

```json
{
  "results" : [ {
    "columns" : [ "n" ],
    "data" : [ {
      "row" : [ { } ],
      "meta" : [ {
        "id" : 12,
        "type" : "node",
        "deleted" : false
      } ]
    } ]
  } ],
  "errors" : [ ],
  "commit" : "http://{HOST}:7474/db/{dbname}/tx/{txid}/commit",
  "transaction" : {
    "expires" : "EXECUTION_DATE"
  }
}
```

The details of the a python request to call the Cypher transaction API are provides in [Graph API](./src/graph_api.py) source file.
