output "instance_public_ip" {
  description = "Public IP of EC2"
  value       = aws_instance.web_server.public_ip
}

output "s3_bucket_name" {
  description = "S3 Bucket name"
  value       = aws_s3_bucket.static_site.id
}

