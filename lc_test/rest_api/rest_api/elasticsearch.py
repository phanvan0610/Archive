from elasticsearch import Elasticsearch
import uuid
import logging

es = Elasticsearch([{"host":"178.128.217.254", "port":"9200"}])

def create_lc_test_user_index():
    if not es.indices.exists(index="lc_test_user"):
        body = {
            "mappings":{
                "properties":{
                    "username":{"type":"keyword"},
                    "role":{"type":"text"},
                    "hashed_password":{"type":"text"},
                    "encrypted_private_key":{"type":"text"},
                    "public_key":{"type":"text"},
                    "transactionIdBlockchain":{"type":"text"}
                }
            }
        }
        try:
            res = es.indices.create(index='lc_test_user', body=body)
            return res
        except Exception as e:
            print("already exist")

create_lc_test_user_index()

async def getUserByUsername(
          username,):
    body = {
        "query": {
            "match": {
                "username": username
            }
        }
    }
    res = es.search(index='lc_test_user', body=body)

    try:
      return res['hits']['hits'][0]['_source']
    except:
      return []

async def createUser(
          username,
          role,
          hashed_password,
          encrypted_private_key,
          public_key,
          transactionIdBlockchain):
  body={
        "transactionIdBlockchain":transactionIdBlockchain,
        "username":username,
        "role":role,
        "hashed_password":hashed_password.hex(),
        "encrypted_private_key":encrypted_private_key.hex(),
        "public_key":public_key
  }
  res = es.index(index='lc_test_user', doc_type='_doc', body=body)
  return res

async def check():
    body = {
        "query": {
            "match": {
                "id":
            }
        }
    }
    res = es.search(index='lc_test_product', body=body)
    try:
        return res['hits']['hits'][0]['_source']
    except:
        return []

def create_lc_test_product_index():
  if not es.indices.exists(index="lc_test_product"):
    body={
    "mappings": {
      "properties": {
        "transactionIdBlockchain":{"type":"text"},
        "timestamp":{"type":"date","format":"epoch_second"},
          "content":{"type":"text"},
          "publicKeyUser":{"type":"text"}
        }
      }
    }
    try:
        res = es.indices.create(index='lc_test_product', body=body)
        return res
    except Exception as e:
        print("already exist")
# Create index if not exist
create_lc_test_product_index()

async def createLc(
          transactionIdBlockchain,
          timestamp,
          content,
          publicKeyUser
):

    body = {
        "transactionIdBlockchain":transactionIdBlockchain,
        "timestamp":timestamp,
        "content":content,
        "publicKeyUser":publicKeyUser
    }

    res = es.index(index='lc_test_product', doc_type='_doc', body=body)
    return res


