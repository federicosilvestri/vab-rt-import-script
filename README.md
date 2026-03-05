# VAB DB Analysis

The current db sucks, but it can be a nice preprocessing exercise for data mining course :) 



## VAB - RT import
Tu update client you can run:

```shell
openapi-python-client generate --url http://localhost:8000/api/schema/

rm -rf importing/vab_rt_api_client
mv vab-rt-api-client/vab_rt_api_client importing/
rm -rf vab-rt-api-client
```
and then move the content of vab-rt-api-client outside of directory. Then, you can delete the directory. 

### Initial data

In order to run import, you have to collect initial data:

```shell
cd importing
python fetch_initial.py
```


### OpenAPI Patches

File members.py, Member class:

```python
birth_date = self.birth_date.strftime('%Y-%m-%d')
```


### Authentication

Go to [Api token obtain page](http://localhost:8000/api/docs/#/auth/auth_create), copy json response and paste it
into `auth.json` file.