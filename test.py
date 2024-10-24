from urllib.parse import urlparse, parse_qs
parsed_uri = urlparse(uri)
query_params = parse_qs(parsed_uri.query)
token = query_params.get('app', [None])[0]
