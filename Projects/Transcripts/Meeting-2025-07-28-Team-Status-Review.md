# Team Meeting Transcript - 2025-07-28 - Project Status Review

**Date:** July 28, 2025  
**Participants:** Manager 1, Analyst 1, Developer 1, Developer 2, QA Engineer 1, Project Manager 1  
**Meeting Type:** Weekly project status review  
**Duration:** 2 hours  

---

## Meeting Start

**Manager 1:** Let's continue with the checklist, guys, because we've been gathering for half an hour already. Anyway, let's start with Client-Logistics.

**Analyst 1:** On Client-Logistics, we've added all custom metrics as part of working with [Name]. Top 5, bottom 5 campaigns make sense, yes. Depending on custom metric switching, this works.

**QA Engineer 1:** For the main report, put in the comments immediately that there are no questions specifically with Google Analytics sessions. In three days we'll have final verification for all of us.

## Discussion of Client-Beauty1

**Developer 1:** What's the question, guys? Previous period sessions just don't display on the main page. Need to check now.

**Manager 1:** Is this exactly how it doesn't work in the system?

**Analyst 1:** Unknown. Seems like it should work. Pretty obvious metric.

**QA Engineer 1:** So, in the full report we have all metrics displayed, yes. Let's check again, I looked today.

**Developer 1:** Metrics display additional indicators, we output them as part of the task, this all works. Simplified fits in one screen, yes, it fits. Grouping works correctly, that's 100%.

**Analyst 1:** We have GA4Purchase, but this, as far as I remember, isn't GA4Purchase. [Name], let's double-check custom metrics, custom conversions separately.

## Technical Discussion

**Manager 1:** At the level of all report sheets. Based on metrics within reports, can management decisions for marketing management really be made?

**Analyst 1:** Yes. The report updates to the time specified in settings, no later.

**QA Engineer 1:** Every team member can read the report without problems and doesn't get confused with metrics. Good question. We'll determine this in a separate meeting.

**Developer 1:** I wouldn't say everyone understands everything. We can explain how the business process works based on the report and suggest three optimization points.

## Data Problems

**Analyst 1:** Don't like that Client-Beauty1 didn't calculate for some reason. Can you check data for June 25th?

**Developer 1:** I think this doesn't work because there's no GA4 data. You see, there are empty cells here, this shouldn't be.

**QA Engineer 1:** There's no data at all for the 25th. Need to scroll backwards?

**Analyst 1:** That's why our customer LTV wasn't calculated. Check the 25th...

**Manager 1:** Shouldn't the data be tied to Google Client ID at all?

**Developer 1:** It shouldn't be, but... We don't have Google Client ID from this period, accordingly, the system didn't merge the data. Data can merge by one value, but if there was more complex merging by email, hash, user ID, client ID, then the system won't connect them if there's no data.

## Recommendations and Plans

**Project Manager 1:** [Name], one more recommendation. Let's somehow fix the time period we're looking at in this checklist, because errors often appear when we check on some dates, then show through others.

**Manager 1:** And the client, as a rule, asks for what data, for what period reports can be viewed. So we need to look uniformly.

**Analyst 1:** Well, what period should we take? Three months?

**Developer 1:** No, we can't take three months, because when did we fix the system? On the 17th last time.

**QA Engineer 1:** The 17th and we look, then, if nobody objects.

## Discussion of Client-Beauty2

**Analyst 1:** There's also a problem on the 20th, LTV also didn't calculate, and additionally... It seems like we partially didn't receive orders...

**Developer 1:** Or there weren't any. Just once more, you have such numbers, like 1, 2, 3, it's not excluded that there was 0 for that day. So check if there really are no orders there.

**Manager 1:** Let's keep going. In the referral source, top-5 sources by referral page by sessions were created, honestly, I don't remember the details.

**Analyst 1:** We have 588 sessions total, and yes, these are all sessions that are here for this period, they were all distributed across these channels. Let's try to extract something meaningful from referral other as a separate task.

## Metrics and Integrations

**QA Engineer 1:** There's a Top Impressions Share metric. It's probably in the system.

**Developer 1:** [Name], do you remember? Top impression share, and absolute top impression share.

**Project Manager 1:** [Name], what did you say about it, that it's only related to certain campaigns, like it shows something related to competitors, but anyway, we needed to clarify because there was no clear explanation.

**Manager 1:** Listen, let's just delete it to hell.

**Analyst 1:** Bad option, because it's in the checklist, and it's marked here as mandatory for report output. I think by deleting it, we're signing ourselves up for problems.

**Developer 1:** If we don't know what it is, we're also signing ourselves up for problems.

**QA Engineer 1:** No, so let's just add a comment here, like figure out details. Where did it even appear in the list? Even interesting.

## Client-EdTech - New Project

**Manager 1:** For the new project, I saw that you even got the project's website. Crazy, that's success.

**Developer 1:** Yes, we got the website, actually, we haven't gotten any access yet, and they still haven't signed documents, I'm poking them now. But tomorrow we need to do planning, that is, at least analyze the website.

**Analyst 1:** And I already made a task, as you asked, for [Name], together with a link to another project. With all these steps, how to connect.

**QA Engineer 1:** The website, as of today, they were supposed to launch advertising, so the website should be working. But if it suddenly becomes noticeable that something's not working there, we need to tell them immediately.

**Developer 1:** Tell me, and I'll tell them. Well yes, seems like tomorrow we have planning. I'll try to get something out of them today, but they, damn, even couldn't sign the NDA yet, so it's difficult.

## Meeting End

**Manager 1:** Anyway, I'll schedule a meeting for tomorrow. We have a meeting with you, [Name], but [Name] decided that Client B defense is more important. So I'll set it a bit earlier.

**Analyst 1:** We'll look at this scheme on our typical weekly calls just right. If you have time, I'll do it today, yes, and send it to you so you can see.

**Manager 1:** So today-tomorrow here, then weekend again, and when will you return?

**Developer 1:** Yes, Monday again. Monday again, I'll be here three days, then two days off again, and that's it, and then this whole story will end.

**Project Manager 1:** Okay, good. Well, basically, this is our main topic, conduct planning, and I'll try to get everything from the client by tomorrow.

**Analyst 1:** Access is really needed, because [Name] could connect this within a week, I would come on Monday, already check, already include in the report.

**Manager 1:** Yes. Okay, agreed. That's it, then let's go to the client.

**Everyone:** Let's go, thanks, bye.

---

**Next Meeting:** August 4, 2025  
**Main Focus:** Complete integrations, check Client-Beauty1, launch Client-EdTech
