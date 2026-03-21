from pathlib import Path

current_dir = Path.cwd()
#^currrent working directory
current_file = Path(__file__).name
#^fetches current file's absolute path but only the endpoint

print(f"Files in {current_dir}")

for filepath in current_dir.iterdir():
    #^remember the iterdir method to iterate through directories
    if filepath.name == current_file:
        continue
    
    print(f" - {filepath.name}")

    if filepath.is_file():
        #^boolean value (whether current iteration exists)
        content = filepath.read_text(encoding='utf-8')
        #^Use read_bytes() if the file is binary, or stream with open(...) if you need to process large files incrementally.
        print(f"    content: {content}")