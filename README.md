# HackZurich22

## Setup

1. create virtualenv if there is no such thing

`python3 -m venv venv`

2. activate virtual env

`. venv/bin/activate`

3. install requirements

`pip install -r requirements.txt`

4. You also need to provide correct tokens for Ai21 and GPT-3. Without them the part of the code relying on these services is not working.

## Status

Currently the project contains:
- initial functions related to backend responsible for collecting data from LinkedIn (using the authorization through the Linkedin account in case of user consent).
- storing data into a initial database and structures: classes, lists and a network (designed for scaling up when more time is available)
- a seed implementation for MatchMaking (`matchmaking` directory in the repo) where we were able to show how cutting-edge tech (transformers like AI21 and GPT-3) might be used to solve the problem of matching the right volunteers with the right needs. We implemented a customizable way to weight

## Future plans
Finally the project is planned to contain a system to collect the feedbacks in order to improve the system in the long term.

Moreover, currently the frontend is visualized using the rapid prototyping tool (figma) but we plan to implement the frontend using a scalable lightweight frameworks.

We plan two sides of the experience suited for two different group of users: one for volunteers (done in figma), second for NGOs / companys to provide volunteering opportunities. We were not able to address this perspective on time, but we listed planned experience from the NGOs perspective:
- invitation link to register to the program
- registration detail through the social accounts (similarly to the experience of the volunteers)
- dashboard to add, modify or check vv (volunteering vaccancies)
- approve/reject volunteer. In case of approval the points are to be transferred to the volunteer account
- ability to find potential volunteers based on the similarity score even if they're not yet signed up

We also thought to add nice features to improve the user experience like an ability to talk to potential volunteer leveraging the whatsapp bot so the experience will be the best and the interested person can instantly accept/ reject based on preferences and availability. 

## References
[figma prototype](https://www.figma.com/file/04LYMt9HBrwp2OcHwHyUu8/HackZurich-2022?node-id=0%3A1)

[slides](https://docs.google.com/presentation/d/1Mexdbd98SMmIZqn5KvacZ5BWgntLuSyD/edit?usp=sharing&ouid=113434312309221824159&rtpof=true&sd=true)

[pitch recording](https://youtu.be/xzUIwHXxf4s)

## Acknowledges
We want to thank Zurich Insurance for giving us a nice challenge that directed us to this nice area where we believe the right technology can help
Also we thank to HackZurich for organizing the great experience both on-site and remotely.

Thank you,
Team Missing Australia
