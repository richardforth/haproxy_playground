from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.programming.language import Python

## Graph Attributes
graph_attr = { 
    "layout":"osage", 
    "ratio":"expand", 
    "size":"5", 
    "rankdir":"LR" 
    }

## Visor Commmerce Sources and Replicas Diagran
with Diagram("HAProxy Playground Layout", show=False): 

    ### Define Load Balancer 
    with Cluster("HAProxy Loadbalancer"): 
        lb1 = Server("(HAproxy) \n \
127.0.0.1:80") 

             
    ### Define BACKEND REPLICAS 
    with Cluster("(Back Ends)"): 
        with Cluster("Web01"): 
            web1 = Python("(Python Script) \n \
Python Flask\n \
127.0.0.1:5001")
        with Cluster("Web02"): 
            web2 = Python("(Python Script) \n \
Python Flask\n \
127.0.0.1:5002") 
        with Cluster("Web03"): 
            web3 = Python("(Python Script) \n \
Python Flask\n \
127.0.0.1:5003")
        with Cluster("Web04\nwibble.com/foo"): 
            web4 = Python("(Python Script) \n \
Python Flask\n \
127.0.0.1:5004")
            with Cluster("Additional Function"):
                func = Python("""@app.route(\"/foo\")
def foo\(\):
\treturn \"bar\"""")
 
     
    ### TOPOLOGY AND ENTITY LINKS 
    lb1 >> [web1,web2,web3,web4]
    web4 >> func
