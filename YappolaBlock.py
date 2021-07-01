from tronpy import Tron,Contract
from tronpy.keys import PrivateKey
import datetime
import hashlib
import json
import os
from flask import Flask, jsonify,redirect 
from flask import Flask, jsonify,request, render_template
import re 
from urllib.parse import urlparse  
from uuid import uuid4
from flask_cors import CORS
# Part 1 - Building a Blockchain
from web3 import Web3 
from web3 import middleware
from web3.middleware import geth_poa_middleware
client1 = Tron()

class yappolaBlockchain:

	def __init__(self):
		self.chain = []
		self.transactions = []
		self.create_block(proof = 1, previous_hash = '00000') 
		self.nodes = set()



	def create_block(self, proof, previous_hash):
		import bs4
		import urllib.request
		import requests
		from urllib.request import urlopen
		from bs4 import BeautifulSoup as soup
		import random
		my_url = 'http://http://54.163.150.45/'
		#opening up connection, downloading the page
		html_page = requests.get('http://http://54.163.150.45/)
		soup = soup(html_page.content, 'html.parser')
		warning = soup.find('div', class_="image-part")
		images = warning.findAll('img')
		image = images
		image = str('http://http://54.163.150.45/'.format(image[0:]))

		mint_acct ='' #<= input acct address 
		mint_key = '' #<= input acct priv. key	
		receiver1= ''
		
		block = {'index': len(self.chain) + 1,
				 'timestamp': str(datetime.datetime.now()),
				 'proof': proof,
				 'previous_hash': previous_hash,
				 'transactions': self.transactions,
				 'Miner_Minting_Address':mint_acct, 
				   'receiver':receiver1 ,
				   'image':image,
				   'totalSupply':cntr.functions.max_yappolacoins(),
				 }
		self.transactions = []	 
		self.chain.append(block) 
		return block 

	def get_previous_block(self):
		return self.chain[-1]

	def proof_of_work(self, previous_proof):
		new_proof = 1
		check_proof = False
		while check_proof is False:
			hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
			if hash_operation[:4] == '0000':
				check_proof = True
			else:
				new_proof += 1
		return new_proof
	
	def hash(self, block):
		encoded_block = json.dumps(block, sort_keys = True).encode()
		return hashlib.sha256(encoded_block).hexdigest()
	
	def is_chain_valid(self, chain):
		previous_block = chain[0]
		block_index = 1
		while block_index < len(chain):
			block = chain[block_index]
			if block['previous_hash'] != self.hash(previous_block):
				return False
			previous_proof = previous_block['proof']
			proof = block['proof']
			hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
			if hash_operation[:4] != '0000':
				return False
			previous_block = block
			block_index += 1
		return True
	
	def add_transaction(self,sender,receiver,amount): # sender = sender receiver = receiver amount = amount
		mint_acct =''
		priv_key = PrivateKey(bytes.fromhex(""))
		# web3.eth.mint_acct = mint_acct
		receiver1= ''


		previous_block = blockchain.get_previous_block()
		previous_proof = previous_block['proof']
		proof = blockchain.proof_of_work(previous_proof)
		previous_hash = blockchain.hash(previous_block)	 
		self.transactions.append({'sender': sender,
		'receiver':receiver1,
		'amount':amount,
		'minter':mint_acct})
		previous_block = self.get_previous_block()
		return previous_block['index'] + 1 

	def add_node(self, address):
		# address = 'http:127.0.0.1:8677/'
		parsed_url = urlparse(address)
		self.nodes.add(parsed_url.netloc) 
		# node = parsed_url.															   
#Give the Chain a Reason to exist 
	def replace_chain(self): 
		network = self.nodes 
		longest_chain = None 
		max_length = len(self.chain)
		for node in network:
			response = requests.get(f'http://{node}/get_chain') 
			if response.status_code == 200:
				length = response.json()['length'] 
				chain = response.json()['chain'] 
				if length > max_length and self.is_chain_valid(chain):
					max_length = length 
					longest_chain = chain 
		if longest_chain:
			self.chain = longest_chain
			return True 
		return False 


		   





# Part 2 - Mining our Blockchain

# Creating a Web App
app = Flask(__name__)
#Creating Addresses for nodes on Port:8677
node_address = str(uuid4()).replace('-','')


# Creating a Blockchain
blockchain = yappolaBlockchain()
cors = CORS(app, resources={r"/*": {"origins": ["http://yappolacoinbase.herokuapp.com/sakujoooCloud/","http://127.0.0.1:3000/","http://localhost:8000/api/","https://ropsten.infura.io/v3/89f69d97c5c44c35959cc4d15c0f0531"," https://ropsten.etherscan.io/","http://127.0.0.1:8678/dai_gen","http://127.0.0.1:8678/yappolaDAI_minted"]}})
# cors = CORS(infura_url, resources={r"/*": {"origins": "https://ropsten.infura.io/v3/89f69d97c5c44c35959cc4d15c0f0531"}})

@app.route('/home')
def home():
	message = {}
	data = {}

	message['message'] = 'Welcome To The Official yappola Decentralized Network !'
	data['status'] = 200
	data['data'] = message

	return jsonify(data)
@app.route('/dai_gen')
def dai_gen():
	from tronpy import Tron
	from tronpy.keys import PrivateKey

	client = Tron() 
	node = client.get_node_info()
	new_cl = client.generate_address()

	warning = 'COPY/PASTE User Address / PRIVATE KEY-> Address: base58check_address, PRIVATE KEY: private_key'

	message = {}
	add = {}
	data = {}

	message['message'] = 'NODE :"{}":   New Address/Private key. Use This To get paid for image uploads. ["({})"], [{}]'.format(node,new_cl,warning)
	add['address'] = str(new_cl)
	data['status'] = 200
	data['data'] = message

	return jsonify(data)
import json
from flask import Flask, request, jsonify


# Mining a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
	client = Tron() 
	client1 = Tron(network='nile')
	amount =  1
	mint_acct =''
	priv_key = PrivateKey(bytes.fromhex(""))
	receiver1= ''
	previous_block = blockchain.get_previous_block()
	previous_proof = previous_block['proof']
	proof = blockchain.proof_of_work(previous_proof)
	previous_hash = blockchain.hash(previous_block)
	# amount =  web3.toWei(float(.0003),'ether')

	txn = (client.trx.transfer(mint_acct,receiver1, 1)
				.memo("did it work")
				.build()
				.sign(priv_key)
		)
	tx_hash = txn.txid
	# tx_hash = hash(tx_hash)+hash(tx_hash)**2
	txn.broadcast()	blockchain.add_transaction(sender = mint_acct , receiver=receiver1,amount=amount)
	block = blockchain.create_block(proof, previous_hash)
	response = {'message': 'Congratulations, you just mined a block!',
				'index': block['index'],
				'timestamp': block['timestamp'],
				'proof': block['proof'],
				'previous_hash': block['previous_hash'],
				'TRON-YPC_HASH': tx_hash,
				'transactions': block['transactions'],
				'receiver':receiver1,
				'image':block['image']} 
	message = {} 
	data = {}
	message['message'] = 'Congratulations, you just mined  block {} at {}!, \n TRON-Yappola HASH {}, Proof of work {}, previous yappola hash {}, \n transactions{}, \n RECEIVING MINTER {}'.format(block['index'],block['timestamp'],web3.toHex(tx_hash),block['proof'],block['previous_hash'],block['transactions'],receiver1) 
	data['status']= 200
   
	data['data'] = message
	data1 = pd.DataFrame(data['data'])
	return data1

# Getting the full Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
	response = {'chain': blockchain.chain,
				'length': len(blockchain.chain)}
	message = {}
	data = {}
	message['message'] = ' length {}, \n full blockchain {}'.format(len(blockchain.chain),blockchain.chain)
	data['status']= 200
   
	data['data'] = message
	return data

# Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
	is_valid = blockchain.is_chain_valid(blockchain.chain)
	message = {} 
	data = {}
	if is_valid:
		response = {'message': 'All good. The Blockchain is valid.'}
		message['message'] = 'All good,Blockchain Is Valid' 
		data['status'] = 200 
		data['data'] = message
	else:
		response = {'message': 'Houston, we have a problemo. The Blockchain is not valid.'}
		message['message'] = 'Houston, we have a problemo. The Blockchain is not valid' 
		data['status'] = 200 
		data['data'] = message   
	return jsonify(data)

### Adding yappolaChain Transactions
@app.route('/add_transaction', methods = ['POST'])
def add_transaction():
	message = {} 
	data = {}
	json = request.get_json()
	transactions_keys= ['sender','receiver','amount']
	if not all (key in json for key in transactions_keys):
		message['message'] = 'HOME ELMENTS OF THE TRASACTION ARE MISSING' 
		data['status'] =  400
		data['data'] = message   
		return jsonify(data) #'HOME ELMENTS OF THE TRASACTION ARE MISSING' 
	index = blockchain.add_transaction(json['sender'],json['receiver'],json['amount']) 
	response = {'message': f'This Transaction IS NOW ON BLOCK {index}'}
	message['message'] = 'This Transaction IS NOW ON BLOCK {}'.format(index)
	data['status'] = 201 
	data['data'] = message   
	return jsonify(response),201

### Decentralizing yappolaCoin 


###Connecting Nodes 
@app.route('/connect_node', methods = ['POST']) 
def connect_node():
	message = {} 
	data = {}   
	json = request.get_json() 
	nodes = json.get('nodes')
	if nodes is None: 
		response = {'message': f'No Nodes Found'} 

		message['message'] = 'No node connected'
		data['status'] = 400
		data['data'] = message   
		return jsonify(data)

	for node in nodes:
		blockchain.add_node(node)
	response = {'message':'THE FOLLOWING NODES ARE CONNECTED',
	'total_nodes': list(blockchain.nodes)} 
	message['message'] = 'THE FOLLOWING NODES ARE CONNECTED {}'.format(list(blockchain.nodes))
	data['status'] = 201 
	data['data'] = message   
	return jsonify(data)


### Connect longest chain if necessary
@app.route('/replace_chain', methods = ['GET'])
def replace_chain():
	is_chain_replaced = blockchain.replace_chain()
	message = {} 
	data = {}
	if is_chain_replaced:
		response = {'message': 'NODES HAD DIFFERENT CHAINS , REPLACED BY LONGEST CHAIN',
		'new_chain': blockchain.chain }
		message['message'] = 'NODES HAD DIFFERENT CHAINS , REPLACED BY LONGEST CHAIN {}'.format(blockchain.chain)
		data['status'] = 200 
		data['data'] = message
	else:
		response = {'message': 'NODE IS CONNECT TO LARGEST CHAIN',
		'actual_chain':blockchain.chain}
		message['message'] = 'NODE IS CONNECT TO LARGEST CHAIN {}'.format(blockchain.chain)
		data['status'] = 200 
		data['data'] = message   
	return jsonify(data)

from bs4 import BeautifulSoup



import requests

import urllib.request

import shutil





usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}



if __name__ == '__main__':
	app.secret_key = os.urandom(24)
	app.run(host = '127.0.0.1', debug=True,port=8676)
