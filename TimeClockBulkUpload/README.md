# Time Clock Bulk Upload

A single-file web app for adding users to a time clock system and generating a
bulk-upload file. It's just **`index.html`** — no install, no Python, works on
any OS. Double-click it to open in a browser, or share the one file with anyone.

## How to use

1. Open **`index.html`** in a web browser (Chrome, Edge, Firefox, or Safari).
2. *(Optional)* Under **Excel record**, click **Load existing record** and pick
   your most recent `TimeClockUsers_*.xlsx`. This loads every user already in it
   so their IDs are blocked as duplicates.
3. Enter a user — **ID, First Name, Last Name, Pin, Passcode** — and click
   **Add User** (or press Enter). Repeat for as many users as you need.
4. Click **Generate Files**. The app downloads:
   - **`Ecuser.txt`** — the batch you just entered, ready to upload.
   - **`TimeClockUsers_YYYY-MM-DD.xlsx`** — a brand-new dated workbook containing
     **every** user (the ones loaded in step 2 plus the new batch).
5. Next time, load that dated `.xlsx` in step 2 to carry the running record
   forward and keep blocking duplicate IDs.

## The `Ecuser.txt` format

Every user is one line; every field is written as `fieldID=fieldvalue` with
fields separated by commas:

```
id=1,First=John,Last=Doe,Pin=1234,Passcode=5678,cardNum=,FaceFlag=1,FingerprintFlag=0;
id=2,First=Jane,Last=Smith,Pin=4321,Passcode=8765,cardNum=,FaceFlag=1,FingerprintFlag=0;
```

Every line ends with the fixed suffix `,cardNum=,FaceFlag=1,FingerprintFlag=0;`
required by the time clock.

Field IDs written to the file:

| Prompt      | Field ID in file |
| ----------- | ---------------- |
| ID          | `id`             |
| First Name  | `First`          |
| Last Name   | `Last`           |
| Pin         | `Pin`            |
| Passcode    | `Passcode`       |

## How duplicate IDs are prevented

The downloaded `.xlsx` is a running record. Because browsers can't silently
re-write a file on your disk, the flow is **load-in / save-out**: you load the
latest record when you start, and the app saves a new dated record when you
finish. Any ID already present — in the loaded record **or** in the current
batch — is rejected when you click *Add User*. (IDs are matched smartly, so
`1`, `1.0` and `"1"` count as the same ID, since Excel sometimes stores whole
numbers as `1.0`.)

## Notes

- **All five fields are required.** Values can't contain a comma or an equals
  sign, since those delimit the file format.
- Generated files land in your browser's **Downloads** folder. If prompted to
  "allow multiple downloads", say yes — that's the `.txt` and the `.xlsx`.
- The app runs entirely in your browser. Nothing is uploaded anywhere; the
  SheetJS spreadsheet library is bundled inside `index.html` so it also works
  offline.
- The record format is `.xlsx` (the modern Excel workbook format), which opens
  in Excel and any compatible spreadsheet app.
