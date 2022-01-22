"""
SonOfAnton
created by: nekumelon
version: v0.0.1
"""

import platform, query.query as query, IO.io as io

assert platform.system() == 'Windows', 'At the moment, Microsoft Windows (10>) is the only operating system compatible with SonOfAnton';

querier = query.Querier();

while (True):
    inputQuery = io.inp();
    querier.query(inputQuery);