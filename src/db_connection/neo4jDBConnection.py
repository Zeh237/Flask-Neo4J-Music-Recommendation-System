import os
import logging
from neo4j import GraphDatabase
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Neo4jConnection:
    def __init__(self):
        self.uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self.user = os.getenv("NEO4J_USER")
        self.password = os.getenv("NEO4J_PASSWORD")
        self.auth = (self.user, self.password) if self.user and self.password else None
        self.driver = None

    @contextmanager
    def get_connection(self):
        """Context manager for getting a Neo4j connection that automatically closes"""
        driver = None
        try:
            driver = GraphDatabase.driver(self.uri, auth=self.auth)
            driver.verify_connectivity()
            logging.info("Created new Neo4j connection for query")
            yield driver
        except Exception as e:
            logging.error(f"Error creating Neo4j connection: {e}")
            raise
        finally:
            if driver:
                driver.close()
                logging.info("Closed Neo4j connection")

    def query(self, cypher_query, parameters=None):
        """Execute a query using a temporary connection"""
        try:
            with self.get_connection() as driver:
                with driver.session() as session:
                    result = session.run(cypher_query, parameters)
                    structured_result = [record.data() for record in result]
                    logging.info(f"Query executed successfully: {cypher_query}")
                    return structured_result
        except Exception as e:
            logging.error(f"Error executing query: {e}")
            return None

    def close(self):
        """Close the main driver"""
        if hasattr(self, 'driver') and self.driver:
            self.driver.close()
            logging.info("Neo4j driver closed.")
