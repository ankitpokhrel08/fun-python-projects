# PDF to Image Converter

This project provides a Python script to convert PDF files into images, with each page of the PDF saved as a separate image file.

## Prerequisites

- Python 3.x
- `pdf2image` library
- Poppler (required for `pdf2image` to work)

### Installing Poppler

- **macOS**: `brew install poppler`
- **Windows**:
  1. Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases).
  2. Extract it and add the `bin` directory to your PATH environment variable.
- **Linux**:
  - Ubuntu/Debian: `sudo apt-get install poppler-utils`
  - Fedora: `sudo dnf install poppler-utils`

## Usage

1. Rename your PDF files to `1.pdf`, `2.pdf`, `3.pdf`, and so on.
2. Run the script using the following command:

   ```bash
   python pdf_to_images.py --output-dir <output_directory> --format <image_format> --dpi <dpi_value>
   ```

   - `--output-dir` or `-o`: Directory to save the images (optional, defaults to the same directory as the PDFs).
   - `--format` or `-f`: Image format (e.g., `png`, `jpeg`, etc.). Defaults to `png`.
   - `--dpi` or `-d`: Image resolution in DPI. Defaults to `300`.

3. Enter the number of PDF files to process when prompted.

## Example

To convert 3 PDF files to PNG images with 300 DPI and save them in the `output` directory:

```bash
python pdf_to_images.py --output-dir output --format png --dpi 300
```

## Error Handling

- If Poppler is not installed or not in the PATH, the script will display installation instructions.
- If a PDF file is missing, the script will skip it and display a warning.

## License

This project is licensed under the MIT License.
