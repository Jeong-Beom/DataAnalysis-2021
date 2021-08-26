import pymysql

def get_monthly_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT DATE_FORMAT(sdate, '%m') AS `month`,
            SUM(revenue) AS revenue, SUM(profit) AS profit
            FROM sales_book
            GROUP BY `month`
            ORDER BY `month`;
    """
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def set_month(config, params):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        update sales set sid=%s, sunit=%s where sid=%s;
    """
    cur.execute(sql, params)
    cur.close()
    conn.close()

def get_scompany_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT scompany,
            SUM(revenue) AS revenue, SUM(profit) AS profit
            FROM sales_book
            GROUP BY `scompany`
            ORDER BY `scompany`;
    """
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def get_scompany_product_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
            SELECT scompany, pname,
                SUM(sunit) as unit
                FROM sales_book
                GROUP BY `scompany`, `pname`
                ORDER BY `scompany`;
        """
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def get_category_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pcategory,
	        SUM(revenue) AS revenue, SUM(profit) AS profit
            FROM sales_book
            GROUP BY `pcategory`
            ORDER BY `pcategory`;
        """
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results

def get_name_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pname,
            SUM(sunit) as unit, 
	        SUM(revenue) AS revenue, SUM(profit) AS profit
            FROM sales_book
            GROUP BY `pname`
            ORDER BY `pname`;
        """
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results