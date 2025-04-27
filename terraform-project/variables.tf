variable "aws_region" {
  description = "AWS region"
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "Type of EC2 instance"
  default     = "t2.micro"
}

variable "key_name" {
  description = "Name of the SSH key pair"
}

variable "bucket_name" {
  description = "Name of the S3 bucket"
}

variable "lambda_zip_path" {
  description = "Path of lambda_function.zip file"
  type        = string
  default     = ""
}

