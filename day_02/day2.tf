provider "local" {
  version = "~> 2.0.0"
}

data "local_file" "foo" {
  filename = "${path.module}/data.txt"
}

locals {
  data        = split("\n", data.local_file.foo.content)
  parsed      = [for i in local.data : split(" ", replace(replace(i, ":", ""), "-", " ")) if i != ""]
  char_counts = [for i in local.parsed : [tonumber(i[0]), tonumber(i[1]), length([for j in split("", i[3]) : 1 if j == i[2]])]]
  old_policy  = length([for i in local.char_counts : 1 if i[0] <= i[2] && i[1] >= i[2]])
  new_policy  = length([for i in local.parsed : 1 if length([for j in [split("", i[3])[tonumber(i[0]) - 1] == i[2], split("", i[3])[tonumber(i[1]) - 1] == i[2]] : 1 if j]) == 1])
}

output "part_1" {
  value = local.old_policy
}
output "part_2" {
  value = local.new_policy
}
