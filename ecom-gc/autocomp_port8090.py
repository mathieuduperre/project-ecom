import datetime
import logging
import json
import socket
from flask import Flask, request
from google.cloud import datastore
from wsgiref.simple_server import make_server
from urlparse import parse_qs
import urlparse
import time

app = Flask(__name__)


@app.route('/')
def application (environ,start_response):

    output = []

    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    try:
        # environ['QUERY_STRING'] returns ""
        qsdata = urlparse.parse_qs( environ['QUERY_STRING'] )
        pathUrl = environ['PATH_INFO']
        if "/_ah/health" in pathUrl:
            start_response('200 OK', [('Content-Type', 'text/html')])
            return ['healthy']
    except:
        output = ["parse error"]

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print "\n------------------------------------"
    print "Request received %s" % st
    
    if 'search' in qsdata:
        valToSearch = qsdata["search"]
        print "Value to look for in datastore: %s" % valToSearch[0]
        ds = datastore.Client()        
        query = ds.query(kind='product')        
        query.add_filter('name', '>=', valToSearch[0])        
        query.projection = ['name']
        results = list(query.fetch(limit=8))
        #print "ds query result: %s" % results
        if not results:
            print "Found no result for that search string: %s" % valToSearch[0]
            output = "empty"            
        else:
            output = json.dumps(results)
            print "Results found! %s" % results
        
    else:        
        output = 'No search value requested'
        print output
    
    status = '200 OK'
    response_headers = [('Content-type','json/application; charset=utf-8'),('Access-Control-Allow-Origin','*')]    
    start_response(status,response_headers)
    print "Response sent"
    print "------------------------------------\n"
    return [output.encode("utf-8")]
 

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    try:
        httpd = make_server('', 8090, application) 
        print "Serving on port 8090"
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')
    
