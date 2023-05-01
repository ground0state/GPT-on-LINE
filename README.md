# GPT on LINE

![System](/image/system.png)

Using Chalice and AWS CDK, we will build a REST API that will serve as a webhook for LINE bot. We use AWS API Gate way, Lambda, and Dynamo DB.

## Credentials

Before you can deploy an application, be sure you have credentials configured.
Create an AWS IAM user named "chalice"　and attouch admin (or appropriate) role.
You can follow these steps to configure aws credentials:

```sh
$ mkdir ~/.aws
$ cat >> ~/.aws/config
[chalice]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
region=YOUR_REGION (such as us-west-2, us-west-1, etc)
output=json
```

## Install

Install Python3.9 and Node.js in advance. Install AWS-CDK, chalice.

```sh
npm install -g aws-cdk
pip install "chalice[cdkv2]"
```

Clone this repository. We will call the root directory of this repository `$ROOT_DIRECTORY`。

```sh
git clone https://github.com/ground0state/GPT-on-LINE.git
```

Install libraries.

```sh
cd $ROOT_DIRECTORY
pip install -r requirements.txt
```

## Environment variables

[Create your OpenAI API Key.](https://platform.openai.com/account/api-keys) Please also set up payment methods for Billing.
[Create your new Messaging API channel.](https://developers.line.biz/ja/docs/messaging-api/getting-started/#using-oa-manager)

Copy config file and edit to set your openAI API Key and LINE token.

```sh
cd runtime/.chalice
cp config_sample.json config.json
vi config.json
```

## Deploy

Deploy with the following command.

```sh
cd infrastructure
cdk bootstrap --profile chalice
cdk deploy --profile chalice
```

If you are using a virtual environment and receive the following error, deactivate the virtual environment and re-activate it.

```bahs
Traceback (most recent call last):
  File "/Users/masafumi/work/chatgpt_aws_line/infrastructure/app.py", line 3, in <module>
    from aws_cdk import core as cdk
ModuleNotFoundError: No module named 'aws_cdk'
```

After deployment is complete, the API Gateway URL will be displayed. Copy this and set it to the webhook URL of LINE Bot as `https://YOUR_ADDRESS/callback`.

## Usage

Chat with bot from your line app. "EXIT" command is special command to reset chat histories.
When you want to instruct, edit `SYSTEM_PROMPTS` in `runtime/chalicelib/chatgpt_api.py`.

## Undeploy

Uneploy with the following command. Delete your LINE channel.

```sh
cdk destroy --profile chalice
```

## Rederences

- <https://zenn.dev/zuma_lab/articles/chatgpt-line-chatbot>
