provider "aws" {
  region = "us-west-2"
}
resource "aws_eks_cluster" "fas5-eks" {
  name     = "fas5-eks-cluster"
  role_arn = aws_iam_role.fas5-eks.arn
  depends_on = [aws_iam_role_policy_attachment.fas5-eks-AmazonEKSClusterPolicy]
}