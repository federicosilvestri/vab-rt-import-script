#!/usr/bin/env bash

echo "Generating API"
openapi-python-client generate --url http://localhost:8000/api/schema/
rm -rf vab_rt_import/importing/vab_rt_api_client
mv vab_rt_import/vab-rt-api-client/vab_rt_api_client importing/
rm -rf vab-rt-api-client

echo "applying patches.."
find importing/vab_rt_api_client -name "*.py" -exec \
    sed -i "s/\.isoformat()/.strftime('%Y-%m-%d')/g" {} +