import os
import argparse
import subprocess
import sys
from pdf2image import convert_from_path

def is_poppler_installed():
    """Check if poppler is installed on the system."""
    try:
        # Try to run pdftoppm command (part of poppler)
        if sys.platform == "win32":
            result = subprocess.run(["where", "pdftoppm"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:  # macOS, Linux
            result = subprocess.run(["which", "pdftoppm"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except:
        return False

def print_installation_instructions():
    """Print instructions for installing poppler based on the OS."""
    print("\nPoppler is not installed or not in PATH. Please install it:")
    
    if sys.platform == "darwin":  # macOS
        print("\nFor macOS (using Homebrew):")
        print("  brew install poppler")
    
    elif sys.platform == "win32":  # Windows
        print("\nFor Windows:")
        print("  1. Download the latest binary from: https://github.com/oschwartz10612/poppler-windows/releases")
        print("  2. Extract it and add the 'bin' directory to your PATH environment variable")
    
    else:  # Linux
        print("\nFor Ubuntu/Debian:")
        print("  sudo apt-get install poppler-utils")
        print("\nFor Fedora:")
        print("  sudo dnf install poppler-utils")
    
    print("\nAfter installation, restart your terminal/command prompt and try again.")

def convert_pdf_to_images(pdf_path, output_dir=None, format='png', dpi=300):
    """
    Convert a PDF file to individual image files, one per page.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_dir (str, optional): Directory to save images. Defaults to same directory as PDF.
        format (str, optional): Image format (png, jpeg, etc.). Defaults to 'png'.
        dpi (int, optional): Image resolution in DPI. Defaults to 300.
    
    Returns:
        list: Paths to the created image files
    """
    # Set output directory
    if output_dir is None:
        output_dir = os.path.dirname(pdf_path)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get PDF filename without extension
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Convert PDF to list of images
    print(f"Converting PDF: {pdf_path}")
    images = convert_from_path(pdf_path, dpi=dpi)
    
    # Save each image
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_dir, f"{pdf_name}_page_{i+1}.{format}")
        image.save(image_path, format.upper())
        image_paths.append(image_path)
        print(f"Saved page {i+1}/{len(images)} to {image_path}")
    
    return image_paths

def bulk_convert_pdfs(count, output_dir=None, format='png', dpi=300):
    """
    Convert multiple PDF files to images in bulk.

    Args:
        count (int): Number of PDF files to process.
        output_dir (str, optional): Directory to save images. Defaults to same directory as PDFs.
        format (str, optional): Image format (png, jpeg, etc.). Defaults to 'png'.
        dpi (int, optional): Image resolution in DPI. Defaults to 300.

    Returns:
        None
    """
    for i in range(1, count + 1):
        pdf_name = f"{i}.pdf"
        pdf_path = os.path.join(os.path.dirname(__file__), pdf_name)

        if not os.path.exists(pdf_path):
            print(f"Warning: The PDF file '{pdf_path}' does not exist. Skipping.")
            continue

        try:
            print(f"Processing {pdf_name}...")
            convert_pdf_to_images(pdf_path, output_dir, format, dpi)
        except Exception as e:
            print(f"Error processing {pdf_name}: {e}")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert PDF pages to images')
    parser.add_argument('--output-dir', '-o', help='Directory to save images')
    parser.add_argument('--format', '-f', default='png', help='Image format (png, jpeg, etc.)')
    parser.add_argument('--dpi', '-d', type=int, default=300, help='Image resolution in DPI')

    args = parser.parse_args()

    print("Please rename your PDF files to '1.pdf', '2.pdf', '3.pdf', and so on.")
    try:
        count = int(input("Enter the number of PDF files to process: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if not is_poppler_installed():
        print("Error: Poppler is required but not found.")
        print_installation_instructions()
        return

    bulk_convert_pdfs(
        count=count,
        output_dir=args.output_dir,
        format=args.format,
        dpi=args.dpi
    )

if __name__ == "__main__":
    main()
