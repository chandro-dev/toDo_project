# back/app/__init__.py
import os
from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from app import create_app
app = create_app()

if __name__ == "__main__":
    # DEV local: python back/app/__init__.py
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)), debug=True)


try:
    row_count = 0
    for df_chunk in wr.s3.read_parquet(path='s3://arn:aws:s3:us-east-1:891377143548:accesspoint/ada-us-east-1-data-live-ar-datatmp-ap/tmp/kbtq/master/kbtq/t_kbtq_cust_contact_chan_tmp/gf_cutoff_date=2025-09-19/'):
        row_count += len(df_chunk)
        print("Cantidad de registros:", row_count)
except Exception as e:
    print(str(e))