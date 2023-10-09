aws_lambda.py - Here .py file is added in which i have passed the ssm parameter ('external-api-url') .Also I have created an IAM Role named "my_para_lambda-role-thgt4fds".Below attaching the screenshots for better understanding. Also adding screen of output too.
Lambda function:
![image](https://github.com/yuvatimankar/aws_lambda_fxn/assets/72244797/5109ac45-a9bd-47c6-8b05-c42a21e1249c)
![image](https://github.com/yuvatimankar/aws_lambda_fxn/assets/72244797/2aa8c991-6831-41cf-a67a-f987ec771228)
output
![image](https://github.com/yuvatimankar/aws_lambda_fxn/assets/72244797/facd878f-a9f0-4c4a-a75d-ff79444dc8e2)
ssm parameter:
![image](https://github.com/yuvatimankar/aws_lambda_fxn/assets/72244797/0663c39f-76a1-4280-afad-158c70eb7c5f)

Now I have created an cloudformation stack named " MyStack" in which i have uploaded aws_lambda.yaml file which i have uploaded already below will give the screenshots for better understanding.
![image](https://github.com/yuvatimankar/aws_lambda_fxn/assets/72244797/673ed3d4-e603-4d7e-8d5d-dedee9cbe2b4)
Then I have used codecommit for creating repo named "MyRepo". 
![image](https://github.com/yuvatimankar/aws_lambda_fxn/assets/72244797/9856a4ee-d4d6-4e98-ab36-f274e5453a9b)
Then I have deployed it in codepipeline
![image](https://github.com/yuvatimankar/aws_lambda_fxn/assets/72244797/dc56c7fd-d11d-4761-bfd5-0a92e80f525d)
![image](https://github.com/yuvatimankar/aws_lambda_fxn/assets/72244797/629cfb49-8363-4386-ba72-4ef0d3251b8a)
![image](https://github.com/yuvatimankar/aws_lambda_fxn/assets/72244797/7c3ccee0-e82a-478f-8753-c16091f893ad)
Error which i am getting
![image](https://github.com/yuvatimankar/aws_lambda_fxn/assets/72244797/b9acdf07-2436-4291-ac39-f4b9588ad72f)



