# D16

Django_Project: MMORPG Board

Bulletin board for MMORPG Community


Users can register on the site by e-mail, after which they receive an email with a registration confirmation link.

After registration, users can create, edit and delete ads. When creating an ad, the user must define the ad into one of the following categories: Tanks, Heals, DDs, Merchants, Guildmasters, Questgivers, Blacksmiths, Leatherworkers, Potions Masters, Spellmasters.

Ads consist of a title and text that can include images, embedded videos, and other content.
Users can submit responses to other users' ads in plain text.
When sending a response, the user-author of the ad receives an e-mail with a notification about it.

The user also has access to a private page with responses to his ads, inside which he can filter responses by ads, delete them and accept (when a response is accepted, the user who left the response also receives a notification).

It is also possible to send newsletters to users.


Notifications implemented:
- registration confirmation letter - django-allauth
- changing user profile - Signals
- response status change - Signals
- subscription to the newsletter - Celery
- weekly newsletter - Celery
