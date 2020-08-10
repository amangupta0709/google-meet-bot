# Google Meet Bot

An advance level google meet bot which will attend classes on desktop just by sending a link via phone through its web app. It will leave the classes when students are less than 30-40 in a lecture. Also it will simultaneously record the classes and prevent us from leaving the classes by reconnecting till the class end.

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

   