variable "aws_region" {
  type        = string
  default     = "us-east-1"
  description = "AWS region"
}

variable "ecr_values" {
  type = any
  default = {
    repository_name = "example_python_flask"
  }
  description = "AWS ECR configuration"
}

variable "vpc" {
  type        = any
  default     = {}
  description = "AWS VPC configuration"
}

