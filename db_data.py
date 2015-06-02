#!flask/bin/python
from app import db, models
import os
import hashlib
import seccure


models.PrivateKey.query.delete()
models.PublicKey.query.delete()



# models.PrivateKey.query.delete()
#
# pk = models.PrivateKey(
# 	name = 'Skylock-1',
#     key = 'asfafaFASFASF124qFdgbsd')
# pk2 = models.PrivateKey(
# 	name = 'Skylock-2',
# 	key = 'asfafaFASFasdaF124dasdy')
# pk3 = models.PrivateKey(
# 	name = 'Skylock-3',
# 	key = 'asfafaFASF12yasdasfghjl')
#
# db.session.add(pk)
# db.session.add(pk2)
# db.session.add(pk3)
#
db.session.commit()
