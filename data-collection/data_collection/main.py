from dotenv import dotenv_values
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Load configuration from '.env' file in root folder
config = dotenv_values(".env")

token = f"token {config['SOURCEGRAPH_TOKEN']}"
url = config["SOURCEGRAPH_API_ENDPOINT"]

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url=url, headers={"Authorization": token})

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# Provide a GraphQL query
# TODO: build query to obtain the code
query = gql(
    """
    query {
        currentUser {
            username
        }
    }
"""
)

# Execute the query on the transport
result = client.execute(query)
print(result["currentUser"])


# save query in csv & files
