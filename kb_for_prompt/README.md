# KB for Prompt

A CLI tool that converts online and local documents (URLs, YouTube videos, Word, and PDF files) into Markdown files using the docling library and LLM processing.

## Features

- Supports multiple input types:
  - URLs
  - YouTube videos (via transcript extraction)
  - Word documents (.doc/.docx)
  - PDF files
- Provides two conversion modes:
  - Batch conversion (using a CSV file with a mix of URLs and file paths)
  - Single item conversion
- Interactive menu for user-friendly operation
- Automatic input type detection (including YouTube URL recognition)
- Validation of local file inputs
- Error handling with retries
- Detailed conversion summary
- LLM-powered YouTube transcript processing for readable blog-style output

## Installation

### Requirements

- Python >= 3.11
- Rust and Cargo (required for building the tokenizers library)
- uv (optional but recommended)
- No YouTube API key required

> **Note**: This project depends on libraries like `tokenizers` which contain native Rust components. You need to have Rust and Cargo installed on your system. To install Rust, visit [rustup.rs](https://rustup.rs) or run:
> ```bash
> curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
> ```

### Using uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/kb-for-prompt.git
cd kb-for-prompt

# Run with uv
uv run --script kb_for_prompt/pages/kb_for_prompt.py
```

### Traditional Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/kb-for-prompt.git
cd kb-for-prompt

# Install dependencies
pip install -r requirements.txt

# Run the application
python kb_for_prompt/pages/kb_for_prompt.py
```

## Usage

The application provides an interactive menu to guide you through the conversion process. Here are the basic operations:

### Batch Conversion

1. Prepare a CSV file with URLs and/or local file paths
2. Select "Batch conversion mode" from the main menu
3. Enter the path to your CSV file
4. Specify the output directory
5. The application will process all inputs and generate markdown files in the output directory

### Single Item Conversion

1. Select "Single item conversion mode" from the main menu
2. Enter a URL, YouTube video URL, or local file path
3. Enter an output file name (or accept the default)
4. Enter an output directory (or accept the default)
5. The application will convert the input and generate a markdown file

**Example YouTube URL**: `https://www.youtube.com/watch?v=Y5elLLjcmLU`

Output filename will be automatically generated based on the video title.

### YouTube Video Support

The tool supports converting YouTube videos to readable markdown documents by:

- **Extracting transcripts**: Automatically fetches video transcripts (prefers manual captions over auto-generated)
- **Supported URL formats**:
  - `https://www.youtube.com/watch?v=VIDEO_ID`
  - `https://youtu.be/VIDEO_ID`
  - `https://m.youtube.com/watch?v=VIDEO_ID`
  - YouTube embed and other variations
- **LLM Processing**: Transcripts are processed using an LLM to create well-structured, blog-style articles
- **Automatic metadata**: Extracts video title, channel, and duration when available
- **Batch support**: YouTube URLs can be mixed with other input types in CSV files

**Limitations**:
- Videos must have captions/transcripts enabled
- Private or age-restricted videos may not be accessible
- No API key required - uses public transcript data

## Project Structure

The project follows atomic design principles for clear separation of concerns:

- **atoms**: Basic utility functions (file path resolution, validation, etc.)
- **molecules**: Individual conversion functions (URL, Word, PDF)
- **organisms**: Orchestration of conversion processes (batch, single item)
- **templates**: Display components for the CLI interface
- **pages**: Main entry points for the application

## Development

### Code Style

Follow PEP 8 guidelines and maintain clear separation between different atomic design layers.

### Testing

```bash
# Run tests
pytest
```

## License

MIT

## Troubleshooting

### YouTube-Related Issues

**"Transcripts are disabled for this video"**
- The video owner has disabled captions/transcripts
- Try a different video or check if captions are available on YouTube

**"No transcripts found"**
- The video may not have any captions available
- Some live streams or very new videos might not have transcripts yet

**Network timeouts**
- YouTube transcript fetching may occasionally timeout
- The tool will automatically retry up to 3 times
- Check your internet connection if errors persist

**Private or deleted videos**
- The tool cannot access private, deleted, or age-restricted content
- Ensure the video is publicly accessible

## Acknowledgments

- docling library for document conversion
- Rich library for beautiful terminal interfaces
- youtube-transcript-api for YouTube transcript extraction