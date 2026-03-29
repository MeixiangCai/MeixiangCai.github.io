# AI-Powered TXT to PPT Generator

## Objective
Automatically convert TXT documents into structured, presentation-ready HTML slides using AI.

## Features
	•	Extracts main title, chapters, and pages from raw text.
	•	Generates structured JSON representation of content.
	•	Uses Jinja2 templates to create HTML slides for:
	•	Welcome page
	•	Directory page
	•	Chapter overview pages
	•	Chapter detail pages
	•	Thank you page

## Process
	1.	Read a TXT file containing work summaries.
	2.	Use OpenAI API with a few-shot prompt to structure content into JSON.
	3.	Render slides using Jinja2 templates, filling in titles, descriptions, and body content.
	4.	Combine all rendered slides into a final HTML file (out_put.html).
	
- The .txt to be converted has been provided.
- The prompt template has been provided.
- The output .html has also been provided for reference.

