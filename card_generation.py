from PIL import Image, ImageDraw, ImageFilter

import random

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to generate a random pattern
def generate_pattern(draw, width, height):
    num_shapes = random.randint(5, 100)
    for _ in range(num_shapes):
        shape = random.choice(["rectangle", "circle"])
        color = random_color()
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 =x1+ random.randint(0, 500),y1+ random.randint(0, 500)

        if shape == "rectangle":
            draw.rectangle([x1, y1, x2, y2], fill=color)
        else:
            diameter = random.randint(20, 100)
            draw.ellipse([x1, y1, x1 + diameter, y1 + diameter], fill=color)

# Function to generate a greeting card
def generate_greeting_card():
    width, height = 800, 600
    background_color = random_color()

    # Create a blank image with a random background color
    img = Image.new("RGB", (width, height), background_color)
    
    # Initialize ImageDraw
    draw = ImageDraw.Draw(img)
    
    # Generate random patterns on the card
    generate_pattern(draw, width, height)
    
    img = img.filter(ImageFilter.GaussianBlur(radius=10))

    # Save the image as a greeting card
    img.save("greeting_card.png")
    print("Greeting card generated and saved as 'greeting_card.png'.")

# Generate a greeting card
generate_greeting_card()
