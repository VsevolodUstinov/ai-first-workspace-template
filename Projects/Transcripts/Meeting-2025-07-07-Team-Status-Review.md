# Team Meeting Transcript - Project Status Review

**Date:** 07/07/2025  
**Participants:** Manager 1, Analyst 1, Developer 1, Manager 2

---

**Manager 1:** Hi everyone! Let's review our projects. I'll start with Client-Logistics. They finally have updates. They've deployed ads on two systems - Google and LinkedIn. They're not giving us access yet, but [Name] promised to provide access.

**Analyst 1:** Yes, I looked at what's happening with them. On Google they launched YouTube ads, but there's an issue - the video doesn't lead anywhere. There's only a mention to visit and subscribe to their account. No direct links at all.

**Manager 1:** They're super worried about moderation. The point is - they're running these ads now, and unfortunately for now it will drive traffic as direct or organic, because no links are provided anywhere.

**Developer 1:** What about their LinkedIn?

**Manager 1:** On LinkedIn they launched two campaigns. Inside the first one there are two tests. Both lead not to the website, but to booking through Calendly for a call with a manager. The problem is they don't have UTM tracking in Calendly.

**Analyst 1:** According to them, they tried, but it didn't work. Do we have any other experience with this?

**Manager 1:** We suggested that other clients have different onboarding formats. Through fillout, MarketWhiz, whatever. And you can put tracking there. They said they'll think about it, but don't want to for now.

**Developer 1:** Can they drive people to the website and give them a "Book a demo" button there?

**Manager 1:** Not yet. They're trying their best not to drive to the website because all their accounts got blocked before.

**Analyst 1:** What else will they have besides Google and LinkedIn?

**Manager 1:** There will also be Facebook. Facebook will launch through a partner account. For Facebook they're ready to install our script, set up cross-domain tracking and put a tagged link on the button.

**Manager 2:** Do partners allow them to install third-party scripts?

**Manager 1:** From what their CEO said - yes. I think he hasn't talked to partners yet. We connected [Name] and [Name] there, they said okay, but only CEO has control.

**Analyst 1:** Good. Moving on to Client-Beauty1?

**Manager 2:** Yes, about Client-Beauty1. We implemented customer attribution logic as they needed. [Name] created a document, we put it in Notion. We'll need to clarify if they have questions about this. We cleaned up other, meaning unknown. Everything in the report got better.

**Developer 1:** Regarding influencers and promo codes - everything's good, everything's available in the report. The client complained that our update on the 5th didn't work, but I highlighted it and ran it manually.

**Analyst 1:** How are things with hashes?

**Developer 1:** I checked several times in different windows. Hashes work everywhere. Phone number and email are saved everywhere. I went to their test site - everything's correct.

**Manager 2:** Where does the Google Client ID tracking break? They have an issue with pass-through.

**Developer 1:** I can't say the specific place where Google Client ID might break now. Need to look separately, I'll add a task to check hooks on all website pages.

**Analyst 1:** Okay, what about Client-Beauty2?

**Developer 1:** We still have the issue that the script doesn't cover all email input forms. There was an issue where Google Client ID wasn't passed through normally, but the paradox is that as soon as we reinstalled the app, the pass-through percentage dropped.

**Manager 1:** Why is that?

**Developer 1:** Because before, static coefficients were written to null Google Client ID fields. After the fix, all null Google Client ID values started coming with zero. The percentage dropped because of this.

**Analyst 1:** Not exactly. He fixed it and now it should be better. I deployed the fix on Friday, we can check today or tomorrow.

**Manager 1:** What do we do about UTMs?

**Developer 1:** UTMs are on me. Need to research how the mechanism works inside Shopify, how it determines UTM tags. This will take time.

**Manager 2:** What about consent mode and banner? Wouldn't it be easier to transfer the task to [Name]?

**Developer 1:** We transferred the task to [Name], he gave it back. This needs to be configured on the client side and rolled out to all European countries.

**Analyst 1:** Moving on to Client-Food?

**Manager 1:** About Client-Food - this week Monday they'll have Moldova, Wednesday will be Romania, Shopify data. After that we can start installing the script with hashes.

**Developer 1:** They also have a question about separating Romania and Moldova countries within the report. [Name] isn't sure they'll have one Shopify for two countries.

**Manager 1:** I think it will be one. When they launch in Europe, will they have 20 Shopify stores? That's nonsense. Most likely we'll filter orders by tags.

**Analyst 1:** What about Client-EdTech?

**Manager 2:** We have 17% unknown revenue according to their data, and it's unclear how to fix this, even after Client ID pass-through.

**Developer 1:** What percentage was it at launch?

**Manager 2:** I think it was slightly less. Looking now - in December it was 9%, now it's 17%.

**Analyst 1:** They're catching some users who extend subscriptions from 2021 that we don't know anything about.

**Manager 2:** We can make an export of these contacts and tell them - we don't know where they came from. No Client IDs, no UTMs, nothing was written to them. We need to solve this question together.

**Developer 1:** We can try to look at contacts from June that are in unknown, try to find their events in Google through hash.

**Analyst 1:** Good. And the last one - Client-Logistics (additional project)?

**Manager 1:** About Client-Logistics (additional project) - they wrote to me that they have holidays, almost another month. But accordingly she gave us access to adjust, to all systems. Now publishing script, plus they published QR codes and unique client IDs are generated there.

**Developer 1:** Can't deploy server yet because of holidays?

**Manager 1:** Yes, but there's progress. These are the main updates.

**Manager 2:** Good, that's all from me. If there are no questions, let's finish here.

**Analyst 1:** Great, see you next week.

**Manager 1:** Yes, let's meet Thursday at the same time. Thanks everyone!

---

**Meeting Duration:** 45 minutes  
**Next Meeting Date:** 14/07/2025
