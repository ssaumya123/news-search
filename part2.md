# Part2 - Riak Tasks
I have gone through the basho's documentation to learn how to use Riak without installation.

## Assumptions
I am only using documentation for writing sample example curl commands to insert or retrieve cached results from Riak Database.

## Example Curl Request for cache result1 with OR query 
The following curl request command to cache the result from the Acceptance criteria having query as "Care Quality Commission" and with search type as "OR":
```
where bucket='hsic-news'
curl -XPUT -H "Content-Type: text/plain" -d "0,1,2,3,4,5,6" http://<Riak_backend_IP>:<Riak_backend_PORT>/buckets/hsic-news/keys/'Care Quality Commission'
```

## Example Curl Request for cache result2 with OR query
The following curl request command to cache the result from the Acceptance criteria having query as "September 2004" and with search type as "OR":
```
where bucket='hsic-news'
curl -XPUT -H "Content-Type: text/plain" -d "9" http://<Riak_backend_IP>:<Riak_backend_PORT>/buckets/hsic-news/keys/'September 2004'
```

## Example Curl Request for cache result3 with OR query
The following curl request command to cache the result from the Acceptance criteria having query as "general population generally" and with search type as "OR":
```
where bucket='hsic-news'
curl -XPUT -H "Content-Type: text/plain" -d "6,8" http://<Riak_backend_IP>:<Riak_backend_PORT>/buckets/hsic-news/keys/'general population generally'
```

## Example Curl Request for cache result4 with AND query
The following curl request command to cache the result from the Acceptance criteria having query as "Care Quality Commission admission" and with search type as "AND":
```
where bucket='hsic-news'
curl -XPUT -H "Content-Type: text/plain" -d "1" http://<Riak_backend_IP>:<Riak_backend_PORT>/buckets/hsic-news/keys/'Care Quality Commission admission'
```

## Example Curl Request for cache result5 with AND query
The following curl request command to cache the result from the Acceptance criteria having query as "general population Alzheimer" and with search type as "AND":
```
where bucket='hsic-news'
curl -XPUT -H "Content-Type: text/plain" -d "6" http://<Riak_backend_IP>:<Riak_backend_PORT>/buckets/hsic-news/keys/'general population Alzheimer'
```

## Example Curl Request for retrieving cached result of OR query with 'Care Quality Commission'
The following curl request command to retrieve the result of the inserted data of OR query with 'Care Quality Commission':
```
where bucket='hsic-news'
curl -H "Content-Type: text/plain" http://<Riak_backend_IP>:<Riak_backend_PORT>/buckets/hsic-news/keys/'Care Quality Commission'
```

# Note: For Remaining question, I can learn new IT technology quickly, and if I get an opportunity to work, then I will perform well with all the new IT technologies.
