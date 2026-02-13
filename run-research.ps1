# Daily Database & AI News Research Script
# Runs at 5 AM to generate news digest

$logFile = "C:\Haripriya\News\research-log.txt"
$date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# Log start
Add-Content -Path $logFile -Value "`n=== Research started at $date ==="

try {
    # Run Claude Code with the /research skill
    # Note: Adjust the claude command path if needed
    claude /research 2>&1 | Add-Content -Path $logFile

    Add-Content -Path $logFile -Value "Research completed successfully"
} catch {
    Add-Content -Path $logFile -Value "Error: $_"
}

Add-Content -Path $logFile -Value "=== Research ended ==="
