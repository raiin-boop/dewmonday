# 🖌️ Art Tutorial App

> **Concept Status:** 🌱 Ideation
> **Last Updated:** June 2026

---

## Overview

A structured, creator-focused educational platform (web app + mobile) delivering art tutorials across skill levels and media — digital illustration, traditional drawing, photography composition, video editing, and more. The Dew Monday approach: project-based learning, community accountability, and a strong brand personality that makes learning feel like an invitation, not a chore.

---

## Problem Statement

YouTube tutorials are free but unstructured. Skillshare and MasterClass are broad but lack community. Most art education apps feel corporate or gamified in ways that miss the point. Aspiring creators want a clear path, real progress, and a place that gets their aesthetic.

---

## Value Proposition

- **Structured paths, not algorithm rabbit holes** — curated curricula by medium and goal
- **Project-first** — every lesson ends in something shareable
- **Community layer** — learners share, get feedback, and stay motivated
- **Dew Monday voice** — editorial, warm, creator-native

---

## Target Audience

| Segment | Profile |
|---|---|
| Beginner Artists | Age 16–28, wants to develop a real skill, no formal training |
| Creator Upgraders | Already making content, wants to level up visual quality |
| Career Pivoters | Exploring creative work as a side hustle or full-time shift |
| Hobbyists | Learning for joy, not income |

---

## Core Features (MVP Thinking)

MVP: Structured curriculum tracks, Video lessons with downloadable project files, Lesson progress tracking, Project submission gallery
V2: Community feed, Instructor portal, Certificate of completion, Creator Hub integration
V3: Live workshops, AI critique tool, Mobile app (iOS + Android)

---

## Tech Stack Considerations

| Layer | Options |
|---|---|
| Frontend | React / Next.js, React Native (mobile) |
| Backend | Node.js / Supabase / Firebase |
| Video hosting | Mux, Cloudflare Stream, or Vimeo |
| Payments | Stripe |
| Auth | Clerk, Auth0, or Supabase Auth |
| Animation/Video tooling | Remotion (for programmatic video content) |

---

## Revenue Model

- Monthly subscription (individual & team tiers)
- One-time course purchases
- Instructor revenue share (marketplace model)
- Bundled with Dew Monday store (gear purchase → free trial)

---

## Key Questions to Answer

- [ ] Web-first or app-first at launch?
- [ ] Build instructor marketplace immediately or start with in-house content?
- [ ] How does this differentiate from Skillshare / Domestika / Procreate's own tutorials?
- [ ] What's the minimum curriculum to launch credibly?
- [ ] How does community accountability work without becoming a moderation burden?

---

## Next Steps

1. Map out 1 full curriculum track end-to-end as a proof of concept
2. Define subscription pricing and tier structure
3. Evaluate Mux vs. Cloudflare Stream for video hosting cost
4. Sketch wireframes for lesson player + project gallery
5. Identify 2–3 potential instructors / content collaborators

---

*Part of the [Dew Monday](../../README.md) brand incubator.*
