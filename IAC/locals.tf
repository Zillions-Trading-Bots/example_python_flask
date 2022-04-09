locals {
  region = var.aws_region

  ecr_defaults = {
    repository_name = ""
  }
  ecr = merge(local.ecr_defaults, var.ecr_values)

  vpc_defaults = {
    id = ""
  }
  vpc             = merge(local.vpc_defaults, var.vpc)
  use_default_vpc = local.vpc.id == ""

}
