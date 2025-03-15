# Google Meet Bot

An advance level [Google Meet](https://support.google.com/meet/?hl=en#topic=14074839) bot which can attend meetings on your desktop just by sending a link via phone through its web app. It will leave the meeting when there are an insufficient amount of students in a lecture. Also, it record the meetings while in them and prevents you from leaving by reconnecting.

## Setup

### Setup with Docker & Docker-compose

1. Make sure you have [Docker](https://docs.docker.com/get-docker/) and [Docker-Compose](https://docs.docker.com/compose/install/) installed.

    ```shell script
    docker --version
    docker-compose --version
    ```

2. Bring up the docker container in the background
    
    ```shell script
   docker-compose up -d
    ```

### Setup the environment (linux)

1. Install the dependencies:
   
   ```bash
   pip3 install -r requirements.txt
   ```
   
2. Install `ffmpeg`

   ```bash
   sudo apt-get install ffmpeg
   ```

3. Install `ngrok` :

   * Click this [link](https://ngrok.com/download) and follow the instructions.

### Launch the app

1. launch ngrok tunnel on port 8000:

   ```bash
   ./ngrok http 8000
   ```

2. go to `djangobot/settings.py`file and change the following:

   ```python
   
   ALLOWED_HOSTS = ['ngrok address','localhost','127.0.0.1']
   
   # change ngrok address to the one you got from your ngrok tunnel
   # don't forget to remove 'https://'
   ```

3. Run the server:

   ```bash
   python3 manage.py runserver
   ```

4. Finally, enter the link in the web app 

## Q&A

- Where is the main part of the bot?

  - It is a little deep, but it can be found under [botserver/meetbot.py](https://github.com/evjf/PR-google-meet-bot/blob/master/botserver/meetbot.py.). Make sure to check other places, as they have the other pieces of information.

- How do I ask more questions?

  - You can create an issue with the title having "Question: " in it.
