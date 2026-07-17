output "instance_public_ip" {
  value = aws_instance.ops_pilot.public_ip
}

output "instance_public_dns" {
  value = aws_instance.ops_pilot.public_dns
}

output "instance_id" {
  value = aws_instance.ops_pilot.id
}