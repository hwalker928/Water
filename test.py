import water
water.init()
from water import Flow

#Flow.Databases.create("testing")
#Flow.Tables.create("testing","test")

Flow.Drops.set("Test","True","testing","test")
Flow.Drops.get("Test","testing","test")
#water.Flow.Databases.ls_tables("testing")
