# DIS

To start the website, you'll need to do 4 things:

1. First, you must install the required Python packages with `pip install -r requirements.txt`.
2. The file paths in `CreateKebab.sql` and `CreatePosts.sql` must be changed to where `src/tmp/kebab.csv` 
   and `src/tmp/posts.csv` is on your device.
3. All the tables need to be created with `psql -d [database] -U [username] -W -f Create[table name].sql`.
4. Database information on line 11 in `app.py` must be changed to your own database.

If you've followed the steps above, you should be able to start the website with `py app.py` 
or on Mac `python3 app.py`.

The terminal will tell you which web address the website can be found on, like: `* Running on http://[address]`.

------------------------------------------------------------------------------------------------------------------

# How to use the website

1. Create an account. This can be done by clicking the create an account link. Here we used regex for passwords.
2. Login. After creating your account you'll be back at the login screen. Just input the username and password
   you registered.
3. Homepage. Here you can navigate navigate to other sites and see how many post you've made, called Kebab Score.
4. Post. You can make a post about an experience you've had at a kebab place and give the place a score.
5. Kebab Places. A list of all the kebab places that are in the database with all the information they have.
6. Den Lokale. Here you can choose your favorite kebab place. Additionally, if you have a Den Lokale, it will 
   display information about the place and how many times you've posted about it (visited).
7. Feed will display the posts made by the users that you follow (and your own), ordered by when the post was created. 
   When you create an account, you will automatically follow three users, so there will be something on the feed page.
8. Followers. Shows you the usernames of the users you follow and allows you to add new followers to follow.