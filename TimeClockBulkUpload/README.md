# Time Clock Bulk Upload

A small standalone desktop app for adding users to a time clock system and
generating a bulk-upload file.

## What it does

1. You enter users one at a time: **ID, First Name, Last Name, Pin, Passcode**.
2. You can add as many users as you like. Nothing is written to disk until you
   click **Generate File**.
3. It writes **`Ecuser.txt`**, where every user is one line and every field is
   written as `fieldID=fieldvalue`, with fields separated by commas:

   ```
   id=1,First=John,Last=Doe,Pin=1234,Passcode=5678
   id=2,First=Jane,Last=Smith,Pin=4321,Passcode=8765
   ```

   The field IDs written to the file are:

   | Prompt      | Field ID in file |
   | ----------- | ---------------- |
   | ID          | `id`             |
   | First Name  | `First`          |
   | Last Name   | `Last`           |
   | Pin         | `Pin`            |
   | Passcode    | `Passcode`       |

4. **Excel record (to prevent duplicate IDs).** You can link the app to an
   Excel workbook (`.xlsx`). When you link an existing file the app reads all
   IDs already in it; when you generate a batch the new users are appended to
   the workbook. Any ID that already exists — in the workbook or in the current
   batch — is rejected, so you never reuse an ID.

   - **New record…** creates a fresh workbook with a header row.
   - **Link existing…** points the app at a workbook you already have. The
     **first column** is treated as the ID column and the first row as a header.

## Running from source (any OS)

```bash
pip install openpyxl          # optional: enables the Excel record feature
python time_clock_bulk_upload.py
```

The app runs without `openpyxl`; only the Excel record feature is disabled in
that case (`Ecuser.txt` generation still works).

## Building the Windows .exe

On a Windows machine with Python 3 installed, just run:

```bat
build_exe.bat
```

It installs `openpyxl` and `pyinstaller`, then builds the executable. When it
finishes, your standalone app is at:

```
dist\TimeClockBulkUpload.exe
```

That `.exe` is self-contained — it can be copied to another Windows PC and run
without installing Python.

To build it manually instead:

```bat
pip install openpyxl pyinstaller
pyinstaller --onefile --windowed --name TimeClockBulkUpload --collect-all openpyxl time_clock_bulk_upload.py
```

## Notes

- **Required fields:** all five — ID, First Name, Last Name, Pin and Passcode.
- Values may not contain a comma or an equals sign, since those characters
  delimit the file format; the app blocks them on entry.
- IDs are compared smartly: `1`, `1.0` and `"1"` are treated as the same ID,
  because Excel sometimes stores whole numbers as `1.0`.
- The Excel record format is `.xlsx` (the modern Excel workbook format), which
  opens in Excel and any compatible spreadsheet app.
