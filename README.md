<h1>Gun Detection System using OpenCV and Telegram</h1>
<p>This is a Python script that uses OpenCV, Telegram API, and Pygame to detect guns in a video stream from a camera. If guns are detected, an alarm sound is played, and a message is sent to a Telegram chat using a bot. The script can be used for security purposes to detect guns in public places or restricted areas.</p>
<h1>Requirements</h1>
<ul>
<li>Python 3.x</li>
<li>OpenCV</li>
<li>NumPy</li>
<li>imutils</li>
<li>Telegram API</li>
<li>Pygame</li>
</ul>
<h1>Installation</h1>
<ul>
<li>Install Python 3.x on your computer.</li>
<li>Install OpenCV, NumPy, and imutils using pip: <em>'pip install opencv-python numpy imutils'</em></li>
<li>Install Telegram API using pip:  <em>'pip install python-telegram-bot'</em></li>
<li>Install Pygame using pip: <em>'pip install pygame'</em></li>
<li>Download the cascade.xml file and the alarm.wav file and save them in the same directory as the Python script.</li>
</ul>
<h1>Usage</h1>
<ul>
<li>Open the Python script in a text editor or IDE.</li>
<li>Replace the YOUR_BOT_TOKEN and YOUR_CHAT_ID with your own bot token and chat ID.</li>
<li>Run the Python script: <em>' python gun_detection.py</em></li>
<li>The script will start capturing frames from the camera and detecting guns. If guns are detected, an alarm sound will be played, and a message will be sent to the Telegram chat. You can stop the alarm sound by pressing the 's' key, and you can exit the script by pressing the 'q' key.</li>
</ul>
<h1>License</h1>
<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
<h1>Acknowledgements</h1>
<p>This project was made by Alexis Valentino for the Project Bagsik "Iot powered smart security surveillance system with Threat Detection (Weapons, Anomaly, Behavior Detection), Android Monitoring app and Night Vision capabilities."

