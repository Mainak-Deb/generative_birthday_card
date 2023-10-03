from PIL import Image
import colorsys
import math

# Function to generate a Mandelbrot fractal
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    if n == max_iter:
        return 0
    return n + 1 - (math.log(math.log2(abs(z))) / math.log(2))

# Function to generate Mandelbrot fractal image
def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    img = Image.new('RGB', (width, height), 'black')
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            # Map pixel coordinate to complex plane
            c = complex(x / width * (x_max - x_min) + x_min, y / height * (y_max - y_min) + y_min)
            # Calculate Mandelbrot value
            mandelbrot_value = mandelbrot(c, max_iter)
            # Map Mandelbrot value to RGB color
            hue = int(255 * mandelbrot_value / max_iter)
            saturation = 255
            value = 255 if mandelbrot_value < max_iter else 0
            r, g, b = colorsys.hsv_to_rgb(hue / 255.0, saturation / 255.0, value / 255.0)
            pixels[x, y] = (int(r * 255), int(g * 255), int(b * 255))

    return img

# Set the dimensions and properties of the Mandelbrot fractal
width, height = 800, 600
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 256

# Generate the Mandelbrot fractal image
mandelbrot_img = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

# Save the image
mandelbrot_img.save("mandelbrot_fractal.png")
print("Mandelbrot fractal generated and saved as 'mandelbrot_fractal.png'.")
