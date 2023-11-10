provider "aws" {
  region = "eu-north-1" # Change this to your desired AWS region
  access_key="AKIA367S7HZ5YGLBFNC2"
  secret_key="T6Xjp/OGUJTnj3WgRzic5hInb3KpuvyYYiR3XW7T"
}

resource "aws_instance" "example" {
  ami           = "ami-0fe8bec493a81c7da" # Ubuntu 20.04 LTS AMI ID
  instance_type = "t3.micro" # Change instance type as needed
  key_name      = "mahesh1" # Change to your EC2 key pair name
  subnet_id     = "subnet-03cbf7b1e6ab66758" # Change to your subnet ID
#  security_groups=["launch-wizard-1"] # Change to your security group name

  tags = {
    Name = "Ubuntu-Instances"
  }
}

output "public_ip" {
   value = aws_instance.example.public_ip
}
