import subprocess
repo_url = "https://github.com/abernalsec/neocloudsploit"

with open("trivy-sca-vuln.json", "w") as output:
    subprocess.run(["docker", "run", "--rm", "--name", "trivy-sca-vuln", "-v", "/var/run/docker.sock:/var/run/docker.sock", "aquasec/trivy", "repository", repo_url, "-s", "UNKNOWN,MEDIUM,HIGH,CRITICAL", "--scanners", "vuln", "-f", "json"], stdout=output)
