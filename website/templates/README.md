# Instructions
**Only** put html files in this folder. If the file does not end in '.html' do not put it in here.

For images/gifs/videos, `.css` files, and `.js` files. Write them as follows:
```html
<!-- Images
.png, .jpeg, .gif etc all follow the same format. just change the file extension in the line below -->
<img src="{{ url_for('static', filename='images/imagename.png') }}">
```

<br>

```html
<!-- CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/filename.css') }}">
```

<br>

```html
<!-- JS -->
<script src="{{ url_for('static', filename='javascript/filename.js') }}"></script>
```

<br>

You do not have to do this when linking to **external** things (e.g. you are copying a link to a css file from the internet). But please refrain from doing that and instead just **download** the css or js or whatever file from the website and put it in the appropriate folder.