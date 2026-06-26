@echo off
REM ---------------------------------------------------------------------------
REM Build a standalone Windows .exe for the Time Clock Bulk Upload app.
REM Run this on Windows with Python 3 installed. The finished file appears in
REM the "dist" folder as dist\TimeClockBulkUpload.exe and needs no Python to run.
REM ---------------------------------------------------------------------------

echo Installing build dependencies...
python -m pip install --upgrade pip
python -m pip install openpyxl pyinstaller
if errorlevel 1 goto error

echo Building executable...
python -m PyInstaller --onefile --windowed --name TimeClockBulkUpload ^
    --collect-all openpyxl time_clock_bulk_upload.py
if errorlevel 1 goto error

echo.
echo Done. Your app is at: dist\TimeClockBulkUpload.exe
goto end

:error
echo.
echo Build failed. See the messages above.
exit /b 1

:end
