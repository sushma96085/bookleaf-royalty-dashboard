# BookLeaf Assignment 2 — consolidated handoff (27 October 2026)

## What is included
- `local_demo/bookleaf_fixed/`: runnable Node.js reference app, dataset, Bubble import CSVs, and a sample n8n workflow. Run `npm start` inside this folder, then open `http://localhost:5050`. Run `npm test` for local smoke tests. These tests passed in the packaging environment: health, dataset counts, author login, isolation, own data, admin login.
- `n8n_bubble_starter/bookleaf_assignment2_package/`: n8n webhook/AI/Bubble logging starter workflow, sample payload, Bubble setup notes, testing checklist.

## What is NOT complete or verified
This ZIP is NOT an export of your existing Bubble app, and cannot install or update it automatically. The assignment requires the real Bubble app and an n8n Cloud workflow. Your existing Bubble project is at https://bubble.io/page?id=bookleaf-royalty-dashboard-39532. No account changes, real Bubble login tests, live n8n execution, callback test, email send, or recording have been performed. The sample n8n JSON is a starter, not a production-verified workflow. It lacks fully tested error handling and robust duplicate prevention. Do not submit as 100% complete.

## Minimum remaining account-side tasks
1. Verify Bubble author/admin user roles, record relationships, privacy rules, actual royalty totals, My Books and admin filters.
2. Enable only required Bubble API access and protect it. Ensure `NotificationLog` field API names and create/update methods match the n8n request. Avoid giving browser users admin API tokens.
3. Import ONE n8n workflow JSON, configure secure webhook header auth, AI API credential, Bubble callback credential and actual endpoint. Verify success AND failure branches and duplicate prevention.
4. Test a real author login and a different author login for data isolation; test admin individual and bulk triggers, Bubble log success/failure, and one AI-generated message against the knowledge base.
5. Provide Bubble collaborator access (to the email supplied by HR), live/test URL, test accounts, n8n JSON export, README and 3–5 minute screen recording. Never include real passwords/API keys in the ZIP.

## Security warning
Previously a Bubble admin API key was visible in a screenshot. Ensure it has been regenerated and never embed it in these files. Demo credentials in the local app are for offline testing only; do not deploy publicly.
