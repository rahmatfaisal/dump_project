from google.colab import auth #import auth 
from google.cloud import bigquery

auth.authenticate_user()
client = bigquery.Client(project='project-01-257405') #project=projectID

QUERY = ('SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = "TX" '
        'LIMIT 100')

query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
        print(row.name)
