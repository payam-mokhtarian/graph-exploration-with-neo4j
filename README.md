# Graph Exploration with Neo4j

This repository demostraits an overview on tabular data ingestion to Neo4j graph database following some graph analytics and visualition. In addition, it shows how to buid a RESTfull API endpoint to execute Cypher query estatement. In this exercise, we build application based on Neo4j python driver on Neo4j sandbox environment. This exercise can be done locally using Neo4j Desktop.

The Knowledge Grapgh Game dataset from ![KG Game Neo4j]() is used for this exercise. There are four separate tabular datasets as follow:

- [Education](./data/sng_education.csv)
- [Employment](./data/sng_work.csv)
- [Travel](./data/sng_trips.csv)
- [Bank Card Transactions](./data/sng_work.csv)

## Tabular to Graph Data Modelling

The firt step prior to create an ingestion pipeline is to understand data model and relationships. Using the structure and accossation in tabular datasets, we can start creating a visual data model. To create a visual data model, we used ![arrows.app](https://arrows.app/). Below is the visual representation of the graph with it's nodes, relationships, and their properties:

![Graph Data Model](./data_model/graph_explorer.png)

We can also export the data model as a JSON file. Here is the exported data model ![file](./data_model/graph_exploere.josn) in JSON.

## Data Ingestion to a Graph

## Graph Analytics

## RESTfull API to Execute Cypher Queris
