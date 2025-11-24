import re
import sys

def test_service_worker_paths():
    print("Checking service-worker.js for absolute paths...")
    try:
        with open('service-worker.js', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("service-worker.js not found!")
        sys.exit(1)

    # Extract the array urlsToCache
    match = re.search(r'const urlsToCache = \[(.*?)\];', content, re.DOTALL)
    if not match:
        print("Could not find urlsToCache")
        sys.exit(1)

    array_content = match.group(1)
    # Find strings
    urls = re.findall(r'"(.*?)"', array_content)

    print(f"Found URLs: {urls}")

    failed = False
    for url in urls:
        if url.startswith('/'):
            print(f"Error: URL '{url}' is absolute. It should be relative for GitHub Pages compatibility.")
            failed = True

    if failed:
        print("Test FAILED: Absolute paths found.")
        sys.exit(1)
    else:
        print("Test PASSED: All paths are relative.")
        sys.exit(0)

if __name__ == "__main__":
    test_service_worker_paths()
