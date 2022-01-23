"""
Queries should be handled 2 ways. Basic queries such as "What time is it?" and queries relating to local information such as "Set an alarm..." are handled-
locally and (For the most part) statically. This is to save money querying everything with pay per token APIs like GPT-3.

Queries using pay per token APIs automatically cache previous queries and index those prompts for new queries. This is an optional option though since one-
of the perks of using paid APis is that they have dynamic answers.

Queries should follow this path:

query -> static query? -> out
            |
            v
        cached query? -> out
            |
            v
        api query? -> cache -> out
            |
            v
        none found
            |
            v
        check cache -> cached? -> out
            |
            v
           out

"""

import re
from query.staticQuery import staticQuery
from query.APIQuery import APIQuery

def prepareQuery(query):
    assert query and query != '', 'Unable to handle no/blank query';

    query = query.lower(); # Case doesn't matter
    query = re.sub(r'^\s+|\s+$', '', query); # Remove line breaks from the start and end of the query since they just add tokens
    query = re.sub(r'[^\w\s]', '', query); # Remove punctuation from the query since it just adds tokens

    return query;

class Querier:
    def __init__(self, APIEngine='text-davinci-001', maxTokens=100):
        self.APIEngine = APIEngine;
        self.maxTokens = maxTokens;

    def query(self, inputQuery):
        inputQuery = prepareQuery(inputQuery);
        response = staticQuery(inputQuery);

        if (response):
            return;

        response = APIQuery(inputQuery, self.APIEngine, self.maxTokens);