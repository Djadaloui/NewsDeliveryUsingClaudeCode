@echo off
REM Daily Database & AI News Research Script
REM Runs at 5 AM to generate news digest

set LOGFILE=C:\Users\DELL\data-Engineering-Tools\NewsDeliveryUsingClaudeCode\research-log.txt

echo. >> %LOGFILE%
echo === Research started at %date% %time% === >> %LOGFILE%

REM Run Claude Code with the /research skill
REM Adjust the claude path if needed
claude /research >> %LOGFILE% 2>&1

echo === Research ended at %date% %time% === >> %LOGFILE%
