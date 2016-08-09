
from google.appengine.ext import ndb



class Vendor(ndb.Model):

    name = ndb.StringProperty()
    service_type = ndb.StringProperty()
    description = ndb.TextProperty()
    address = ndb.TextProperty()
    contact_no_1 = ndb.StringProperty()
    contact_no_2 = ndb.StringProperty()
    created_on = ndb.DateProperty(auto_now_add=True)
    created_by = ndb.StringProperty()
    updated_on = ndb.DateProperty(auto_now=True)
    updated_by= ndb.StringProperty()







