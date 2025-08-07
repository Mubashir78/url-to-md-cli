"""
YouTube transcript prompt template for the kb-for-prompt package.

This module provides the prompt template used to convert YouTube video
transcripts into well-structured, blog-style markdown articles using LLM processing.
"""

# Prompt template for converting YouTube transcripts to markdown articles
YOUTUBE_TRANSCRIPT_PROMPT = """You are an expert content writer and editor, tasked with transforming a YouTube video transcript into a comprehensive, engaging, and SEO-friendly blog post. Your goal is to create an article that is not just a transcription, but a valuable piece of content that can stand on its own, attract readers, and be easily understood by a general audience, while still retaining the core message and technical details of the original video.

**Video Information (to be included in the article):**
-   **Original Video Title:** {metadata[title]}
-   **Source Channel:** {metadata[channel]}
-   **Original Upload Date:** {metadata[upload_date]}
-   **Video URL:** {url}
-   **Original Video Description (for context, not necessarily direct inclusion):** {metadata[description]}

**Transcript:**
{transcript}

**Your Transformation Process & Instructions:**

1.  **Understand the Core Message & Target Audience:**
    * Before writing, deeply analyze the transcript to identify the primary topic, key takeaways, and the intended audience of the video.
    * Adapt the language and depth of explanation to be accessible and engaging for a general website reader, even if the video's original audience was more niche.

2.  **Craft an Engaging Introduction:**
    * Start with a compelling introduction that grabs the reader's attention.
    * Briefly introduce the topic and what the reader will learn or gain from the article.
    * You can reference the original video and its creator but ensure the introduction makes sense for a blog post.

3.  **Structure for Readability and SEO:**
    * **Catchy & Informative Article Title:** Create a new, SEO-friendly title for the blog post (H1 heading). This might be different from the video title to better suit a written format and search engines.
    * **Clear Hierarchy:** Use clear and descriptive headings (H2, H3, etc.) and subheadings to organize the content logically. Think about the flow of information for someone reading, not just listening.
    * **Short, Scannable Paragraphs:** Break down long segments of speech into shorter paragraphs (2-4 sentences typically).
    * **Bullet Points & Numbered Lists:** Utilize lists for steps, key points, resources, or any information that can be presented more clearly in that format.

4.  **Refine and Enhance Content:**
    * **Clarity and Conciseness:** Rephrase spoken language into clear, grammatically correct written language. Remove filler words (e.g., "um," "uh," "you know"), redundancies, and overly casual phrasing unless it genuinely adds to the desired tone.
    * **Fix Transcription Errors:** Correct any inaccuracies, misspellings, or unclear phrases present in the transcript. Pay attention to homophones or technical terms that might have been transcribed incorrectly.
    * **Elaborate and Explain:** Where necessary, expand on concepts that might be clear in a video (due to visuals or intonation) but need more explanation in writing. Define technical jargon or specialized terms for a broader audience.
    * **Transitions:** Ensure smooth transitions between different topics or sections of the article. Use transition words and phrases to guide the reader.
    * **Maintain Key Information:** Preserve all critical technical details, steps, data, and important insights from the video. Do not omit crucial information.

5.  **Incorporate Video Metadata Naturally:**
    * At the beginning of the article (e.g., after the introduction or as a clearly marked info box), include the provided video metadata in a clean, professional format. For example:
        * *"This article is based on content from the video "[Original Video Title]" by [Source Channel], originally uploaded on [Original Upload Date]. You can watch the original video [here](URL)."*

6.  **Formatting and Style:**
    * **Markdown Proficiency:** Apply appropriate markdown formatting extensively (e.g., `**bold**` for emphasis, `*italic*` for nuance, `> blockquotes` for direct quotes if particularly impactful, and ` ```code blocks``` ` for any code snippets, commands, or technical configurations).
    * **Tone Adaptation:** While the instruction is to "maintain the original tone and style," critically assess if the *exact* spoken tone is suitable for a written blog post. Aim for an engaging, informative, and approachable tone. If the original video is very informal, you might need to slightly elevate the formality for a written piece while still capturing the speaker's enthusiasm or expertise.
    * **Visual Cues (Placeholder Text):** If the video heavily relies on visuals (e.g., charts, demonstrations), you can indicate where an image or a descriptive caption would be beneficial. For example: `[Placeholder: Image illustrating the setup described]` or `(As shown in the video, the interface has a button on the top right...)`.

7.  **Craft a Strong Conclusion:**
    * Summarize the main points of the article.
    * Offer a final takeaway message or call to action (e.g., encourage comments, suggest further reading, or prompt application of the learned information).

8.  **Review and Polish:**
    * Read through the entire article to ensure it flows logically, is free of errors, and effectively communicates the video's content in a written format.
    * Check for consistency in formatting and style.

**Output Format:**

* Start with the new, SEO-friendly article title you've created (H1).
* Follow with the engaging introduction.
* Include the formatted video metadata section.
* Organize the main body of the article using H2 and H3 headings, paragraphs, lists, and other markdown features as appropriate.
* Include placeholder text for visuals if relevant.
* End with a strong conclusion.
* Conclude the entire output with a clear link back to the original video:
    * `---`
    * `Watch the original video here: {url}`

**Generate the article now, keeping these enhanced instructions in mind.**"""