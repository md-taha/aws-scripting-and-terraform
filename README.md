# AWS Scripting and Terraform Assignment - [Mohammad Taha](https://github.com/md-taha)

## Assignment Overview

This repository contains the solutions for the AWS Scripting and Terraform assignment. The tasks cover various aspects of AWS services, including EC2, S3, Lambda, and more, along with scripting in Python and automating infrastructure setup using Terraform.

---

### Task Breakdown

1. **Task 1: AWS Setup**
   - **S3 Bucket**: Created an Amazon S3 bucket for static website hosting with public access.
   - **EC2 Instance**: Launched an Amazon EC2 instance running Amazon Linux and set up a web server (Apache) to serve a simple HTML page.
   - **Security Group**: Configured the EC2 instance's security group to allow HTTP traffic from my public IP only.
   - **AWS Lambda**: Created an AWS Lambda function that triggers on S3 events (e.g., object creation) and logs the event details to CloudWatch Logs.

2. **Task 2: Scripting**
   - **Python Scripts**:
     - **s3_list_and_count.py**: Lists all S3 buckets and counts the total number of objects in a specified bucket.
     - **students_grade_analysis.py**: Analyzes a CSV file (students' names, ages, and grades) and prints the names of students with average grades above a specified threshold.

3. **Task 3: CI/CD Setup**
   - Created a GitHub repository to host the web server script and Terraform scripts.
   - Implemented a simple CI/CD pipeline using GitHub Actions for automated deployment.

4. **Task 4: Infrastructure as Code (IaC) with Terraform**
   - **Terraform Scripts**:
     - Automated the creation of an EC2 instance, S3 bucket, and Lambda function using Terraform.
     - Parameterized the Terraform scripts to accept variables like instance type, key pair, bucket name, etc.

---

### AWS Resources

- **S3 Bucket (Static Website)**: [http://taha-assignment-bucket.s3-website.ap-south-1.amazonaws.com](http://taha-assignment-bucket.s3-website.ap-south-1.amazonaws.com)
- **EC2 Web Server**: [http://13.232.170.207/](http://13.232.170.207/)

---

### GitHub Repository

You can find all the code, configurations, and documentation for this assignment in my GitHub repository:

[GitHub Repository: aws-scripting-and-terraform](https://github.com/md-taha/aws-scripting-and-terraform)

---

### File Structure

Here is the file structure of the project:

```
aws-scripting-and-terraform
├── scripts
│   ├── s3_list_and_count.py           # Python script to list S3 buckets and count objects
│   ├── students.csv                   # CSV file for student grade analysis
│   └── students_grade_analysis.py     # Python script to analyze student grades
└── terraform-project
    ├── lambda
    │   ├── lambda_function.py         # Python code for the Lambda function
    │   └── lambda_function.zip        # Zipped Lambda function for deployment
    ├── lambda.tf                      # Terraform configuration for Lambda
    ├── main.tf                        # Main Terraform configuration file
    ├── outputs.tf                     # Outputs of the Terraform setup
    ├── provider.tf                    # Terraform provider configuration
    ├── s3.tf                          # S3 bucket creation and configuration
    ├── s3_event_notification.tf       # S3 event notification for Lambda trigger
    ├── terraform.tfstate              # Terraform state file
    ├── terraform.tfstate.backup       # Backup of Terraform state file
    ├── test.txt                       # Placeholder file for testing
    └── variables.tf                   # Variables for Terraform configurations
```

---

### How to Run the Code

1. **Terraform Setup**:
   - Install [Terraform](https://www.terraform.io/downloads).
   - Navigate to the `terraform-project` directory and run:
     ```bash
     terraform init
     terraform apply -auto-approve
     ```

2. **Python Script**:
   - Install [boto3](https://boto3.amazonaws.com) and other dependencies:
     ```bash
     pip install boto3 pandas
     ```
   - To list all S3 buckets and count objects:
     ```bash
     python scripts/s3_list_and_count.py
     ```
   - To analyze the students' grades:
     ```bash
     python scripts/students_grade_analysis.py
     ```

---

### AWS Lambda Function

The AWS Lambda function is triggered on S3 events (e.g., object creation) and logs the event details to CloudWatch. It is deployed automatically via Terraform.

---

### Cost Estimation

The setup involves the following AWS resources:
- **EC2 Instance**: EC2 (t2.micro if not free): ~$96/year
- **S3 Bucket**: S3 (small static website): ~$2/year
- **Lambda**: Lambda (small usage): ~$0

---

If you have any questions or need further information, feel free to reach out!

Best regards,  
**Mohammad Taha**  
[GitHub](https://github.com/md-taha)  
[LinkedIn](https://www.linkedin.com/in/md--taha/)  

