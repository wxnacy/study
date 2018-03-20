#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from app.models import db
from app.models import User


db.Model.metadata.drop_all(db.engine)
db.Model.metadata.create_all(db.engine)
users = [
    dict(name='wxnacy'),
    dict(name='win'),
    dict(name='xiao'),
    dict(name='spring'),
    dict(name='anonymous'),
]
db.session.execute(User.__table__.insert(), users)
db.session.commit()
