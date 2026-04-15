Create a new class in this Bible curriculum repository.

Follow these steps:

1. Ask the teacher for:
   - Class name (will be used as the folder name, lowercased and hyphenated)
   - Grade level (e.g. 11–12)
   - Textbook or series used
   - Number of chapters or units

2. Create the class directory under `classes/<class-name>/` with this structure:
   ```
   classes/<class-name>/
   ├── README.md
   ├── teaching-map.md      (placeholder — will be generated separately)
   ├── lesson-plans/.gitkeep
   ├── assessments/.gitkeep
   └── handouts/.gitkeep
   ```

3. Generate a `README.md` for the class that includes:
   - Class title
   - Grade level
   - Textbook/series
   - Number of chapters
   - A brief course description (ask the teacher or draft one for review)
   - The standard subfolder layout

4. After creating the class, remind the teacher:
   > To generate a full teaching map, provide the syllabus or chapter list and run `/generate-map`.

5. Update the "Current Classes" section in the root `CLAUDE.md` to include the new class as a stub.
