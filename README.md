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
3. **Data Extraction:** Lambda pulls the PDF into ephemeral storage (`/tmp`), reads the raw document
