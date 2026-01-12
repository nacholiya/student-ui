#CREATE KEYPAIR FOR EC2 INSTANCE

resource "aws_key_pair" "student-ui-key"{
    key_name = "student-ui-key"
    public_key = file("student-ui-key.pub")
}

#CREATING DEFAULT VPC FOR EC2 INSTANCE

resource "aws_default_vpc" "default" {
}

#CREATING SECURITY GROUP FOR EC2 INSTANCE

resource "aws_security_group" "student-ui-sg" {
  name = "student-ui-sg"
  vpc_id = aws_default_vpc.default.id #INTERPOLATION

  #INBOUND RULES

  ingress  {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "ssh-open"
  }
  ingress {
    from_port = 5000
    to_port = 5000
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Frontend"
  }
  ingress {
    from_port = 5001
    to_port = 5001
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Backend"
  }

  #OUTBOUND RULES

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "all ports open"
  }

  tags = {
    Name = "student-ui-sg"
  }
}

#CREATE EC2 INSTANCE

resource "aws_instance" "student-ui-ec2-instance" {
  ami = "ami-042b4708b1d05f512" #UBUNTU
  instance_type = "t3.micro"
  key_name = aws_key_pair.student-ui-key.key_name
  security_groups = [aws_security_group.student-ui-sg.name]
  user_data = file("user_data.sh")

  root_block_device {
    volume_size = 30
    volume_type = "gp3"
  }
  tags = {
    Name = "student-ui-ec2-instance"
  }
 }