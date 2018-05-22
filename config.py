import os


WEBSOCKET_URL = os.environ.get('WEBSOCKET_URL', "ws://178.62.249.104:8090")

POSTGRES = {'host': os.environ.get('POSTGRES_HOST', 'localhost'),
            'database': os.environ.get('POSTGRES_DATABASE', 'explorer'),
            'user': os.environ.get('POSTGRES_USER', 'postgres'),
            'password': os.environ.get('POSTGRES_PASSWORD', 'posta'),
}

# a connection to a bitshares full node
FULL_WEBSOCKET_URL = os.environ.get('FULL_WEBSOCKET_URL', "ws://178.62.249.104:8090")

# a connection to an ElasticSearch wrapper
#ES_WRAPPER = os.environ.get('ES_WRAPPER', "http://185.208.208.184:5000")


CORE_ASSET_SYMBOL = 'ZGV'
CORE_ASSET_ID = '1.3.0'
