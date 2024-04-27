# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers
# MAGIC 1. raw
# MAGIC 2. processed
# MAGIC 3. lookup

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "f95fc954-6be1-4b79-9a06-11b3019982ce",
           "fs.azure.account.oauth2.client.secret": "<service-credential>",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/7e185ec6-ac86-4ef6-b3ab-f0e224a21cd6/oauth2/token"}

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://raw@andracovidreportingdl.dfs.core.windows.net/",
  mount_point = "/mnt/andracovidreportingdl/raw",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the processed container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://processed@andracovidreportingdl.dfs.core.windows.net/",
  mount_point = "/mnt/andracovidreportingdl/processed",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the lookup container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://lookup@andracovidreportingdl.dfs.core.windows.net/",
  mount_point = "/mnt/andracovidreportingdl/lookup",
  extra_configs = configs)
