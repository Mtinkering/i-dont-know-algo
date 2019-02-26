# NoSQL vs SQL
SQL: ACID property, suitable for financial transactions
NoSQL: like TWITCH chat, write heavy, not so stressed about consistency 

SQL: data across tables, collect by JOIN. Can select a column. 
NoSQL: everything in one document. Can't select a column though

SQL: schema. slower due to constraint PK, FK . 
NoSQL: schemaless. Fast read and write

ACID:
- Atomicity: all transactions must fail or complete as a whole
- Consitency: all nodes in the cluster must be indentical. => wait for all nodes to write before returning to the client
- Durability: write to disk first then reply to client


Dropping atomicity: can reduce the number of tables locked. CouchDB, mongoDB
Dropping consitency: heavy write like Cassandra
Dropping Durability: like redis, memcached. This makes sense because if the write was not successful, then just need to fetch again