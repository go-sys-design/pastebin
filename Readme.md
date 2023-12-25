# Pastebin

Start Time: 5:00 PM

## Database

### Pastebin

Item | Type | Size | Note
:--:|:-----:|:----:|:----:|
PasteID | string | 36 | uuid4, Partition Key
UserID  | string | 36 | uuid4
RawContent | string | 10k | average size of content
ContentURL | string | 100 | AWS S3 URL
TimestampCreated | number | | timestamp
TimestampModified | number | | timestamp

