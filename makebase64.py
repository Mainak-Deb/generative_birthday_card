import base64

# Read image file and convert to Base64
with open("mandelbrot_fractal.png", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')

# Write Base64 string to an HTML file
with open("output.html", "w") as html_file:
    html_file.write(f'''
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Base64 Image Example</title>
    </head>

    <body>
        <h1>Base64 Image Example</h1>
        <img src="data:image/jpg;base64,{base64_image}" alt="Base64 Image">
    </body>

    </html>
    ''')

print("HTML file generated successfully.")
