terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
  # GitLab Managed Terraform State
  backend "http" {}
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "rg-${var.project_name}-${var.environment}"
  location = var.location
}

# Azure AI Services (OpenAI)
resource "azurerm_cognitive_account" "openai" {
  name                = "oai-${var.project_name}-${var.environment}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  kind                = "OpenAI"
  sku_name            = "S0"
  
  custom_subdomain_name = "oai-${var.project_name}-${var.environment}"
}

# Azure AI Search (VectorDB)
resource "azurerm_search_service" "search" {
  name                = "search-${var.project_name}-${var.environment}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "standard"
}

# Azure API Management
resource "azurerm_api_management" "apim" {
  name                = "apim-${var.project_name}-${var.environment}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  publisher_name      = "Admin"
  publisher_email     = "admin@contoso.com"
  sku_name            = "Developer_1"
}

# Storage Account
resource "azurerm_storage_account" "storage" {
  name                     = replace("st${var.project_name}${var.environment}", "-", "")
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
