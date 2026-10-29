# Bubble integration setup
1. Enable backend workflows and Data API in Settings → API; expose only required types.
2. Confirm NotificationLog Data API type and exact field keys. The starter assumes request_id, author_id, status, content, sent_at; adjust to actual schema.
3. The sample endpoint is https://bookleaf-royalty-dashboard-39532.bubbleapps.io/version-test/api/1.1/obj/notificationlog — verify it with a real test.
4. Call n8n authenticated webhook from an admin-only Bubble backend workflow. Never expose secret tokens in browser logic.
5. Configure privacy rules for author-only data and admin-wide data.
6. Add a notification log and a failure callback; implement idempotency for repeat clicks.
7. Regenerate/revoke any previously exposed API token; never commit tokens to ZIP or GitHub.
