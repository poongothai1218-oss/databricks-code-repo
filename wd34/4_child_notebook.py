# Databricks notebook source
# MAGIC %md
# MAGIC #Creating this child notebook for the demo of calling child notebook from the parent notebook

# COMMAND ----------

# MAGIC %sql
# MAGIC select current_timestamp()

# COMMAND ----------

#dbutils.notebook.exit(0)

# COMMAND ----------

dbutils.widgets.text("table_name", "cust")

# COMMAND ----------

text_box_value=dbutils.widgets.get("table_name")
print(text_box_value)

# COMMAND ----------

dbutils.notebook.exit("notebook completed successfully")
