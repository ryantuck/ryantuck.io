---
title: "Resume Building"
date: 2020-06-21T21:07:01-04:00
draft: true
---

## Plan

The table stakes here seem to be:

- Generate a PDF
- Display online
- Don't edit exclusively in html

## Discovery

I've discovered [JSON Resume](https://jsonresume.org/), which seems like a really wonderful way of splitting the content out from the display layer. Now I'm not shoe-horned into a design, so I can iterate fast on that bit.

For storing the resume, I'm actually storing it as yaml so it's actually manageable to edit, and then leveraging `pandoc` to translate it.

Storing it in a [github gist](https://gist.github.com/ryantuck/a9f824957b8500d4a0a470731c815d51) named `resume.json` allows me to automatically have a version available here, which is sweet: https://registry.jsonresume.org/ryantuck

The templates don't work _that_ well, so I'll likely need to end up laying it out myself. Fortunately, I know enough react to make that (I think?) fairly straightforward.

## Unknowns

**How should I enable formatting like a PDF?**

I had accomplished this the last time I was doing this [here](https://github.com/ryantuck/ryantuck.github.io/blob/master/print-resume/index.html).

Okay, I was able to figure out an A4 size page. I think that should be sufficient.










