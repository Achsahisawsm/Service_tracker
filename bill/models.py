from google.appengine.ext import ndb
from vendors.models import Vendor

BILL_STATUS_CHOICES = {0: 'Created', 1: 'partialy_paid',
                       2: 'Paid'}


class Bill(ndb.Model):

    vendor = ndb.KeyProperty(kind='Vendor')
    bill_date = ndb.DateProperty()
    amount = ndb.FloatProperty()
    due_date = ndb.DateProperty()
    line_items = ndb.JsonProperty()
    company = ndb.StringProperty()
    branch = ndb.StringProperty()
    status = ndb.IntegerProperty(choices=BILL_STATUS_CHOICES.keys())
    date_of_payment = ndb.DateProperty()
    notes = ndb.TextProperty()

    created_by = ndb.StringProperty()
    created_on = ndb.DateProperty(auto_now_add=True)
    updated_by = ndb.StringProperty()
    updated_on = ndb.DateProperty(auto_now=True)
