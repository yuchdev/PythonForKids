The traditional way to start programming in a new language is to get your computer to say, “Hello, World!”

```python
from microbit import display
display.scroll("Hello, World!")
```

MicroPython comes with lots of built-in pictures to show on the display 

For example, to make the device appear happy you type:

```python
display.show(Image.HAPPY)
```

Here’s a list of the built-in images we display every second.
To cycle through the images, we can use a for loop:

```python
images_list = [Image.HEART, Image.HEART_SMALL, Image.HAPPY, Image.SMILE, Image.SAD, Image.CONFUSED, Image.ANGRY,
               Image.ASLEEP, Image.SURPRISED, Image.SILLY, Image.FABULOUS, Image.MEH, Image.YES, Image.NO,
               Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6,
               Image.CLOCK5, Image.CLOCK4, Image.CLOCK3, Image.CLOCK2, Image.CLOCK1]

for image in images_list:
    display.show(image)
    sleep(1000)  # sleep for 1 second
```

The `display.show()` function can also be used to show numbers 

For example, to show the number 0:

```python
display.show(0)
```

Output is what the device puts out to the world whereas input is what goes into the device for it to process.
The most obvious means of input on the micro:bit are its two buttons, labelled A and B.

Somehow, we need MicroPython to react to button presses.

```python
# this script sleeps for 5 seconds and then scrolls the number of times you pressed button A
sleep(5000)
display.scroll(str(button_a.get_presses()))
```


This script shows a happy face when you press button A

```python
while True:
    if button_a.was_pressed():
        display.scroll('A')
```


This script shows a happy face when you press button A and a sad face when you press button B 
Rest of the time it shows a sleeping face

```python
while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)
    else:
        display.show(Image.ASLEEP)
```
