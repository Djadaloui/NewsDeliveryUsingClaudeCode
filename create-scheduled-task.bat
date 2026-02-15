@echo off
REM Create scheduled task for daily research digest

schtasks /create ^
  /tn "Daily Database Research" ^
  /tr "powershell.exe -ExecutionPolicy Bypass -File C:\Users\DELL\data-Engineering-Tools\NewsDeliveryUsingClaudeCode\run-research.ps1" ^
  /sc daily ^
  /st 05:00 ^
  /ru "%USERNAME%" ^
  /rl highest ^
  /f

echo.
echo Scheduled task created successfully!
echo The research will run daily at 5:00 AM
echo.
echo To verify: schtasks /query /tn "Daily Database Research"
echo To delete: schtasks /delete /tn "Daily Database Research" /f
pause
