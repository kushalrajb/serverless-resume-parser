# Serverless Resume Parser & DevSecOps Pipeline

An event-driven, fully automated serverless application deployed on AWS. This project solves the bottleneck of processing unstructured resume data by utilizing Python and AWS Lambda to automatically parse PDF uploads, extract key candidate entities, and persist structured data into DynamoDB.

This repository demonstrates modern cloud engineering practices, featuring complete Infrastructure as Code (IaC) via Terraform and a robust, automated DevSecOps CI/CD pipeline using GitHub Actions.

---

## 🏗️ Repository Architecture

* 📁 **serverless-resume-parser/**
  * 📁 **.github/workflows/**
    * 📄 `devsecops.yml` — Automated CI/CD pipeline (Test, Scan, Deploy)
  * 📁 **lambda/**
    * 📄 `parser.py` — Core Python serverless compute logic utilizing `PyPDF2`
  * 📁 **terraform/**
    * 📄 `main.tf` — Complete AWS resource declarations (S3, DynamoDB, Lambda, API Gateway)
    * 📄 `.checkov.yaml` — Security scanner configuration
  * 📁 **tests/**
    * 📄 `test_parser.py` — Unit tests for data extraction logic (TDD)
  * 📄 `.gitignore` — Security rules preventing local state and credential leakage
  * 📄 `README.md` — Project documentation

---

## 🚀 System Architecture & Workflow

1. **Event Trigger:** A user/system uploads a PDF resume to the designated Amazon S3 bucket.
2. **Serverless Compute:** S3 triggers an event notification, instantly waking up the AWS Lambda function.
3. **Data Extraction:** Lambda pulls the PDF into ephemeral storage (`/tmp`), reads the raw document text, and utilizes Regex to extract specific target data (e.g., Candidate Email).
4. **Data Persistence:** The unstructured text is converted into clean JSON and stored inside an Amazon DynamoDB NoSQL table for downstream querying.

---

## 🛡️ DevSecOps & CI/CD Pipeline

Every push to the `main` branch triggers a strict GitHub Actions workflow designed to enforce enterprise security and code quality before deployment:

* **Stage 1: Security Scanning** * Executes **Bandit** to scan the Python Lambda code for vulnerabilities.
  * Executes **Checkov** to analyze the Terraform IaC for cloud misconfigurations.
* **Stage 2: Unit Testing**
  * Runs standard `unittest` suites to ensure text-extraction algorithms work perfectly.
* **Stage 3: Automated OIDC Deployment**
  * Securely authenticates with AWS via **OpenID Connect (OIDC)**—meaning no static, long-lived AWS Access Keys are stored in GitHub Secrets.
  * Packages the Lambda function with its `PyPDF2` dependencies.
  * Executes `terraform apply` to dynamically update infrastructure and push the new code.

---

## 🛠️ Technology Stack

* **Cloud Provider:** Amazon Web Services (AWS)
* **Compute & API:** AWS Lambda, API Gateway
* **Storage & Database:** Amazon S3, Amazon DynamoDB
* **Infrastructure as Code (IaC):** Terraform
* **CI/CD & Automation:** GitHub Actions
* **Languages:** Python 3.12 (boto3, PyPDF2), HashiCorp Configuration Language (HCL)
* **Security & Testing:** Bandit, Checkov, `unittest`

---

## ⚙️ How to Deploy & Run

### Step 1: Clone the Repository
```bash
git clone [https://github.com/kushalrajb/serverless-resume-parser.git](https://github.com/kushalrajb/serverless-resume-parser.git)
cd serverless-resume-parser
```

### Step 2: Provision the Infrastructure (Local Manual Deploy)
*Note: If you have OIDC configured, simply pushing to the `main` branch will deploy this automatically via GitHub Actions.*
To deploy manually from your local machine:
```bash
# Navigate to the terraform directory
cd terraform

# Initialize providers
terraform init

# Review and apply the infrastructure blueprint
terraform apply -auto-approve
```

### Step 3: Trigger the Serverless Pipeline
Because this is an event-driven architecture, the application runs automatically when a file is uploaded. You can trigger it using the AWS CLI:
```bash
# Upload a sample PDF to your newly created S3 bucket
aws s3 cp sample_resume.pdf s3://resume-parser-uploads-dev-portfolio/
```

### Step 4: Verify the Results
Once the file hits the bucket, Lambda will execute in milliseconds. You can verify the extracted data in DynamoDB:
```bash
# Scan the DynamoDB table to see the parsed JSON output
aws dynamodb scan --table-name ParsedResumes
```

### Local Testing
To run the Python unit tests locally without deploying to AWS:
```bash
python3 -m unittest tests/test_parser.py
```
