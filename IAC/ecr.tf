module "ecr_fargate" {
  source = "git::https://github.com/Zillions-Trading-Bots/example_python_flask.git//modules/ecr"

  aws_region = var.aws_region
  ecr_values = var.ecr_values
  tags       = var.tags
}
