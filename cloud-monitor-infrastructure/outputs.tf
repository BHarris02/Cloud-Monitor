output "instance_ip" {
    description = "Public IP of instance"
    value = aws_instance.cloud-monitor.public_ip
}