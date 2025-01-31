Database Selection
To lead with the conclusion, PostgreSQL (pSQL) would be my go-to database for a variety of reasons that I will
discuss below. The primary reason is its widespread use in production-level environments across both large and 
small-scale organizations around the world. Opting for a product with an extensive community behind it is 
beneficial when problems arise (as they always seem to).

SQL databases are primarily meant for structured data (i.e., data with columns and rows). Lately, NoSQL databases
(semi-structured, JSON) have gained popularity (e.g., MongoDB, Cassandra). PostgreSQL has caught on with this 
trend and recently gained the functionality of working with both structured and semi-structured data. This allows
for a lot of flexibility when requirements change or database additions need to be made.

Another benefit of working with SQL databases is the structured nature of the data storage. This allows for
seamless integration with tools like Excel or BI tools (e.g., Looker), enabling all relevant stakeholders to work
with data without requiring a technical background. Choosing a NoSQL database like MongoDB or a vector/graph 
database such as Milvus greatly limits how data can be stored and usually has a limited use case.

It is important to recognize why these database styles are gaining popularity. It is due to the size and scale of
data being aggregated by some companies growing exponentially. For example, Twitter needs to process hundreds of 
gigabytes of text data every hour. When working with data at this size and scale, database options outside of SQL
become more attractive because of performance. However, unless development truly reaches hundreds of terabytes
in scale, SQL (or some variant like PostgreSQL) is still, in my opinion, the most attractive option.

I am happy to discuss this further if there are questions.