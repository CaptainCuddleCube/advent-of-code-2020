provider "local" {
  version = "~> 2.0.0"
}

data "local_file" "foo" {
  filename = "${path.module}/data.txt"
}

locals {
  data       = split("\n", data.local_file.foo.content)
  int_data   = [for s in local.data : tonumber(s) if s != ""]
  list_1     = [for i1 in local.int_data : i1 if contains(local.int_data, 2020 - i1)]
  int_data_2 = [for i in local.int_data : [for j in local.int_data : [i, j]]]
  list_2     = tolist(toset(flatten([for i in local.int_data_2 : [for j in i : j if contains(local.int_data, 2020 - j[0] - j[1])]])))
}

output "answer_1" {
  value = local.list_1[0] * local.list_1[1]
}
output "answer_2" {
  value = local.list_2[0] * local.list_2[1] * local.list_2[2]
}
