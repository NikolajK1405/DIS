# DIS

To start the website, you'll need to do 4 things:

1. First, you must install the required Python packages with `pip install -r requirements.txt`.
2. The file path in `CreateKebab.sql` must be changed to where `src/tmp/kebab.csv` is on your device.
3. All the tables need to be created with `psql -d test -U postgres -W -f Create[table name].sql`.
4. Database information on line 11 in `app.py` must be changed to your own database.

If you've followed the steps above, you should be able to start the website with `py app.py` 
or on Mac `python3 app.py`.

The terminal will tell you which web address the website can be found on, like: `* Running on http://[address]`.