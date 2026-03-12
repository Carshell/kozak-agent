import subprocess

result = subprocess.run(
    ["systemctl", "is-active", "--quiet", "ssh"]
)

print(result.returncode)