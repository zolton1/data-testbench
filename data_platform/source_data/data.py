import duckdb
import time    

class duckDbInstance:
    def __init__(self, host='localhost:9000'):
        self.con = duckdb.connect()
        self.con.execute("INSTALL httpfs;")
        self.con.execute("LOAD httpfs;")
        self.con.execute("INSTALL tpch;")
        self.con.execute("LOAD tpch;")
        self.con.execute("CALL dbgen(sf = 1);")
        self.con.execute("SET s3_use_ssl = false;")
        self.con.execute("SET s3_url_style='path';")
        self.con.execute(f"SET s3_endpoint = '{host}';")
        self.con.execute("SET s3_access_key_id = 'minio';")
        self.con.execute("SET s3_secret_access_key = 'minio123';")
        print("tpch dataset generated")

if __name__=="__main__":
    d = duckDbInstance(host="minio:9000")
    epoch_time = int(time.time())
    print(f"generating dataset {epoch_time}")
    d.con.sql(f"COPY (select * from customer USING SAMPLE 20 PERCENT (bernoulli)) TO 's3://datalake/import/tpch/customer/customer.parquet' ;")
    d.con.sql(f"COPY (select * from lineitem USING SAMPLE 20 PERCENT (bernoulli)) TO 's3://datalake/import/tpch/lineitem/lineitem.parquet' ;")
    d.con.sql(f"COPY (select * from nation USING SAMPLE 20 PERCENT (bernoulli)) TO 's3://datalake/import/tpch/nation/nation.parquet' ;")
    d.con.sql(f"COPY (select * from orders USING SAMPLE 20 PERCENT (bernoulli)) TO 's3://datalake/import/tpch/orders/orders.parquet' ;")
    d.con.sql(f"COPY (select * from part USING SAMPLE 20 PERCENT (bernoulli)) TO 's3://datalake/import/tpch/part/part.parquet' ;")
    d.con.sql(f"COPY (select * from partsupp USING SAMPLE 20 PERCENT (bernoulli)) TO 's3://datalake/import/tpch/partsupp/partsupp.parquet' ;")
    d.con.sql(f"COPY (select * from region USING SAMPLE 20 PERCENT (bernoulli)) TO 's3://datalake/import/tpch/region/region.parquet' ;")
    d.con.sql(f"COPY (select * from supplier USING SAMPLE 20 PERCENT (bernoulli)) TO 's3://datalake/import/tpch/supplier/supplier.parquet' ;")



