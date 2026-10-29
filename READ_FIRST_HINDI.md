# BookLeaf — Features aur step-by-step guide

## Is ZIP mein kya hai
- Author/admin demo login aur role-based API access.
- Author ki apni books aur earned / paid / pending royalty totals.
- Admin author list, city/status/name filters aur author details.
- Individual aur bulk notification trigger, notification logs.
- 10 authors, 18 books ka dataset aur Bubble import CSVs.
- n8n webhook → validation → AI draft → Bubble log → response starter.
- Sample request, test checklist aur Bubble data/privacy setup instructions.

## Sabse pehle local demo chalayein
1. ZIP extract karein (ZIP ke andar se directly run na karein).
2. `local_demo/bookleaf_fixed` folder VS Code mein kholein.
3. Terminal mein `npm start` chalayein.
4. Browser mein http://localhost:5050 kholein.
5. Admin: admin@bookleaf.demo / Admin@12345
6. Author: priya.sharma@email.com / Author@12345
7. Check karne ke liye `npm test` chalayein.

Ye demo passwords sirf local testing ke liye hain.

## Aapke n8n screenshot ka issue
`Log Success to Bubble` ke URL field mein descriptive placeholder tha.
Dashboard preview URL ko us field mein paste karna sahi nahi hai.
Asli notification API endpoint aur uske accepted fields chahiye.
ZIP ka starter ek Data API URL dikhata hai: wo aapke account mein verified nahi hai.
Apne Bubble API configuration se endpoint copy karein. Guess na karein.

## n8n import aur configuration
1. `n8n_bubble_starter/bookleaf_assignment2_package/n8n/bookleaf_royalty_notification.json` starter hai.
2. Niche diya helper chalakar apna VERIFIED endpoint set karein:
   `python tools/configure_n8n.py --bubble-log-url "YOUR_VERIFIED_HTTPS_ENDPOINT"`
3. Helper `n8n-configured.json` banata hai. Ye output import karein.
4. Webhook par Header Auth credential configure karein aur Bubble request mein wahi header bhejein.
5. OpenAI aur Bubble token ko n8n credentials mein securely configure karein.
   Starter mein environment expressions hain; agar n8n Cloud environment access allow nahi karta,
   Authorization header expressions ko credential-based authentication se replace karein.
6. Bubble log request body ko actual endpoint fields se match karein.
7. Test webhook request bhejein; output aur Bubble log dono check karein.
8. Invalid request, wrong auth, AI failure, Bubble failure aur duplicate request test karein.
9. Tests ke baad workflow publish karein aur Bubble connector mein Production webhook URL use karein.

## Kya abhi complete verified nahi hai
- Ye native Bubble export nahi hai; existing Bubble project change nahi hua.
- Live n8n import/execution, credential configuration aur Bubble log verification nahi hui.
- AI email DRAFT generate hota hai; actual email send node included nahi hai.
- Starter mein complete failure branches aur persistent idempotency nahi hain.
- Local demo ka deduplication sirf 60-second Pending-request guard hai.
- Production-safe authentication/database deployment is package ka hissa nahi hai.
- Sample prompt mein quarterly/45-day policy text hai: original Knowledge Base se verify karein.
- 502/failure handler wala screenshot workflow is ZIP ka verified export nahi hai.

`START_HERE.md`, local README aur TEST_CHECKLIST.md mein detail hai.
