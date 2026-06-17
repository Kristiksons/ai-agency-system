import subprocess

result = subprocess.run(
    ["ollama", "run", "llama3.1"],
    input="Say hello in one line",
    text=True,
    capture_output=True
)

print("STDOUT:")
print(result.stdout)

print("STDERR:")
print(result.stderr)
