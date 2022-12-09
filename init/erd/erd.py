from sqlalchemy import MetaData
from sqlalchemy_schemadisplay import create_schema_graph, create_uml_graph
from sqlalchemy.orm import class_mapper
import os
from datetime import datetime

import models
from models import *

try:
    os.remove("app.db")
except:
    pass

Base.metadata.create_all(engine)

date = str(datetime.now())
date = date.split(".")[0].split(" ")
date = "".join([date[0], "_", date[1]])

# create the pydot graph object by autoloading all tables via a bound metadata object
graph = create_schema_graph(metadata=MetaData(database_url),
    show_datatypes=True,
    show_indexes=True,
    rankdir='LR', # From left to right (instead of top to bottom)
    concentrate=True # join the relation lines together?
)
graph.write_png(f'generated-ERD/dbschema_{date}.png') # write out the file

# lets find all the mappers in our model
mappers = []
for attr in dir(models):
    if attr[0] == '_': continue
    try:
        cls = getattr(models, attr)
        mappers.append(class_mapper(cls))
    except Exception:
        pass

# pass them to the function and set some formatting options
graph = create_uml_graph(mappers,
    show_operations=True,
    show_multiplicity_one=True
)
graph.write_png(f'generated-ERD/schema_{date}.png') # write out the file
