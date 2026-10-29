# BookLeaf Royalty Dashboard — Runnable Local Demo + Bubble/n8n Handoff

## Run in VS Code

1. Install Node.js 18+.
2. Open this folder in VS Code.
3. Run `npm start` (no npm install needed: only built-in Node modules).
4. Open http://localhost:5050 . Health: http://localhost:5050/health .
5. Run `npm test` for automated smoke checks.

Demo logins: admin@bookleaf.demo / Admin@12345; priya.sharma@email.com / Author@12345. All 10 sample authors can use `Author@12345` with their dataset email. **These are insecure DEMO credentials; never deploy them publicly.**

## What works locally

- Real author/admin login with signed, expiring tokens; author data isolation on API routes.
- All 10 authors, 18 books from the supplied JSON, with production and no-payout cases.
- Author books, per-book royalty status, consolidated earned/paid/pending figures.
- Admin author list, city/status/name filters, details, notification log.
- Individual and bulk trigger endpoints with 60-second in-flight deduplication.
- Webhook delivery, shared-secret callback and notification status recording (requires n8n config).

## Important: Bubble submission requirement

**This is NOT a Bubble application**. The employer explicitly requires Bubble for UI, authentication, database, privacy and workflows. The local Node.js application is a working reference/demo and integration aid; a Bubble app must still be built in Bubble's web editor. No Bubble live URL, editor access, or screen recording is provided here. Do not submit this alone as a completed Assignment 2.

## Bubble setup guide

Create data types:

- `Author`: author_id (text unique), name (text), email (text), phone (text), city (text), joined_date (date), user (User).
- `Book`: book_id (text unique), author (Author), title (text), isbn (text), genre (text), publication_date (date optional), status (text), mrp (number optional), author_royalty_per_copy (number optional), total_copies_sold (number), total_royalty_earned (number), royalty_paid (number), royalty_pending (number), last_royalty_payout_date (date optional), print_partner (text optional), available_on (list of texts).
- `NotificationLog`: notification_id (text unique), author (Author), status (text), message (text), created_at (date), updated_at (date).
- `User`: role (text: admin/author), author (Author, optional). Use Bubble's native password authentication.

Import data from `authors_import.csv` first, then `books_import.csv`. The `author_id` field in books is a lookup key; use a Bubble workflow or bulk update to resolve each Book's `author` relationship to its matching Author. Never treat raw author_id alone as an enforced privacy boundary.

**Privacy rules:** Author: only when `This Author's user is Current User`; Book: only when `This Book's author's user is Current User`; NotificationLog: author may read own logs if desired, but only admin can update. Admin condition: `Current User's role is admin` for all types. Lock down searches, auto-binding, and API exposure. Admin trigger buttons should be visible and callable only for admin.

Build Bubble pages: login; author dashboard with repeating group of Current User's Author's Books and sums; admin page with author repeating group and filters; detail page; notification log. Add API Connector POST to n8n webhook with shared secret header (keep secret server-side), passing author and notification ID. Configure n8n callback to a protected Bubble backend API workflow rather than the local Node callback.

## n8n

Import `n8n-workflow.json` in n8n. Set `OPENAI_API_KEY` and `WEBHOOK_SECRET` on the n8n host (environment variable access may be restricted by your n8n hosting plan). Configure Node server with `N8N_WEBHOOK_URL`, `WEBHOOK_SECRET`, and `PUBLIC_BASE_URL`. The public base URL must be reachable from n8n; localhost callback cannot be reached from n8n Cloud. The workflow sends the generated content to the callback; it does **not** send an actual email. Callback failures require monitoring/retry configuration in n8n; invalid webhook secrets currently fail without a callback by design. Verify your n8n version supports imported nodes and expressions.

## Local API

- `GET /health` public
- `POST /api/login` `{email,password}`
- `GET /api/me` bearer token
- `GET /api/authors` admin only
- `GET /api/authors/:id` admin or owning author
- `POST /api/trigger` admin only `{author_id}` or `{bulk:true}`
- `GET /api/logs` admin only
- `POST /api/notification/callback` shared secret header; `{notification_id,status,message}`

## Limits / security

This reference uses static dataset and file-based notification logs, not a persistent multi-user database. Token secret and passwords have insecure local defaults. No password hashing, rate limiting, audit trails, queue, robust idempotency across restarts, production-safe callback URL allowlisting, or verified email delivery. Do not expose this server to the internet without implementing those protections. The royalty status uses a simplified 90-day last-payout/publication threshold as the assignment suggests, not the full quarter settlement calculation. Actual next payout date cannot be reliably derived from the sample data alone.
