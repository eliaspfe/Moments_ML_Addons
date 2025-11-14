# Moments_ML_Addons

## Description

This project is based on the moments application from Github. [Moments](https://github.com/greyli/moments) got updated with 3 machine learning based features:

- Alternative text generation
- Image search based on AI-generated tags
- Comment translation from english to german

## Obtaining an API-KEY

1. Go to [HuggingFace](https://huggingface.co)-Website
2. Create Account
3. When logged in -> Click onto the profile picture (top right corner)
4. In the dropdown menu -> Click onto Access tokens or follow the Link: [AccessTokens](https://huggingface.co/settings/tokens)
5. Click the Create button in the top right corner
6. Choose Write and give your Token a name
7. Copy your token and paste it into the Dockerfile behind `HF_API_KEY`

## Setup

1. Build the Docker Image: `docker image build -t moments .`
2. - Windows: `docker container run -p 5000:5000 moments`
   - Mac (Port 5000 is used by Airplay): `docker container run -p 5001:5000 moments`
3. Open [Windows](http://localhost:5000) or [Mac](http://localhost:5001) in Browser

## Example Login Data

- email: `admin@helloflask.com`
- password: `moments`
