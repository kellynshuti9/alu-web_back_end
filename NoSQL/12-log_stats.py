#!/usr/bin/env python3
""" 12. Log stats
"""

from pymongo import MongoClient

def log_stats():
    """ log_stats.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    
    total = collection.count_documents({})
    get = collection.count_documents({"method": "GET"})
    post = collection.count_documents({"method": "POST"})
    put = collection.count_documents({"method": "PUT"})
    patch = collection.count_documents({"method": "PATCH"})
    delete = collection.count_documents({"method": "DELETE"})
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
