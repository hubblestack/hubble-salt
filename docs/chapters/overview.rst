Overview
========

Before you dive into learning about the four components of Hubble let's explore
a little background--some history of the project. Hopefully, given this
background, the overall design of HubbleStack will make sense.

History
-------

It's said that the squeaky-wheel gets the grease. I ended up building this
project becauese of an itch I needed to scratch. An annoyance that needed to go
away.

At `work` we were using a security compliance tool (also known as Tool X) that
didn't really agree with me. For one I didn't like the idea that the Security
Team would make decisions that affected my systems without my input. Maybe I'm
a little too interested in taking ownership of my systems than others. In any
case I didn't like the solution and was frustrated to be stuck with it. It was
during this phase that I set out to build a replacement.

I mentioned my frustration with my fiance (who just happens to work for a
different Security Team) and talked about what I could do about it. I credit
her for her insight and inception of this project. Also for helping me realize
how important a project like this could be.

The Modules
-----------

The first iteration of this project has fairly simple requirements: reproduce
the functionality we have with Tool X.

I set out to gather requirements, and the more I dug the less impressed I was
with Tool X. Turns out it *didn't* do quite a number of things. The basic
functionality boiled down to two things: HIDS and FIM. 
