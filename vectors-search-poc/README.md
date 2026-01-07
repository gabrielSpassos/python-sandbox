# Vectors Search POC

### What is

* Vector search is an AI-powered technique that finds data (text, images, audio, etc.) by converting it into numerical lists called vectors (or embeddings) and then finding items whose vectors are numerically closest, representing semantic similarity rather than just keyword matches, powering semantic search and recommendation engines. 

![arch](./vectors-search-poc/embedding-search.png)


### Usage

* Configure venv
```bash
python3 -m venv .venv
source .venv/bin/activate
```


* Install dependencies
```bash
pip3 install -r requirements.txt
```

* Build vectors 
```bash
python3 -m src.index
```

* Run search api
```bash
uvicorn src.api:app --reload
```

* Query about vector search
```bash
curl "http://localhost:8000/search?q=what+is+vector+search"
```

```json
{
   "query":"what is vector search",
   "results":[
      {
         "id":"11",
         "text":"Vector search uses embeddings to find semantically similar documents instead of exact keyword matches.",
         "score":0.6645376682281494
      },
      {
         "id":"22",
         "text":"Elasticsearch can perform approximate nearest neighbor searches using dense vector fields.",
         "score":0.797502338886261
      },
      {
         "id":"21",
         "text":"OpenSearch provides k-NN search capabilities using vector fields and ANN algorithms.",
         "score":0.8590518236160278
      },
      {
         "id":"24",
         "text":"Weaviate supports vector search with schema-based metadata and hybrid queries.",
         "score":0.883150577545166
      },
      {
         "id":"23",
         "text":"Pinecone is a managed vector database optimized for large-scale similarity search.",
         "score":0.889991819858551
      }
   ]
}
```

* Query about auto scaling
```bash
curl "http://localhost:8000/search?q=how+can+auto-scale+my+application"
```

```json
{
   "query":"how can auto-scale my application",
   "results":[
      {
         "id":"1",
         "text":"Kubernetes Horizontal Pod Autoscaler automatically scales the number of pods based on CPU or custom metrics.",
         "score":1.0372390747070312
      },
      {
         "id":"9",
         "text":"Vertical scaling increases the resources allocated to a single instance.",
         "score":1.083997368812561
      },
      {
         "id":"8",
         "text":"Horizontal scaling improves throughput by adding more replicas of a service.",
         "score":1.183692216873169
      },
      {
         "id":"32",
         "text":"Continuous Deployment automates the release of applications into production environments.",
         "score":1.2167726755142212
      },
      {
         "id":"2",
         "text":"Vertical Pod Autoscaler adjusts CPU and memory requests for pods to improve resource utilization.",
         "score":1.2492738962173462
      }
   ]
}
```