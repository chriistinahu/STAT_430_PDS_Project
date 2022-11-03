# API key ID: otlwwfxero72fkms03hi49x2
# API key secret: 5qbnpzqphl1y8bz6eggxraxlzlnbnhso49bro4925r1rpxj6sn
# app token

# crime data docs: https://dev.socrata.com/foundry/data.cityofchicago.org/9hwr-2zxp

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
import sodapy
from sodapy import Socrata

crime_url = "https://data.cityofchicago.org/resource/9hwr-2zxp.json"
# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.cityofchicago.org", None)


# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("9hwr-2zxp", limit=10000)

# Convert to pandas DataFrame
crime_df = pd.DataFrame.from_records(results)

print(crime_df)

# THIS DOES NOT WORK YET. I AM CONTACTING SUPPORT BC I HAVE NO IDEA HOW TO GET AN APP TOKEN THAT WE NEED TO MAKE THE API CALLS WITH.