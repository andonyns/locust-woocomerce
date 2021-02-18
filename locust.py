import time
import json
from locust import HttpUser, task, between
from locust.contrib.fasthttp import FastHttpUser

class WebsiteUser(FastHttpUser):
    wait_time = between(1, 5)
    
    @task
    def index_page(self):
        self.client.get(path="/")

class AddProduct(FastHttpUser):
    userInfo = {}
    wait_time = between(1, 5)
    
    def on_start(self):
    	with open("./user.json") as f:
    	    global userInfo
    	    userInfo = json.load(f)
    	    
    	self.client.post(path="login", json={"username": userInfo['username'], "password": userInfo['password']})

    @task
    def index(self):
        with open("./order.json") as o:
    	    orderData = json.load(o)
    	    
        self.client.request(method="POST", path="wp-json/wc/v3/orders", name="order",auth=(userInfo['username'], userInfo['password']), json = orderData)
        self.client.request(method="GET", path="my-account/cart", name="cart")

