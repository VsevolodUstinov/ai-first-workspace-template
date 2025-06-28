# Candidate Pipeline — Senior Marketing Analyst

This document defines the full hiring process stages and AI evaluation triggers for the Senior Marketing Analyst position.

---

## 📊 Full Process Stages

| Stage | Description |
|-------|-------------|
| 1️⃣ New Application | Candidate applied or sourced (from Huntflow or manual entry) |
| 2️⃣ Screening Interview Scheduled | Screening interview appointment created |
| 3️⃣ Screening Interview Completed | Screening interview conducted, transcript available |
| 4️⃣ Screening Evaluation Done | Screening Agent completed initial evaluation |
| 5️⃣ Technical Interview Scheduled | Technical interview appointment created |
| 6️⃣ Technical Interview Completed | Technical interview conducted, transcript available |
| 7️⃣ Full Evaluation Done | Full Evaluation Agent completed final evaluation |
| 8️⃣ Hiring Decision Pending | Human committee reviewing AI evaluation |
| 9️⃣ Offer Extended | Offer sent to candidate |
| 🔟 Offer Accepted / Rejected | Final hiring outcome |

---

## 🔄 Huntflow Status Mapping

| Huntflow Status | Elly AI Pipeline Stage |
|------------------|------------------------|
| New | New Application |
| Screening | Screening Interview Scheduled |
| Screening Done | Screening Evaluation Done |
| Technical Interview | Technical Interview Scheduled |
| Technical Done | Full Evaluation Done |
| Decision | Hiring Decision Pending |
| Offer | Offer Extended |
| Hired | Offer Accepted |
| Rejected | Offer Rejected |

---

## 🤖 AI Agent Trigger Points

| Stage | AI Agent Action |
|-------|-------------------|
| After Screening Interview Completed | Run Screening Agent |
| After Technical Interview Completed | Run Full Evaluation Agent |
| After Full Evaluation Done | Save Final Score |
