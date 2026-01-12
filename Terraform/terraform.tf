terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "6.0.0"
    }
  }
  backend "s3" {
    bucket = "remote_bucket_for_tfstatefile"
    key = "terraform.tfstate"
    region = "eu-north-1"
    dynamodb_table = "remote_state_table"
  }
}