# aws_lambda_img_thumbail_processing
Aws lambda function that creates an img thumbnail of an image uploaded to S3.

## Create Lambda Deployment Package
1. Create a directory and create a file named lambda_function.py in it. 
2. Now in the same directory run the following command.

    `pip install pillow -t .`
 
3. Now select and compress all the files in the directory(Not the directory itself). I named my zip file as archive(can be anything).
4. Finally upload the archive.zip to lambda from the lambda console.
