from flask import Flask, jsonify
from flask import make_response
from flask.ext.sqlalchemy import SQLAlchemy
import os
import hashlib
import seccure

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Returns all private keys
@app.route('/skylock/api/private/keys', methods=['GET'])
def get_private_keys():
    keys = models.PrivateKey.query.all()
    return jsonify(Private_Keys=[i.serialize for i in keys])

# Returns all public keys
@app.route('/skylock/api/public/keys', methods=['GET'])
def get_public_keys():
    keys = models.PublicKey.query.all()
    return jsonify(Public_Keys=[i.serialize for i in keys])

# Generates a new public and private key
# Displays the new public key
@app.route('/skylock/api/key', methods=['POST'])
def create_key():
    # Get the latest id
    latestPKs = models.PrivateKey.query.all()
    priv_id = -1
    for priv in reversed(latestPKs):
        priv_id = priv.id + 1
        break
    if(priv_id == -1):
        priv_id = 1
    # Create private key
    randomStr = os.urandom(64)
    h = hashlib.sha256()
    h.update(randomStr)
    privKey = h.hexdigest()
    publicKey = seccure.passphrase_to_pubkey(privKey)
    # Save private key
    pk = models.PrivateKey(
        name = 'SKYLOCK-' + str(priv_id),
        key = str(privKey))
    db.session.add(pk)
    db.session.commit()
    # Save public key
    pubk = models.PublicKey(
        id = priv_id,
        name = 'SKYLOCK-' + str(priv_id),
        key = str(publicKey)
    )
    db.session.add(pubk)
    db.session.commit()
    # Display new public key
    pubKeyRes = models.PublicKey.query.get(priv_id)
    return jsonify(Public_key=[pubKeyRes.serialize])

from app import models
