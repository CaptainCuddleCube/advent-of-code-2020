provider "local" {}

data "local_file" "foo" {
  filename = "${path.module}/data.txt"
}

locals {
  data       = split("\n\n", trim(data.local_file.foo.content, "\n"))
  split      = [for s in local.data : [for i in split("\n", s) : toset(split("", i))]]
  p1_reducer = sum([for s in local.split : length(setunion(s...))])
  p2_reducer = sum([for s in local.split : length(setintersection(s...))])
}

output "part_1" {
  value = local.p1_reducer
}

output "part_2" {
  value = local.p2_reducer
}
