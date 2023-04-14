import logging

from cartography.util import load_resource_binary

logger = logging.getLogger(__name__)


def get_index_statements():
    statements = []
    with load_resource_binary('cartography.data', 'indexes.cypher') as f:
        statements.extend(
            line.decode('UTF-8').rstrip('\r\n') for line in f.readlines()
        )
    return statements


def run(neo4j_session, config):
    logger.info("Creating indexes for cartography node types.")
    for statement in get_index_statements():
        logger.debug("Executing statement: %s", statement)
        neo4j_session.run(statement)
