provider "aws" {
    region = "us-east-1"
}
resource "aws_iam_user" "ses_user" {
    name = "ses-monitoring-user"
}
resource "aws_iam_user_policy" "ses_user_policy" {
    name = "ses-monitoring-user-policy"
    user = aws_iam_user.ses_user.name
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Effect = "Allow"
                Action = [
                    "ses:SendEmail",
                    "ses:SendRawEmail"
                ]
                Resource = "*"
            }
        ]
    })
}
resource "aws_iam_access_key" "ses_user_key" {
    user = aws_iam_user.ses_user.name
}
output "smtp_username" {
    value = aws_iam_user.ses_user.name
}
output "smtp_password" {
    value = aws_iam_access_key.ses_user_key.secret
    sensitive = true
}