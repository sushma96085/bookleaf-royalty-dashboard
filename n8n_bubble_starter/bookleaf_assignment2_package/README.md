# BookLeaf Assignment 2 — Integration Package

This is an **importable n8n workflow starter**, not a verified export of your Bubble application. It has NOT been executed against your Bubble database. Do not submit it as a fully tested solution until the checklist is complete.

## Existing Bubble application
- Editor: https://bubble.io/page?id=bookleaf-royalty-dashboard-39532
- Test app: https://bookleaf-royalty-dashboard-39532.bubbleapps.io/version-test
- The Bubble application remains hosted in your Bubble account; it is **not included** in this ZIP.

## Contents
- `n8n/bookleaf_royalty_notification.json` — importable workflow scaffold (Webhook → Validate → Compose AI Request → OpenAI → Prepare Bubble Log → Bubble API → Respond).
- `samples/webhook_request.json` — **synthetic** example request, not BookLeaf dataset.
- `docs/BUBBLE_SETUP.md` — required Bubble-side configuration.
- `docs/TEST_CHECKLIST.md` — verification and submission checklist.

## Import into n8n
1. Open n8n → Workflows → Import from File → choose `n8n/bookleaf_royalty_notification.json`.
2. In Webhook node, choose Header Auth and create a credential with a random shared secret. Set the matching secret in Bubble API Connector; do not expose it to authors or the browser.
3. Set `OPENAI_API_KEY` and `BUBBLE_API_TOKEN` as securely managed n8n variables/credentials (the starter uses `$env` placeholders, which may not be available in your n8n Cloud plan). If `$env` is unavailable, replace the HTTP Request nodes' header expressions with n8n's **Header Auth** credentials, not hardcoded secrets.
4. Configure the Bubble API endpoint in the `Log Success to Bubble` node. This starter creates a new NotificationLog record via POST; ensure Bubble's type/field API names match the request body. Use a separate Bubble backend workflow for updates or stricter authorization if needed.
5. Test with sample request using n8n's **Listen for test event**, then verify actual Bubble NotificationLog record and webhook response.
6. Activate/publish only after privacy, permissions, duplicate prevention and error-path tests pass.

## Important limitations
- AI generation requires a working OpenAI API key and billing/limits.
- Callback may fail until Bubble Data API, NotificationLog type, field names and permissions are configured.
- The workflow does not yet implement robust cross-execution idempotency, failed-callback logging, or a fully verified failure branch. These are mandatory fixes before calling the assignment complete.
- It assumes Bubble passes full author/book/royalty data in the webhook; do not send private records to an untrusted client.
- Never share or commit real API keys.
