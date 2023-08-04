# Databricks notebook source

print("welcome")


# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select "Welcome Simua"

# COMMAND ----------

username=dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()

# COMMAND ----------

print(username)

# COMMAND ----------

dbutils.notebook.entry_point.getDbutils().notebook().getContext()

# COMMAND ----------

import json

# parse x:
y = dbutils.notebook.entry_point.getDbutils().notebook().getContext().toJson() 
res = json.loads(y)
#print(res)
display(res)

# COMMAND ----------

print(res['extraContext']['notebook_path'])

# COMMAND ----------

display(dbutils.fs.ls("/databricks-datasets/"))

# COMMAND ----------


