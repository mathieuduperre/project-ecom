# project-ecom

Autocomplete project.  Application running in a container serving web request for autocomplete search. Db is an extract of bestbuy datastore. Served as a demo to demonstrate microservice. The application runs in public cloud as an "app" too, and can scale based on traffic/usage. Response latency is in ms, data is stored in a nosql db.  PoC. 

Repo includes a tool to extract content from bestbuy csv db and inject in nosql db, includes the software (python) along with a tool to load test the server. Lastly, it includes a proof of concept webpage that can be run in another cloud to show multi-region serving.
