# BookLeaf Royalty Dashboard

Assignment 2 reference app and Bubble/n8n integration starter, extracted from BookLeaf_Features_and_Setup.zip.

## Run the local reference app

Requires Node.js 18 or later.

```sh
cd local_demo/bookleaf_fixed
npm start
```

Open http://localhost:5050. Run `npm test` in the same folder for the local smoke checks.

## Contents

- `local_demo/bookleaf_fixed`: Node.js reference app, sample data, import CSVs and example workflow.
- `n8n_bubble_starter`: Bubble/n8n starter workflow, sample request and setup checklist.
- `READ_FIRST_HINDI.md`: setup instructions in Hindi.
- `START_HERE.md`: package scope and remaining verification.

## Integration status

The local files are a reference implementation, not a native Bubble app export. The running n8n Cloud workflow was edited separately; those account-side edits are not automatically included in this ZIP. Live notification delivery, Bubble logging and callbacks still require end-to-end verification. GitHub stores this source; it does not run the Node.js backend.

Use environment variables for real secrets. The included accounts are demo fixtures, not production credentials.
