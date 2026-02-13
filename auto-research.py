#!/usr/bin/env python3
"""
Automated Database & AI News Digest Generator
Runs daily at 5 AM to generate news digest
"""

import os
import sys
from datetime import datetime
import subprocess

def main():
    log_file = r"C:\Haripriya\News\research-log.txt"
    date = datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log start
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"\n=== Research started at {timestamp} ===\n")

    try:
        # Prepare the research prompt
        prompt = f"""Generate a daily digest of database and AI news. Follow these steps:

1. Check these SPECIFIC sources for the latest posts:
   SQL Server: brentozar.com/archive, sqlserver.blog, SQLServerCentral.com
   PostgreSQL: Planet PostgreSQL, Crunchy Data blog, pgvector GitHub releases
   AI Infrastructure: anthropic.com/news, OpenAI blog

2. Search Hacker News for stories about: database, PostgreSQL, SQL Server, AI, vector, embeddings

3. Format as markdown with:
   - Title: Database & AI News Digest - {date}
   - Sections: SQL Server, PostgreSQL, AI Infrastructure, Industry Pulse
   - Raw URLs with 📖 emoji
   - Deduplicate stories

4. Add "Content Ideas for Substack" section (2-3 blog post ideas)

5. Save to: C:\\Haripriya\\News\\digest-{date}.md

If a source is down, note "[Source] unavailable" and continue.

Generate the digest now."""

        # Run Claude Code with the prompt via stdin
        result = subprocess.run(
            ['claude'],
            input=prompt,
            capture_output=True,
            text=True,
            encoding='utf-8',
            timeout=300  # 5 minute timeout
        )

        # Log output
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"STDOUT:\n{result.stdout}\n")
            if result.stderr:
                f.write(f"STDERR:\n{result.stderr}\n")

            if result.returncode == 0:
                f.write("Research completed successfully\n")
            else:
                f.write(f"Command returned error code: {result.returncode}\n")

    except Exception as e:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"Error: {str(e)}\n")

    # Log end
    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"=== Research ended at {end_time} ===\n")

if __name__ == "__main__":
    main()
