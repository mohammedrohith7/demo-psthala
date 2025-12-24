variable "environment" {
  description = "Environment name (dev, uat, prod)"
  type        = string
  default     = "dev"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "East US"
}

variable "project_name" {
  description = "Project name prefix"
  type        = string
  default     = "genai-mlops"
}
