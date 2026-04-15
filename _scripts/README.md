# Utility Scripts

Helper scripts for managing the Bible curriculum repository.

## convert-heic.sh

Converts HEIC images to JPG format (macOS only, uses built-in `sips` command).

**Usage**:
```bash
# Convert HEICs in current directory
./_scripts/convert-heic.sh

# Convert HEICs in specific directory
./_scripts/convert-heic.sh classes/understanding-the-faith/syllabus

# From anywhere in the repo
./_scripts/convert-heic.sh path/to/images
```

**What it does**:
- Finds all `.heic` files (case-insensitive)
- Converts each to `.jpg` in the same directory
- Keeps originals (you can delete manually after)
- Silent mode — only shows progress, not `sips` verbose output

**Delete originals after conversion**:
```bash
rm classes/understanding-the-faith/syllabus/*.heic
```
