# https://medium.com/better-programming/understand-blockchains-by-building-your-own-in-python-676dc38816fa
import hashlib
import json
from time import time
from uuid import uuid4

import requests
from flask import Flask, request


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.add_block(previous_hash=1, proof=100)

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        print(guess_hash)
        return guess_hash[:4] == "abcd"

    def add_block(self, proof, previous_hash=None):
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transactions = []

        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, amount):
        self.current_transactions.append(
            {
                "sender": sender,
                "recipient": recipient,
                "amount": amount,
            }
        )

        return self.last_block["index"] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]


app = Flask(__name__)
node_identifier = str(uuid4()).replace("-", "")

blockchain = Blockchain()


@app.route("/mine", methods=["GET"])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block["proof"]
    proof = blockchain.proof_of_work(last_proof)

    blockchain.add_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    previous_hash = blockchain.hash(last_block)
    block = blockchain.add_block(proof, previous_hash)

    response = {
        "message": "New Block Forged",
        "index": block["index"],
        "transactions": block["transactions"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"],
    }
    return json.dumps(response), 200


@app.route("/transactions/new", methods=["POST"])
def new_transaction():
    values = request.get_json()

    required = ["sender", "recipient", "amount"]
    if not all(k in values for k in required):
        return "Missing values", 400

    index = blockchain.add_transaction(
        values["sender"], values["recipient"], values["amount"]
    )

    response = {"message": f"Transaction will be added to Block {index}"}
    return json.dumps(response), 201


@app.route("/chain", methods=["GET"])
def full_chain():
    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain),
    }
    return json.dumps(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)