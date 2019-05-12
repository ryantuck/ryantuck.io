So you wanna pull some google sheets data into python?

`gspread` is a really handy python module for doing just
that. There's some authentication setup involved but it's
pretty straightforward.

Once you've authenticated, you can check out the `readme`
for basic usage for reading/writing to and from sheets over
at https://github.com/burnash/gspread

## setup

### creds

You need to set up your credentials so you can access your
google sheet. Fortunately this is pretty straightforward.

And the `gspread` documentation also has these instructions
[documented
here](http://gspread.readthedocs.io/en/latest/oauth2.html).

I followed the instructions
[here](https://developers.google.com/identity/protocols/application-default-credentials?authuser=1)
but the **tl;dr** is that you need to head over to the [API
Console
Credentials](https://console.developers.google.com/projectselector/apis/credentials)
section of the google developers portal.

1. Select 'create a project'. Give it a name. Yatta yatta
   yatta.
2. Select 'create credentials' > 'Service Account Key'. I
   think this is the easiest. It'll basically give you a
   file to download.
3. Select 'new service account' and give it the 'Owner'
   role, along with some name.
4. Select `json` key type.
5. Hit 'create'. This should download a `.json` file to your
   computer.
6. Move that credentials file somewhere (let's say
   `~/Desktop`).

### share a sheet

You'll need to share your sheet with the service account you
just created. From the credentials page, you should see a
link for 'Manage Service Accounts'. Check that out and you
should see your service account ID for the one you just
created. It'll look something like

```
rt-testing@123456.iam.gserviceaccount.com
```

Share your sheet with that account. Boom.

## code

### install stuff

```
pip install gspread oauth2client PyOpenSSL
```

### pull sheet

Now pull it! `gspread` has great documentation for using the
module but I've found setup to be a big pain in the ass, so
I hope this post helps.

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# that filename path is the creds file you downloaded
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    filename='/Users/ryan/Desktop/rt-testing-12345678.json',
    scopes='https://spreadsheets.google.com/feeds',
)

gc = gspread.authorize(credentials)

worksheet = gc.open('My Workbook Title').worksheet('some sheet title')

records = worksheet.get_all_records()
```
