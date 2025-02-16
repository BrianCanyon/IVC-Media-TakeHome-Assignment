README

This project is meant to capture a take home assignment from IVC media following an interview on Jan 29.
My understanding of the requirements are bulleted below, sub-bullets highlight libraries used:\
    1) Create a categorization algorithm for text based data\
        - NLTK\
        - sklearn\
    2) Create an ETL pipeline that includes event triggers\
        - Requests\
        - Flask\
    3) Define a data warehousing solution (ie. SQL, noSQL, Graph, etc.)\
        - pSQL\
    4) Create an open endpoint API\
        - sqlalchemy

These requirements left a fair amount of room for interpretation. Considering during the interview
there were live demos of AI Slack based tools, I decided to go ahead and create one myself with the
intention of targeting all four of the requirements above in a single project. This project contains
AI data pipeline with integration to a slack channel. Text inputs relating to movie reviews and/or
descriptions can be input to a thread and the bot will run this text against a pretrained model then
return a categorical genre output. For example, if a user types something along the lines of 'the pirate
ship sailed across the seven seas in search of treasure' the app will return 'Adventure'. Please
see the file 'Slack_Thread.png'  for a visual example.

Creation of this bot can be broken down into a few different steps. First, model creation. The file
'TextCategorization.py' leverages libraries 'NLTK' and 'sklearn' (very popular ML/AI libraries) for
model training. With help of ChatGPT to create a large amount of training data, a trained model is
saved locally and leveraged in other scripts. Please note that this file can be ran locally on
any machine with Python configured. In code comments you will see which libraries need to be 
downloaded prior to execution. You will find some helpful print statements as well as descriptions
for following along.

Second, reading messages in Slack in real time needs to be configured. The Python library 'Flask' 
is the most popular for streaming data pipelines. This also requires a fair amount of configuration
within Slack (ie. Access Token, permissions, etc.). With an event trigger setup, the bot will capture
and ingest any messages sent in real time and run them against our previously trained AI model to 
create a categorical prediction. See file 'slack_integration.py'.

Third, the request library is introduced to push messages to slack. For HTTP requests, Requests is
the most popular within Python for achieving this. Using the same event trigger from above, after
the text is run against the ML model, the output is pushed back to the same Slack thread.

Lastly, data is pushed to a SQL database hosted locally on my machine. I went with a very simple
implementation of this using SQLite (lightweight DB solution). The file 'initialize_sqlite_DB' for 
database and table/schema creation. Since there were interview questions about database selection,
I included .md file 'Database Selection' for my thoughts on why SQL remains on top.

That just about summarizes this project, my primary targets were to showcase implementation of each
of the four requirements gathered during interview as well as integrate the most commonly used AI/ML
tools within Python. It should be noted that there are a variety of reasons why this project is not
production ready, however, the path of least resistance to meeting requirements and creation of a live
demo was my primary target.

Feel free to direct any questions or feedback to my personal email: brian.canyon@gmail.com
