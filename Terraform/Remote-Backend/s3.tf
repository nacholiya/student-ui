resource "aws_s3_bucket" "remote_s3" {
  bucket = "remote_bucket_for_tfstatefile"

  tags = {
    Name        = "remote_bucket_for_tfstatefile"
  }
}