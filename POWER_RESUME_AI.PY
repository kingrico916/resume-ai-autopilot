# RESUME_AI.PY — Final one-page version with Missing Requirements section
from flask import Flask, request, jsonify
import requests
import os
import json
import traceback
import sys

app = Flask(__name__)
app.config['DEBUG'] = True

# Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "your-openrouter-key-here")

def analyze_with_ai(resume_text, candidate_name, job_title, job_description):
    """Send to OpenRouter for AI resume analysis, grading, and rewrite based on a specific job description."""
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        resume_prompt = (
            "Resume Evaluation, Job Fit Analysis, and Targeted Resume Rewrite (Final Form)\n\n"
            "You are an expert hiring analyst specializing in resume evaluation, job fit analysis, and strategic resume rewriting.\n\n"
            "Inputs:\n"
            "- A candidate resume\n"
            "- The full job description text extracted from the employer’s HTML page\n"
            "- The job title\n\n"
            "---\n\n"
            "## Target Job Context\n"
            f"- Job Title: {{job_title}}\n"
            f"- Job Description: {{job_description}}\n\n"
            "Instructions:\n"
            "- Treat the job description as authoritative. Grade, suggest improvements, and rewrite the resume based on the *specific requirements, language, and priorities* described in this posting.\n"
            "- Translate all military experience into strong civilian equivalents (leadership, operations, technical, strategic).\n"
            "- If military rank or branch appears, explicitly map it to a civilian title (e.g., Sergeant → Operations Supervisor).\n"
            "- Do not add or fabricate any experience, skills, or details not present in the original resume. Only rephrase, restructure, or emphasize existing content.\n"
            "- If information is missing, state \"Not provided\" rather than inventing it.\n\n"
            "---\n\n"
            "## 1. Opening Match Grade\n"
            "Assign a letter grade (A+ to F) for the resume’s alignment with the provided job description.\n\n"
            "Grading scale:\n"
            "- A+: ≥90% alignment — highly relevant experience, strong skills match, excellent presentation\n"
            "- B: ~70% alignment — relevant but minor gaps present\n"
            "- C: ~50% alignment — partial fit with notable weaknesses\n"
            "- D: <40% alignment — unlikely to progress without major changes\n"
            "- F: No meaningful relevance\n\n"
            "---\n\n"
            "## 2. Justification\n"
            "Provide 3–5 concise bullet points (≤20 words each) explaining the grade. Focus on:\n"
            "- Alignment with specific job requirements\n"
            "- Match of technical and soft skills\n"
            "- Resume formatting and clarity\n"
            "- Transferability of experience\n\n"
            "---\n\n"
            "## 2a. Missing Requirements (from Job Description)\n"
            "List only requirements that are explicitly present in the job description but **absent** from the resume.\n"
            "- Do not infer or guess. If partially present, do not list.\n"
            "- Use short bullets; 3–7 items max.\n"
            "- If none are clearly missing, output: \"None clearly missing.\"\n\n"
            "---\n\n"
            "## 3. Improvement Suggestions\n"
            "Provide 3 actionable, job-specific changes (≤15 words each) to strengthen the resume’s alignment with this job.\n"
            "If possible, apply these edits in *italics* directly on a short resume snippet.\n\n"
            "---\n\n"
            "## 4. Resume Rewrite\n"
            "Rewrite the resume into a clean, modern, one-page document optimized for this job.\n\n"
            "Rules:\n"
            "- Limit to 1 page (≤350 words)\n"
            "- Align structure and language with the job description’s stated requirements\n"
            "- Translate military ranks into equivalent civilian roles using the provided crosswalk\n"
            "- Convert military jargon into high-impact civilian language (leadership, operations, technical, strategic)\n"
            "- Remove irrelevant details and emphasize quantified achievements\n"
            "- Preserve only information present in the original resume. If unsure, omit.\n\n"
            "---\n\n"
            "## Output Cleanliness\n"
            "- Use only the four primary sections and the Missing Requirements subsection above.\n"
            "- Do not include greetings, explanations, or system commentary.\n"
            "- If required data is missing, output \"Not provided\" instead of guessing.\n"
            "- Never claim to have read external files; operate only on the text provided here."
        )

        # Format the prompt with dynamic content
        prompt = resume_prompt.format(
            job_title=job_title,
            job_description=job_description
        )

        # Append the actual resume and candidate for explicit context
        prompt += f"\n\n---\n\n## Candidate Resume\n{resume_text}\n\nCandidate Name: {candidate_name}\n"

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 2000
        }

        print("🤖 Sending request to OpenRouter...")
        response = requests.post(url, headers=headers, json=data, timeout=45)

        if response.status_code == 200:
            result = response.json()
            analysis = result['choices'][0]['message']['content']
            print("✅ AI analysis completed")
            return analysis
        else:
            error_msg = f"OpenRouter API error: {response.status_code} - {response.text}"
            print(f"❌ {error_msg}")
            return error_msg

    except Exception as e:
        error_msg = f"AI analysis error: {str(e)}"
        print(f"❌ {error_msg}")
        return error_msg

@app.route('/analyze_resume', methods=['POST'])
def analyze_resume():
    try:
        print("\n" + "="*50)
        print("📋 NEW RESUME ANALYSIS REQUEST")
        print("="*50)

        data = request.get_json()
        print(f"📥 Request data: {data}")

        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        # Extract input fields
        resume_text = data.get('resume_text', '')
        candidate_name = data.get('candidate_name', 'Unknown Candidate')
        job_title = data.get('job_title', 'Not specified')
        job_description = data.get('job_description', 'Not provided')

        print(f"👤 Candidate: {candidate_name}")
        print(f"🎯 Target Job Title: {job_title}")
        print(f"📄 Resume length: {len(resume_text)} characters")
        print(f"📑 Job description length: {len(job_description)} characters")

        if not resume_text or len(resume_text.strip()) < 10:
            return jsonify({'error': 'Resume text is required and must be substantial'}), 400

        # Run analysis
        print("🤖 Starting AI analysis with full job context...")
        analysis = analyze_with_ai(resume_text, candidate_name, job_title, job_description)

        return jsonify({
            'candidate_name': candidate_name,
            'job_title': job_title,
            'analysis': analysis,
            'status': 'success'
        })

    except Exception as e:
        error_msg = f"Resume analysis failed: {str(e)}"
        traceback_str = traceback.format_exc()

        print(f"\n❌ ERROR: {error_msg}", file=sys.stderr)
        print(f"❌ TRACEBACK:\n{traceback_str}", file=sys.stderr)

        return jsonify({
            'error': error_msg,
            'traceback': traceback_str,
            'status': 'error'
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'api_key_set': bool(OPENROUTER_API_KEY and OPENROUTER_API_KEY != "your-openrouter-key-here")
    })

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Resume Analysis API',
        'endpoints': {
            'analyze': '/analyze_resume (POST)',
            'health': '/health (GET)'
        },
        'status': 'running'
    })

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 STARTING RESUME ANALYSIS API")
    print("="*50)
    print(f"🔑 API Key Set: {bool(OPENROUTER_API_KEY and OPENROUTER_API_KEY != 'your-openrouter-key-here')}")
    print("="*50)
    app.run(host='0.0.0.0', port=5000, debug=True)
