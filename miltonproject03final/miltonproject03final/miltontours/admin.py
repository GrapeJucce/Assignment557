'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltontours package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from miltontours import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from flask import Blueprint
from . import db
from .models import City, Tour, Order
import datetime


bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():
    city1 = City(name='Pastry', image='pastry.jpg', \
        description='Confectionary Items')
    city2 = City(name='Bread', image='bread.jpg', \
        description='General Baked Goods')
    city3 = City(name="Cake", image='cake.jpg', description= 'Dessert Items')

    try:
        db.session.add(city1)
        db.session.add(city2)
        db.session.add(city3)
        db.session.commit()
    except:
        return 'There was an issue adding the cities in dbseed function'
    t1 = Tour(city_id=city1.id, image='pastry1.jpg', price=6.00,\
        date=datetime.datetime(2020, 7, 7),\
        name='Pain au Chocalat',\
        description= 'Home-baked croissant filled with Belgium dark chocolate.A common classic and everyones favourite for breakfast or tea.')
    t2 = Tour(city_id=city1.id, image='pastry2.jpg', price=5.00,\
        date=datetime.datetime(2020, 7, 7),\
        name='Kouign Amann',\
        description= 'Round and sweet Breton cake with flaky layers caramelised by sugar.Best served with tea or coffee')    
    t3 = Tour(city_id=city2.id, image='bread1.jpg', price=6.00,\
        date=datetime.datetime(2020, 7, 7),\
        name='Baguette',\
        description= 'A classic breakfast staple, French baguette with a crispy exterior and chewy interior. ') 

    t4 = Tour(city_id=city2.id, image='bread2.jpg', price=7.00,\
        date=datetime.datetime(2020, 7, 7),\
        name='Baguette',\
        description= 'Homemade sourdough baked through natural fermentation process with organic flours from Australia and natural yeast.')
   
    t5 = Tour(city_id=city3.id, image='cake1.jpg', price=36.00,\
        date=datetime.datetime(2020, 7, 7),\
        name='Chocolate Cake',\
        description= 'Rich chocolate-flavoured cake with Belgium dark chocolate. Cake size is round 6-inch, suitable for 5-6 people.')

    t6 = Tour(city_id=city3.id, image='cake2.jpg', price=42.00,\
        date=datetime.datetime(2020, 7, 7),\
        name='Plain Cheesecake',\
        description= 'Creamy classic cheesecake with graham cracker. Cake size is round 5-inch, suitable for 4-5 people.')
    try:
        db.session.add(t1)
        db.session.add(t2)
        db.session.add(t3)
        db.session.add(t4)
        db.session.add(t5)
        db.session.add(t6)
        db.session.commit()
    except:
        return 'There was an issue adding a tour in dbseed function'

    return 'DATA LOADED'


