# Default USGS pangeo-forge bakery
region = "us-west-2"

cluster_name = "pangeo-forge-usgs"

aws_tags = {
  "wma:project_id"     = "hytest"
  "wma:application_id" = "pangeo_forge_runner"
  "wma:contact"        = "thodson@usgs.gov"
}

aws_vpc = {
  default = false
  id = "vpc-0af42fd592a1efc5b"
}

permissions_boundary = "arn:aws:iam::807615458658:policy/csr-Developer-Permissions-Boundary"

prometheus_hostname = "prometheus.us-west-2.aws.bakeries.pangeo-forge-usgs.omgwtf.in"

buckets = ["pangeo-forge-usgs-runner"]