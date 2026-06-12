import os
import requests
import json

CONIFER_URL = "http://localhost:1234/v1/chat/completions"

def tailor_resume(latex_path, job_description_path, output_path):
    if not os.path.exists(latex_path):
        print(f"❌ Error: Could not find base resume file at {latex_path}")
        return

    with open(latex_path, "r", encoding="utf-8") as f:
        latex_content = f.read()

    with open(job_description_path, "r", encoding="utf-8") as f:
        job_desc = f.read()

    system_prompt = (
        "You are an expert technical resume architect. Your task is to adjust a LaTeX resume "
        "to highlight relevant engineering experiences for a target job description.\n"
        "Rules:\n"
        "1. Maintain the structural syntax exactly (do not break commands like \\item, \\textbf, \\section).\n"
        "2. Translate bullet points semantically based on existing facts (do not invent fake projects or work history).\n"
        "3. Output ONLY valid, raw compilable LaTeX text code. No markdown wrapping or extra commentary."
    )

    payload = {
        "model": "qwen2.5-coder",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"JOB REQS:\n{job_desc}\n\nORIGINAL LATEX:\n{latex_content}"}
        ],
        "temperature": 0.1
    }

    try:
        print("🤖 Communicating with local Conifer inference core...")
        response = requests.post(CONIFER_URL, json=payload, timeout=60)
        if response.status_code == 200:
            result = response.json()["choices"][0]["message"]["content"]
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"✨ Successfully optimized and generated: {output_path}")
        else:
            print(f"❌ Core API Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Failed to reach local LLM server. Is Conifer running on port 1234? Error: {e}")

if __name__ == "__main__":
    # Fallback dry-run files for local student verification
    base_tex = "backend/resume.tex"
    target_job = "backend/job_description.txt"
    out_tex = "backend/tailored_resume.tex"
    
    # Generate mock data files if they do not exist for testing purposes
    if not os.path.exists(base_tex):
        with open(base_tex, "w") as f: f.write("\\section{Experience}\n\\item Developed backend APIs using Python.")
    if not os.path.exists(target_job):
        with open(target_job, "w") as f: f.write("Looking for a engineer who understands Python backend structures.")

    tailor_resume(base_tex, target_job, out_tex)