provider "aws" {
    region = "us-east-1"
}

resource "aws_instance" "cloud_monitor_server" {
    ami = "ami-12345678"
    instance_type = "t2.micro"

    tags = {
        Name = "CloudMonitorServer"
    }
}