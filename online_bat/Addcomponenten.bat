curl -X PUT "http://localhost:8091/i18n/api/v2/translation/products/PythonClient/versions/5.0.0" -H "accept: application/json;charset=UTF-8" -H "Content-Type: application/json" -d "{ \"data\": { \"creation\": { \"operationid\": \"string\" }, \"dataOrigin\": \"string\", \"machineTranslation\": false, \"productName\": \"PythonClient\", \"pseudo\": false, \"translation\": [ { \"component\": \"addcomponent\", \"locale\": \"en\", \"messages\": { \"about.message\": \"test_en_change123\" } } ], \"version\": \"5.0.0\" }, \"requester\": \"string\"}"