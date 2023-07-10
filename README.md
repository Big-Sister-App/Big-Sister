# How to Run the Website Locally
This is assuming you've already cloned the repository on your laptop. If you haven't just Slack me lol, I'm too lazy to write that up rn. The first 3 steps are for when you're setting this up for the first time. After the intial setup you shouldn't have to do all this again. Just reactivating your venv and running the website.

## 1. ENV file
An env file holds something called **environment variables**. Basically you can store sensitive information in the file and then call on that sensistive info throughout our code, without it being displayed in the repository on github (i.e. no one can see it).
<br><br>**Setup**<br>
First time you clone the repository create two files both exactly named `.env`. One should go in the **root** folder of the repository, and the other in the **website** folder. Make sure it is exactly named `.env`. Message me for the information that should go in that file, and make sure you _never_ upload it to github. If you name it `.env` then you dont have to worry about it.

<br>

## 2. VENV folder
A venv stands for a virtual environment. If you want you can learn more about them [here](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/). if not, just know they're useful lol.
<br><br>**Setup**<br>
1. In your repository, in the terminal, run
```python
pip install virtualenv
```
2. Now create the virtual environment
```python
python -m venv .venv
```
3. Next you have to activate the environment (do this every time you see it has closed)
```python
# Mac Activation
source .venv/bin/activate

# Windows Activation
.venv/Scripts/Activate
```
If you've done it correctly you should get a bracket in front of your terminal path that says **(.venv)**
<br><br>
![image](https://github.com/Big-Sister-App/Big-Sister/assets/67931161/092d80e9-47be-466b-8d9f-a82d2915c636)

<br>

## 3. Install Requirements
A reason why we set up the virtual environment is it's like we're cacooning ourselves in a little space with _only_ the imports we actually need for our code. 
<br><br>To install these requirements do:
```python
pip install -r requirements.txt
```

<br>

## 4. Run the Website
You should now be all set and can run the website by doing:
```python
python main.py
```
The terminal will tell you what link to open to see the website.







