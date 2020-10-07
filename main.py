import pymysql
 
connection = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      db='myshop'
                      )

def getBill(index):
    cursor = connection.cursor()
    query = "SELECT products.name, products.price, bill.number_of_prod, bill.number_of_prod*products.price FROM bill join products WHERE products.id = bill.id_pro AND bill.id = %s"
    val = (index)
    cursor.execute(query, val)
    if cursor.rowcount == 0:
        print("ERROR")
        exit()
    else:
        return cursor.fetchall()

# Add new product to bill
def insertToBill(index, id_p, qlt):
    cursor = connection.cursor()
    sql = "INSERT INTO `bill` (`id`, `id_pro`, `number_of_prod`) VALUES (%s, %s, %s)"
    val = (index, id_p, qlt)
    cursor.execute(sql, val)
    connection.commit()

# Check id_product
def checkID(id):
    cursor = connection.cursor()
    sql = "SELECT * FROM `products` WHERE products.id = %s"
    val = (id)
    cursor.execute(sql, val)
    return True if cursor.fetchall() != () else False

# Get price a product
def getNamePrice(id):
    cursor = connection.cursor()
    sql = "SELECT products.name, products.price FROM `products` WHERE products.id = %s"
    val = (id)
    cursor.execute(sql, val)
    a = cursor.fetchall()[0]
    return [a[0], a[1]] 

# Get total
def getTotal(index): 
    cursor = connection.cursor()
    sql = "SELECT products.price * bill.number_of_prod FROM `bill` JOIN products WHERE products.id = bill.id_pro AND bill.id = %s"
    val = (index)
    cursor.execute(sql, val)
    return sum([i[0] for i in cursor.fetchall()])

# Insert product
def insertProduct(id, name, price):
    cursor = connection.cursor()
    sql = "INSERT INTO `products`(`id`, `name`, `price`) VALUES (%s,%s,%s)"
    val = (id, name, price)
    cursor.execute(sql, val)
    connection.commit()

# Delete product 
def deleteProduct(id):
    cursor = connection.cursor()
    sql = "DELETE FROM `products` WHERE products.id = %s"
    val = (id)
    cursor.execute(sql, val)
    connection.commit()
# Update product 
def updateProduct(id, name, price):
    cursor = connection.cursor()
    sql = "UPDATE `products` SET `id`=%s,`name`=%s,`price`=%s WHERE `id`=%s"
    val = (id, name, price, id)
    cursor.execute(sql, val)
    connection.commit()

if __name__ == "__main__":
    updateProduct('4', "bot mi", '7000')