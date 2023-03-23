import os
import sys
import subprocess

def find_txt(commit_sha):
    cmd = ['git', 'diff', '--name-only', '--diff-filter=A', commit_sha]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Error: git diff command failed.")
        sys.exit(1)
    
    file_list = result.stdout.split('\n')
    txt_files = [file for file in file_list if file.startswith('contributions/') and file.endswith('.txt')]
    
    if len(txt_files) != 1:
        print("Error: No .txt file found in 'contributions' folder or multiple .txt files found.")
        sys.exit(1)

    return txt_files[0]

if __name__ == "__main__":
    commit_sha = sys.argv[1]
    txt_file = find_txt(commit_sha)
    print(txt_file)
