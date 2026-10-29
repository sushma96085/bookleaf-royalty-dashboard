"""Configure the bundled starter using a verified endpoint; no credentials are saved."""
import argparse,json
from pathlib import Path
from urllib.parse import urlparse
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--bubble-log-url',required=True)
a=p.parse_args()
u=urlparse(a.bubble_log_url)
if u.scheme!='https' or not u.hostname or u.username or u.password or u.query or u.fragment or 'YOUR_' in a.bubble_log_url or 'PLACEHOLDER' in a.bubble_log_url or '/api/' not in u.path:
    p.error('Supply a verified HTTPS API endpoint without credentials, query parameters or placeholders.')
root=Path(__file__).resolve().parents[1]
f=root/'n8n_bubble_starter/bookleaf_assignment2_package/n8n/bookleaf_royalty_notification.json'
d=json.loads(f.read_text())
for node in d['nodes']:
    if node['name']=='Log Success to Bubble':
        node['parameters']['url']=a.bubble_log_url
out=root/'n8n-configured.json'
out.write_text(json.dumps(d,indent=2)+'\n')
print('Created:',out.name)
print('Starter only: configure credentials, body fields and webhook auth before testing. Live API not verified.')
