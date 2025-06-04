"""
YouTube transcript prompt template for the kb-for-prompt package.

This module provides the prompt template used to convert YouTube video
transcripts into well-structured, blog-style markdown articles using LLM processing.
"""

# Prompt template for converting YouTube transcripts to markdown articles
YOUTUBE_TRANSCRIPT_PROMPT = """You are a technical content writer tasked with converting a YouTube video transcript into a well-structured, blog-style article. 

Video Information:
- Title: {metadata[title]}
- Channel: {metadata[channel]}
- Upload Date: {metadata[upload_date]}
- URL: {url}
- Description: {metadata[description]}

Transcript:
{transcript}

Instructions:
1. Create a comprehensive blog-style article based on the video content
2. Structure the content with clear headings and subheadings
3. Preserve all technical details and important information
4. Improve readability by organizing content into logical paragraphs
5. Include the video metadata at the beginning in a professional format
6. Fix any transcription errors or unclear phrases
7. Add appropriate markdown formatting (headers, lists, code blocks if applicable)
8. Maintain the original tone and style of the content
9. Ensure the article flows naturally as written content, not spoken word

Output Format:
- Start with a title (# heading)
- Include video metadata in a clean format
- Organize content with proper markdown hierarchy
- Use lists, emphasis, and other markdown features where appropriate
- End with a link back to the original video

Generate the article now:"""