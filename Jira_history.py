from pywebio.session import run_js, info

print(json.dumps({
    k: str(getattr(info, k))
    for k in ['user_agent', 'user_language', 'server_host',
              'origin', 'user_ip', 'backend', 'protocol', 'request']
}, indent=4))

import json
