# SAPP Rates Telegram Dashboard

```bash
// Checkout whats needed in the .env file from the file docker-compose.yml, and app/config.py
touch .env
docker compose -f "docker-compose.yml" up -d --build
```

## About Me

Hello (здравствуйте), my name is Mike Z, a 22 y.o Python, TypeScript, Golang programmer based in St Petersburg Europe.
Going straight to the point, shouting at the top of my voice, furiously punching my keyboard: *I AM LOOKING FOR A DECENT JOB AS A JUNIOR OR MID LEVEL SOFTWARE ENGINEER <malito:mzinyoni7@outlook.com>*.
Back to calm, I am a self taught developer but I did go to Software Engineering University as well. I have 7+ years of computer programming experience and four of them being proffessional work experience. I have written software that processed millions of dollars *i.e I am not a millionnaire, I was paid slightly less than 10k*.
I am fluent in English and decent in Russian.

![System Overview](https://github.com/mikietechie/gocurrenciesapi/blob/main/files/architecture.jpg)

## Introduction

A Python Telegram Client app for a Fintech API which I wrote in Golang. This is a frontend service where my users can manage how they use our service. In Russia where I live Telegram is very popular, so instead of using React for the client dashboard I decided to use Telegram. A lot of organizations here use Telegram for managing their business processes like recruitment, placing orders, registrations and error logging.

My motivation for making this API is to prove how well I understand Python development, how much I know about APIs, Security, Caching, Optimazation and Documentation. I also wish to present it as a portfolio project since I am trying to move from being a fullstack Python JavaScript developer to a "Real" Golang, Python backend developer who is worth paying thousands of dollars.

## Technologies Used

Programming language: Python
Python is a general purpose, interpreted, dynamically typed programming language. I chose Python because I am well versed in working with Python, Python has a lot of libraries i.e. it has a library for everything you can think of. It is also famously used in making scripts, bots and automations. Where I work we use Python Telegram bots for error logging and CI/CD. And yes, Python does support typing, and I use typing because I am a nerd.

Frameworks: AioHTTP & Pydantic
AIOHTTP is an asyncronous Python http framework. It has a client and server module. One of the most trending web frameworks Fast API is built on top of Aiohttp and Pydantic. Pydantic is a Python typing library.

Caching: Redis
Redis is an open source cache software. Redis stores data in key value pairs. You can read and write data to Redis way faster than you would to MongoDB or Postgres. Redis will give your server massive perfomance gains. I chose Redis because it is easy to setup and manage.

Data Source: SAPP Finance API
SAPP Finance is a Golang powered fintech data API. Check it out here:
<https://github.com/mikietechie/gocurrenciesapi>

Authentication: Sessions
In this project I implement sessions using the Telegram user details.

## Architecture

The system has 3 data models User, Client and Rate.

![System Architecture](https://github.com/mikietechie/gocurrenciesapi/blob/main/files/architecture.jpg)

![An Image of the API Documentation](https://github.com/mikietechie/gocurrenciesapi/blob/main/files/swagger.png)

![An Image of the database schema](https://github.com/mikietechie/gocurrenciesapi/blob/main/files/schema.png)

## Workflow

Using Telegram, search for the telegram bot name. => Click start. => Register or login. => Create Client. => Get your client API KEY => Check your client status => Update your password => Make payments for your clients.

## Options for future development

1. Add Unit tests (Help me please, I do not know how I will have to test this asyncronous code with a lot of dependancy on external services)
2. Improve the design
3. Inculcate scalability.

## Scalability Plan

Ok here is the point, I do know how to use AWS, unfortunately I do not have certificates to prove my claim. A few years ago I devoted three months of my teenage life to learning Docker, Git and AWS. I wished to get an AWS certificate but I did not have the money, maybe I could have passed even upto cloud architect. On another note I am glad I didn't because the certificate would have expired by now.

Instead of runnig all my services from one `docker-compose.yml` file, I will have to use an infinitely scalable Redis redis and infinitely scalable virtual machine service provided by a good cloud service provider. (Yandex Cloud, VK Cloud, AWS, Google Cloud, Alibaba, Microsoft Azure e.t.c). Truth be told we all hate these giant tech companies but we can't do without them. (Thanks to Microsoft Github, Vs Code, Google Go, Yandex, Sberbank and Ubuntu) I was able to create this project.

Once I do this, I will lose a lot of money to these big tech companies, and I will introduce a lot of complexity to my innocent app, I might even have to end up hiring a Devops Engineer, and an Accountant to handle my Cloud Service invoices and taxes. I will go broke, then they will look for me, find me and ask to sell my properties, unfortunately I do not own any properties except for my precious laptop Lenovo 7th Gen, 16Gb Ram, 1Tb SSD (It's a beast. I got it as a gift from my former boss), then they will find my dad who still has custody over me and sell his mansion located in a porche surbub in Southern Africa where I come from.

## Challenges faced

1. Structuring the code. Unlike Django or Angular.
2. Lack of time, I did not have enough time per day to dedicate to this project. I work 8 hours a day as a Python Backend Developer. (I work on peripheral services only, because I cannot understand properly the language used in my city of residance)
3. *I had no one to give me feedback as I was developing this system. I have 4 years of experience in developing production grade Python JavaScript software, but I have always worked under the watch of an alpha male, a senior software engineer, a 10x developer, a seasoned developer. Truth be told the people who hold these titles have invaluable experience, they know everything, they have seen everything.*
4. Module naming
5. Variable naming

## Conclusion

The name is Mike, Mike Z.
