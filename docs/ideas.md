# Ideas

Plenty of ideas, free for sharing, because execution is the hard part.

## Code

### Dynamic visualizations for sound

Generate dynamic video based on sounds inputs. This seems really accessible. Unclear why auto-pattern-gen video isn't more common, especially at clubs etc.

Would leverage generative art.

### Vim plugin to open configured urls under cursor

For jira ticket PROD-123, hitting `gx` or some similar keystroke pops open a predictable url string in browser.

Use the idea of chrome custom search engines.

Could use it to google stuff, go to github, etc.

### I Love Hue generator / solver

I Love Hue is a great game.

Create a generator in javascript or something for arbitrarily large grids of any hue.

Write a solver for it. Visualize solves.

### Random metaphor generator

Create some adlib structures, compile list of nouns, verbs, etc, and generate.

Create a twitter bot that spits out a random metaphor once a day. Tweets designed for replying to prompt by quote-tweeting.

- {Uber/Airbnb/Warby Parker} of {industry}
- {Brutalism} as it applies to {airplanes}
- {Romanticism}, but for {software development}
- {Moore's law} as it applies to {hand washing}



## Math / Simulations

### Airplane seating simulations

Would be easy to build some basic visualization on top of basic data model / processing. Started this project on github.

Answer questions like:

- What lineup scheme is best for airplane seating to optimize for time?
- On a Southwest flight, given boarding position B34, what is the likelihood that you'll find a window / aisle seat? How far back should you go before just grabbing the first middle seat, trading off between sitting further back etc?

### Elevator waiting simulations

Basically the same as above. Given visitor poisson distribution, how long


### Land distribution stats for MTG

Understand stats for splashing colors, etc. This math is likely pretty straightforward. Understand possibilities of how lands play out if, for example, I'm playing Llanowar Elves, can dig for basics, etc. Basically, if I want to splash black for Garruk, how many swamps am I actually going to need given the other cards in my deck to be able to pay for him 80% of games once I draw him?

### Final trivia statistics

Given 10 teams at trivia, we're in 4th currently, the final trivia category is 80s movies, how much should we wager?

Should take into account existing point distributions, likelihood of average team getting it right, likelihood of other teams betting the house (common bet), likelihood that we're more well-suited to answer it, risk tolerance, need to win, or just get top 3, etc.

### Moneyball for fantasy football

I am sure people do this, but it would be neat to add other features. Provide beta distribution graphs for player, team overall, win percentage against opponent's roster, etc.


## Art

### Overwhelming sensory experience

Create a small room with LEDs covering the walls, insane sound system, maybe really intense HVAC, scents, massage chair, water, etc to completely blast senses.

Open source program generation. Provide configurable controls. Could be a hit at music festivals. Use generative patterns that respond to sound, or not.

Planetarium-style setup could be cool. Single-person or group-of-friends setup.


## Physical

### Good book holder

I like physical books. I hate sprawling out my fingers under a book. I hate not being able to lie down and just read a book, especially a heavy boy.

Something elegant and physical that would hold a book open and hold its pages back. Page turning would be trivial. Could have a handle to hold instead.

Ideally it could have a thin-enough form factor that just hooking onto the book like a bookmark or something would be acceptable.

Worst case, make something that can prop up on a table.

### One-handed bowl lighter

If one were to partake in smoking CBD in a bowl, I might imagine that one might want to be able to do so with one hand.

One may even desire to construct such an object such that it may clip onto said piece.

### Nuanced shower handle

Solves the problem of having a tiny range of shower handle available to access reasonable temperatures.

Use some sort of non-linear gear system on a shower handle to make 90% of the handle swing within reasonable shower temps, then rapidly go hot or cold at the ends of the swing.

This would apply equally well to gas stoves, sink faucets, etc.

My guess is that these sorts of gear systems have existed for a hundred years or more, but clearly haven't been applied to showers, where they would be helpful.



## Apps

### Better recipe site

Create a recipe site that doesn't have a 10-page essay and 4000 ads on it. Make it based on graphs. Each node is a step with a duration. Auto-gen an optimized gantt chart. Make the display look really nice. Allow for crowd-sourcing recipes. Ideal for sharing. Leverage common steps to make input easy (eg mince garlic, boil water, etc).

Cooking for engineers or something is a site that starts on this idea but I don't recall it being slick when I last checked it out.

### Dumb Alarm

Make a stupid simple alarm app that only ever has one alarm, and only works in 5-minute intervals. One tap to alarm creation.

### Insert-only text app

I want to make inboxing thoughts easier. The lightest app possible, automatically bring up the keyboard, hit enter and send thought to pubsub queue or something for later processing. Can configure destination and auth within the app maybe. Could offer hosting.

### Middleman

Something that hooks into various jira, github, etc projects and allows you to create edges between nodes. Tie tickets to PRs, etc, have a nice interface for managing the graph. Provide chronological interface as well.

Something interesting about this app not providing any more functionality than basically foreign-keying to other systems and tying things together.

Alternatively, base of app could simply provide nodes as basic text boxes, and provide linking capabilities. This is kind of roam, but have some default `JiraTicketNode`s etc available for more power.

### Better spreadsheets

I'm interested in using a spreadsheet app with the following features:

- Version control
- Async computation-first
- Numbers-esque layout to support multiple tables in view simultaneously, but with snappier grid
- Testing, etc.

Like an accessible python notebook or something, for generating neater or more sensical outputs.

This generally feels like it would be a sort of R / pandas thing, a little like GCP dataflow, but without requiring the need to spin up R clusters or whatever. Could scale infinitely with lambda backends.

Come to think of it, datastudio is sort of this. I haven't used it enough to understand how many of these problems it solves.

### Boomertech.com

Create best go-to self-aware Boomer Ed site for tech stuff (how do i reset my router?)

Instead of "ugh mom just google it", curate howto articles.

Figure out how to monetize without ads, obviously.


### iOS remote trigger camera app

I set my phone up somewhere, use your phone to trigger the camera.

Could ideally even switch the camera lens used with the new iPhones.

This probably exists.

### Fully-manual iOS camera app

This probably exists. Allow user to configure aperture, etc.

### Drag-n-drop unix tools

Some scratch-like interface for unix tools in a sandboxed environment would be sweet.

The idea here is piping `xargs` to `sed` to etc.

The tech could be a pretty simple lambda backend to read in lines of stdin. Would still cohere to the principles of running on a given machine.



## Half-baked

Little-to-no-thought has been put into curating these. Buyer beware.

- There's gotta be a better way for babies to fly. What would economics of that look like.
- Apex for hosting / deploying a static site to your own S3 bucket. Save your own stuff, sign up for a hosting route53 entry. 50c per month. Don't think about it.
- Shell command generator / common use case guide.
- Seatswap.io - coordinate seat swaps.
- Code challenge site - halite for basic programming skills, connect companies and learners, something about lambda school. I think this might be hackerrank.
- Uber for storage
- Motorized land vehicle RC - simulate boat on water, rollers underneath, etc.
- Hotel rooms with premium stuff on sale
- Skiing - watch coordinated paths on 3d map through time using skitracks files
- CX blog for all company experiences
- Service to call and wait on hold for you, and call you when it's ready
- AI for sorting grocery lists (group ketchup n mustard together)
- Musician tipping app, because no one carries cash (QR code, straight to venmo? Just venmo?)
- Thanks and sorry lights back of car
- Queue line with finite amount of choices for switching lines - feeling of agency and order
- Ad network across multiple sites with opt-ins to reasonable policies
- Better map sharing service online
- Installable window screens with flexible edges for tight fitting
- Some twitter plugin whereby tweets get categorized using NLP / mechanical turks - to highlight likelihood a tweet is just signaling, actually true, based on user's past tweets and reliable past categorization
- Computer vision for plant veins area analysis
- Stackable rubber rings for storing pan lids
- Hibachi for other cuisines
- Customer discounts for helpful behavior
    - Ride share - pay more faster arrival
    - Scooters - incentivize parking within certain geofence for discounts
    - Gas stations on highway - pay 3x for express line, those discounts get passed onto "bottom" line where gas is commensurately cheaper. take advantage of people in rush, willing to pay.
- A tiny RGB LED connected to a watch battery is a great and cheap always-on nightlight









































