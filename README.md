# Serverless Resume Parser API

An enterprise-grade, serverless application designed to parse and extract structured data from resumes. Built with Python and deployed on AWS Lambda, this project utilizes Terraform for robust Infrastructure as Code (IaC) and integrates automated DevSecOps pipelines for continuous security and code quality checks.

## 🏗 Architecture & Tech Stack
* **Compute:** AWS Lambda (Serverless)
* **Infrastructure as Code (IaC):** Terraform (HCL)
* **Runtime:** Python 3.x
* **CI/CD & DevSecOps:** GitHub Actions (Bandit, Checkov)

## ✨ Key Features
* **Scalable Execution:** Leverages AWS Lambda for on-demand, cost-effective processing without the overhead of server management.
* **Immutable Infrastructure:** The entire AWS environment is provisioned, managed, and version-controlled declaratively via Terraform.
* **Automated Security Scanning:** The CI/CD pipeline enforces secure coding principles by scanning for Python vulnerabilities (Bandit) and infrastructure misconfigurations (Checkov) on every commit.
* **Modular Design:** Strict separation of concerns between compute logic (`/lambda`), infrastructure provisioning (`/terraform`), and testing (`/tests`).

## 📁 Repository Structure
* `/lambda` - Python source code for the serverless parsing function.
* `/terraform` - Terraform configurations and state management for AWS deployment.
* `/tests` - Unit tests for parsing logic validation.
* `.github/workflows` - CI/CD pipeline definitions for automated testing and security audits.

## 🚀 Deployment
Infrastructure is deployed via Terraform. Ensure AWS CLI is configured with the appropriate IAM permissions before initializing the backend.

```bash
cd terraform
terraform init
terraform plan
terraform apply
