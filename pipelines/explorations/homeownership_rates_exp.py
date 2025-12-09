# Databricks notebook source
# MAGIC %md
# MAGIC ### Exploratory Notebook
# MAGIC
# MAGIC Notebook for data exploration.

# COMMAND ----------

# Example: Load the Delta table using an absolute path
df = spark.table("usafacts_acs_housing_tenure_and_affordability_data_collection.population_and_society.homeownership_rates_by_area_1960_to_present_pivoted")
display(df)

# COMMAND ----------

df.head()

# COMMAND ----------

import sys

sys.path.append("/Workspace/Users/lockwood.da88@gmail.com/housing_affordability/New Pipeline 2025-12-04 22:54")

# COMMAND ----------

# !!! Before performing any data analysis, make sure to run the pipeline to materialize the sample datasets. The tables referenced in this notebook depend on that step.

display(spark.sql("SELECT * FROM workspace.default.sample_aggregation_dec_4_2254"))
