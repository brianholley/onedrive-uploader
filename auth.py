import onedrivesdk
import secrets

scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
api_base_url = 'https://api.onedrive.com/v1.0/'
http_provider = onedrivesdk.HttpProvider()
auth_provider = onedrivesdk.AuthProvider(
    http_provider=http_provider,
    client_id=secrets.client_id,
    scopes=scopes)

try:
    auth_provider.load_session()
    auth_provider.refresh_token()
    reauth = False
except Exception:
    reauth = True

client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)

if reauth:
    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    print('Paste this URL into your browser, approve the app\'s access.')
    print('Copy everything in the address bar after "code=", and paste it below.')
    print(auth_url)
    code = input('Paste code here: ')

    client.auth_provider.authenticate(code, redirect_uri, client_secret)

auth_provider.save_session()

