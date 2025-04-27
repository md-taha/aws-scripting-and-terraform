resource "aws_instance" "web_server" {
  ami           = "ami-0f1dcc636b69a6438" # (Example: Amazon Linux 2 AMI)
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    Name = "WebServerInstance"
  }
}

resource "aws_s3_bucket" "static_site" {
  bucket = var.bucket_name

  tags = {
    Name        = "StaticWebsiteBucket"
    Environment = "Dev"
  }
}

