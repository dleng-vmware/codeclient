curl -X PUT "http://localhost:8091/i18n/api/v2/translation/products/CSharpClient/versions/1.0.1" -H "accept: application/json;charset=UTF-8" -H "Content-Type: application/json" -d "{ \"data\": { \"creation\": { \"operationid\": \"string\" }, \"dataOrigin\": \"string\", \"machineTranslation\": false, \"productName\": \"CSharpClient\", \"pseudo\": false, \"translation\": [ { \"component\": \"about\", \"locale\": \"zh-Hant\", \"messages\": { \"about.message\": \"test_value_change\" } } ], \"version\": \"1.0.1\" }, \"requester\": \"string\"}"