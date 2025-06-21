#!/bin/bash

# -----------------------
# SIMPLE STATIC SITE DEPLOYMENT TO AZURE
# -----------------------

# 📌 Step 1: Set these before running
RESOURCE_GROUP="myCapstoneProject"
STORAGE_NAME="mystatic10313"
SOURCE_FOLDER="."  # This folder must contain index.html

# ✅ Step 2: Login to Azure if not already logged in
echo "🔐 Logging into Azure..."
az account show > /dev/null 2>&1
if [ $? -ne 0 ]; then
  az login
fi

# 🌍 Step 3: Turn on static website hosting
echo "🚀 Enabling static website hosting..."
az storage blob service-properties update \
  --account-name $STORAGE_NAME \
  --resource-group $RESOURCE_GROUP \
  --static-website \
  --index-document index.html \
  --404-document 404.html

# 🔑 Step 4: Get your storage key
echo "🔑 Getting access key..."
STORAGE_KEY=$(az storage account keys list \
  --account-name $STORAGE_NAME \
  --resource-group $RESOURCE_GROUP \
  --query "[0].value" -o tsv)

# 📤 Step 5: Upload website files
echo "📤 Uploading files from $SOURCE_FOLDER..."
az storage blob upload-batch \
  --account-name $STORAGE_NAME \
  --destination '$web' \
  --source $SOURCE_FOLDER \
  --account-key $STORAGE_KEY

# 🌐 Step 6: Show the website URL
echo "✅ DONE! Your website is live at:"
az storage account show \
  --name $STORAGE_NAME \
  --resource-group $RESOURCE_GROUP \
  --query "primaryEndpoints.web" \
  -o tsv
 why