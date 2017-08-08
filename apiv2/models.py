from __future__ import unicode_literals

from django.db import models

# Create your models here.
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class tra_pings(DjangoCassandraModel):
	pin_id = columns.UUID(primary_key=True, default=uuid.uuid4)
	numa = columns.Text(index=True)
	name = columns.Text(index=True)
	lat = columns.Float()
	lon = columns.Float()
	hora = columns.Text(index=True)

class location(DjangoCassandraModel):
	name = columns.Text(primary_key=True)
	lat = columns.Float(index=True)
	lon = columns.Float(index=True)

class ping(DjangoCassandraModel):
	numa = columns.Text(primary_key=True)
	name = columns.Text()
	lat = columns.Float()
	lon = columns.Float()
	hora = columns.Text()
