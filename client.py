# Import Elasticsearch package
from elasticsearch import Elasticsearch
# Connect to the elastic cluster
es=Elasticsearch([{'host':'192.168.40.107','port':9200}])
print(es)
e1={
    "first_name":"nitin",
    "last_name":"panwar",
    "age": 27,
    "about": "Love to play cricket",
    "interests": ['sports','music'],
}
res = es.index(index='megacorp',doc_type='employee',id=1,body=e1)
e2={
    "first_name" :  "Jane",
    "last_name" :   "Smith",
    "age" :         32,
    "about" :       "I like to collect rock albums",
    "interests":  [ "music" ]
}
e3={
    "first_name" :  "Douglas",
    "last_name" :   "Fir",
    "age" :         35,
    "about":        "I like to build cabinets",
    "interests":  [ "forestry" ]
}
res=es.index(index='megacorp',doc_type='employee',id=2,body=e2)
print(res)
res=es.index(index='megacorp',doc_type='employee',id=3,body=e3)
print (res)
res=es.get(index='megacorp',doc_type='employee',id=3)
print(res)

print(res['_source'])
res=es.delete(index='megacorp',doc_type='employee',id=3)
print(res['result'])
res= es.search(index='megacorp',body={'query':{'match_all':{}}})
print(res['hits'])
res= es.search(index='megacorp',body={'query':{'match':{'first_name':'nitin'}}})
print (res['hits']['hits'])

res= es.search(index='megacorp',body={
        'query':{
            'bool':{
                'must':[{
                        'match':{
                            'first_name':'nitin'
                        }
                    }]
            }
        }
    })

res= es.search(index='megacorp',body={
        'query':{
            'bool':{
                'must':{
                    'match':{
                        'first_name':'nitin'
                    }
                },
                "filter":{
                    "range":{
                        "age":{
                            "gt":25
                        }
                    }
                }
            }
        }
    })

print(res['hits']['hits'])
e4={
    "first_name":"asd",
    "last_name":"pafdfd",
    "age": 27,
    "about": "Love to play football",
    "interests": ['sports','music'],
}
res=es.index(index='megacorp',doc_type='employee',id=4,body=e4)
res= es.search(index='megacorp', body={
        'query':{
            'match':{
                "about":"play cricket"
            }
        }
    })
for hit in res['hits']['hits']:
    print (hit['_source']['about'])
    print (hit['_score'])
    print ('**********************') 
res= es.search(index='megacorp',body={
        'query':{
            'match_phrase':{
                "about":"play cricket"
            }
        }
    })
for hit in res['hits']['hits']:
    print (hit['_source']['about'] )
    print (hit['_score'])
    print ('**********************')
res= es.search(index='megacorp',body={
        "query": {
            "range": {
            "age": { "lte": "32" }
            }
        }
    })
print(res['hits']['hits'] )