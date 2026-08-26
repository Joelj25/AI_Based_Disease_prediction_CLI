from PIL import Image, ImageDraw, ImageFont
import sys
import os

def generate_terminal_screenshot(text_file, output_image):
    if not os.path.exists(text_file):
        print(f"File {text_file} not found.")
        return
        
    with open(text_file, 'r') as f:
        lines = f.readlines()
        
    # Remove excessive empty lines at the end
    while lines and lines[-1].strip() == '':
        lines.pop()
        
    # Configuration
    bg_color = (30, 30, 30) # Dark gray background
    text_color = (0, 255, 0) # Terminal green text
    padding = 20
    line_height = 20
    char_width = 8
    
    # Try to load a monospaced font, fallback to default
    try:
        # Assuming Windows
        font = ImageFont.truetype("consola.ttf", 14)
        line_height = 18
        char_width = 8
    except Exception:
        font = ImageFont.load_default()
        
    # Calculate image dimensions
    max_line_length = max([len(line.rstrip('\n')) for line in lines] + [40])
    img_width = max(max_line_length * char_width + padding * 2, 600)
    img_height = len(lines) * line_height + padding * 2
    
    # Create image
    img = Image.new('RGB', (img_width, img_height), color=bg_color)
    d = ImageDraw.Draw(img)
    
    # Draw text
    y_text = padding
    for line in lines:
        d.text((padding, y_text), line.rstrip('\n'), font=font, fill=text_color)
        y_text += line_height
        
    # Save image
    img.save(output_image)
    print(f"Generated screenshot: {output_image}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python screenshot_generator.py <input_text_file> <output_png_file>")
    else:
        generate_terminal_screenshot(sys.argv[1], sys.argv[2])
