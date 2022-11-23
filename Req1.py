@app.route("/")

defroot():

    logged_in, first_name, no_of_items = get_login_details()

    withsqlite3.connect('database.db') as conn:

        cur= conn.cursor()

        # Show last product added

        cur.execute('SELECT productId, name, price, description, image, stock FROM products ORDER BY productId DESC LIMIT 1 ')

        # Show all items

        #cur.execute('SELECT productId, name, price, description, image, stock FROM products LIMIT 1')

        item_data= cur.fetchall()

        # Show an error instead of the categories

        category_data= [(-1,"Error")]

        # Show all categories

        #cur.execute('SELECT categoryId, name FROM categories')

        #category_data = cur.fetchall()

    item_data= parse(item_data)

    returnrender_template('home.html', itemData=item_data, loggedIn=logged_in, firstName=first_name, noOfItems=no_of_items, categoryData=category_data)
 
