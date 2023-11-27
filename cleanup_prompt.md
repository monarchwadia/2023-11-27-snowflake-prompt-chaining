**Generalized Instructions for Language Model for Code Cleanup Task**

I will paste a specific piece of code, which could be in any programming language, including but not limited to HTML, CSS, JavaScript, Python, or Java. This code may include additional narrative or instructional text. Your task is to process this text and extract only the code, removing any non-code elements, comments, or instructional content. The goal is to provide me with a clean, standalone version of the code block I provide, without altering its functionality or structure. The output should be the exact code I provide, but without the extra narrative or instructional text.

IMPORTANT: YOU ARE OUTPUTTING A SINGLE SOURCE FILE THAT HAS ALL RELEVANT CODE! THERE WILL BE NO OTHER FILES!

For clarity, here are three examples of what I will provide and what I expect in return:

**Example 1 (HTML/CSS/JavaScript):**

For HTML/CSS/JavaScript, there is a need to include all the code in a single HTML file, within the DOM structure (i.e. scripts will be included in between <script></script> tags and CSS will be contained within <script></script> tags). 

**Input Text with Code and Instructions:**
```
Sure! Here's an example of a simple digital clock using HTML5, CSS, and JavaScript:

HTML:
```
<!DOCTYPE html>
<html>
  <head>
    <title>Digital Clock</title>
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
    <div class="clock">
      <h1 id="time"></h1>
    </div>
    <script src="script.js"></script>
  </body>
</html>
```

CSS (style.css):
```
.clock {
  text-align: center;
  margin-top: 200px;
}

#time {
  font-size: 60px;
  color: #333;
}
```

JavaScript (script.js):
```
function displayTime() {
  var currentTime = new Date();
  var hours = currentTime.getHours();
  var minutes = currentTime.getMinutes();
  var seconds = currentTime.getSeconds();

  // Pad the minutes and seconds to two digits if necessary
  minutes = (minutes < 10 ? "0" : "") + minutes;
  seconds = (seconds < 10 ? "0" : "") + seconds;

  // Choose between AM or PM
  var ampm = hours < 12 ? "AM" : "PM";

  // Convert to 12-hour format
  hours = hours > 12 ? hours - 12 : hours;
  hours = hours === 0 ? 12 : hours;

  // Get the final time string
  var timeString = hours + ":" + minutes + ":" + seconds + " " + ampm;

  // Update the time element in the HTML document
  document.getElementById("time").innerHTML = timeString;
}

// Run displayTime function every second
setInterval(displayTime, 1000);
```

**Expected Cleaned Output:**

<!DOCTYPE html>
<html>
  <head>
    <title>Digital Clock</title>
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
    <div class="clock">
      <h1 id="time"></h1>
    </div>
    <script>
        function displayTime() {
            var currentTime = new Date();
            var hours = currentTime.getHours();
            var minutes = currentTime.getMinutes();
            var seconds = currentTime.getSeconds();

            // Pad the minutes and seconds to two digits if necessary
            minutes = (minutes < 10 ? "0" : "") + minutes;
            seconds = (seconds < 10 ? "0" : "") + seconds;

            // Choose between AM or PM
            var ampm = hours < 12 ? "AM" : "PM";

            // Convert to 12-hour format
            hours = hours > 12 ? hours - 12 : hours;
            hours = hours === 0 ? 12 : hours;

            // Get the final time string
            var timeString = hours + ":" + minutes + ":" + seconds + " " + ampm;

            // Update the time element in the HTML document
            document.getElementById("time").innerHTML = timeString;
        }

        // Run displayTime function every second
        setInterval(displayTime, 1000);
    </script>
    <style>
        .clock {
            text-align: center;
            margin-top: 200px;
        }

        #time {
            font-size: 60px;
            color: #333;
        }
    </style>

  </body>
</html>


**Example 2 (Python):**

**Input Text with Code and Instructions:**
```
Here is a Python function to calculate the factorial of a number:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

You can use this function to find the factorial of any non-negative integer.
```

**Expected Cleaned Output:**

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


**Example 3 (Java):**

**Input Text with Code and Instructions:**
```
This is a Java method to reverse a string:

```java
public String reverseString(String s) {
    StringBuilder sb = new StringBuilder(s);
    return sb.reverse().toString();
}
```

You can use this method to reverse any string in Java.
```

**Expected Cleaned Output:**

public String reverseString(String s) {
    StringBuilder sb = new StringBuilder(s);
    return sb.reverse().toString();
}


