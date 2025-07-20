provider "aws" {
  region = "us-west-2"
}
resource "aws_eks_cluster" "fas5" {
  name     = "fas5-eks-cluster"
  role_arn = aws_iam_role.fas5.arn
}