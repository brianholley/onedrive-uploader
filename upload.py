import onedrivesdk
import secrets
import sys

if len(sys.argv) < 3:
	print "Usage: python upload.py <filepath> <dest filepath>"
	sys.exit()
print "Uploading", sys.argv[1], "as", sys.argv[2]

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
except Exception:
    print "Auth is not up to date - quitting"
    sys.exit()

client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)
auth_provider.save_session()

path_parts = sys.argv[2].split('/')
folders = path_parts[:-1]
filename = path_parts[-1]

if filename == "":
    filename = sys.argv[1].split('/')[-1]

parent = 'root'
for f in folders:
    if f == "": continue
    print "Creating folder:", f, "=>",
    i = onedrivesdk.Item()
    i.name = f
    i.folder = onedrivesdk.Folder()
    created_folder = client.item(drive='me', id=parent).children.add(i)
    parent = created_folder.id
    print parent

print "Uploading", filename
client.item(drive='me', id=parent).children[filename].upload(sys.argv[1])
print "Finished"
