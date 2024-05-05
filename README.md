# Google Developer Student Clubs 2024 Solution Challenge
<br>

## Top 100 !! 🥳🥳

<br>


## wanna see commits? Go to Part Repo!
### iOS
<a href="https://github.com/GDSC-PathPal/PathPal-iOS">https://github.com/GDSC-PathPal/PathPal-iOS</a>

<br>

### AI/ML
<a href="https://github.com/GDSC-PathPal/PathPal-ML">https://github.com/GDSC-PathPal/PathPal-ML</a>

<br>

### Backend
<a href="https://github.com/GDSC-PathPal/PathPal-Server">https://github.com/GDSC-PathPal/PathPal-Server</a>

<br>

<img src="https://github.com/GDSC-PathPal/PathPal-iOS/assets/97840728/c0897eb3-76b4-4145-91e6-e64981cac42b" alt="표지" style="width:80%;" />
  
<br>
<br>

# ‣ Introduction
PathPal is a solution helps visually impaired people walk safely. 
PathPal provides an accurate route is provided through voice guidance from the starting point to the destination. In addition, it collects visual information through cameras, detects objects and analyzes them using AI/ML to informs users to prevent risk factors through voice and vibration.

<br>

### Watch the product demo on:

for top10
<br>
<a href="https://youtu.be/gaN0Xd2YYaM?si=UDmmAPTU4DeGubuK"> 
    <img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" alt="Youtube"/>
  </a> 	

<br>
for top100

<br>
<a href="https://www.youtube.com/watch?v=7HeddwSCQK8"> 
    <img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" alt="Youtube"/>
  </a> 	


<br>
<br>


# ‣ Initial sruvey and Probelm statement research

## complaints
<img src="https://github.com/GDSC-PathPal/PathPal-iOS/assets/97840728/b27cca0e-4dd1-4b9d-9bfb-c18c1550e2b9" alt="overview-h p" style="width:80%;" />

## needs of assistive device
<img src="https://github.com/GDSC-PathPal/PathPal-iOS/assets/97840728/058ff0c3-7a7f-4945-af70-c81cfd6412f4" alt="시장규모" style="width:80%;" />

<br>

- Of the 1.1 billion visually impared around the world, 44% have severe disabilities.
- Additionally, the global assistive device market size exceeded 14 billion$ in 2015. It is expected to reach approximately 25.6 billion$ in 2026.

<br>  
<br>
<br>


# ‣ Mockup

Light Mode(English)
<br>

<img src="https://github.com/GDSC-PathPal/PathPal-iOS/assets/97840728/0c62f68c-5103-4307-9538-d6c7058bd95a" alt="목업 라이트" style="width:80%;" />
<br>

Dark Mode(Korean)
<br>

<img src="https://github.com/GDSC-PathPal/.github/assets/97840728/58fb43f3-0a01-4cc9-80c6-72f6a4445a0c" alt="목업 다크" style="width:80%;" />
<br>

1. users can receive voice guidance for the route when they enter thier starting and arraival point.
2. If user is heading a correct starting direction, navigation will begin with vibration.
3. results of the camera screen analyzed by stride of the visually impaired person, will be announced through voice and vibration.
4. In the example screen, you can receive voice guidance such as, “crosswalk in the center and bollard on the right detected”

<br>

<br>
<br>


# ‣ Key Features

## Navigation
- Current location and heading Management
- Voice search for starting and destination
- Setting the correct starting direction using a compass

<br>

## Vision Assistance
- Voice guidance on objects and their locations shown on the camera screen
  - Detectable objects : beverage vending machine, bicycle road, braille sign, brailleblock, chair, resting place, lift , crosswalk, trashcan, green traffic
- Vibration guidance when detecting an accident-causing obstacle
  - Detectable Risks : block kind bad, raised curb, Pillar, bollard, barricade

<br>
 
## Globalization

<img width="692" src="https://github.com/GDSC-PathPal/.github/assets/97840728/0d2ceaed-698b-4d5e-8a95-b9c5ffc07803">


<br>
<br>
<br>


# ‣ UN SDGs targets


<img src="https://github.com/GDSC-PathPal/PathPal-iOS/assets/97840728/7dcf1db8-e8b7-4331-b721-7306610d9791" alt="목표 SDGs" style="width:80%;" />


<br>
<br>
<br>

# ‣ Expected Values
<img src="https://github.com/GDSC-PathPal/PathPal/assets/97840728/7ce882f4-1f43-4344-96c8-7e57f264277d" alt="기대 효과" style="width:80%;" />


<br>
<br>


## Architecture
<br>

<img src="https://github.com/GDSC-PathPal/.github/assets/97840728/db6ddc51-5c5d-4a6f-81bc-f8ed09d13339" alt="아키텍쳐" style="width:80%;" />

<br>
 
## iOS
### Guidance
**You can seek swift code following steps below.**
1. Go to PathPal directory
2. Since iOS code of PathPal follow MNVVM patter, you can check View, ViewModel, Model code in directories.
3. Localized string keys for multilingualn is in en.lproj


<br>
<br>
 
## AI/ML

### Data label collection (before filtering)

<img src="https://github.com/GDSC-PathPal/PathPal/assets/97840728/528f2b3a-18d8-4d4a-992a-090495713238" alt="ML레이블" style="width:80%;" />


### Data label collection (after filtering) - actually providing on service
bold - with vibration alert

#### Pavement status

- **flatness_D, flatness_E**
- **paved_state_broken**
- **block_kind_bad**
- outcurb_rectangle, outcurb_slide, **outcurb_rectengle_broken**

### Obstacles on sidewalk

- **sidegap_out**
- **steepramp**

### Brailleblock

- brailleblock_dot, brailleblock_line, **brailleblock_dot_broken**, **brailleblock_line_broken**
- bicycleroad_broken, bicycleroad_normal

### Crosswalk

- **planecrosswalk_broken**, planecrosswalk_normal

### Means of transportation

- restsapce
- ~~stair_normal, stair_broken~~
- lift

### Signs

- sign_disabled_toilet
- braille_sign

### Infra and Resting places

- resting_place_roof
- chair_multi, chair_back, chair_handle
- beverage_vending_machine
- trash_can

<br>


## Backend
<img src="https://github.com/GDSC-PathPal/PathPal/assets/51076814/42f9e869-2444-4918-9007-c6dac59d4e21" alt="server architecture" width="800">

<br>



# ‣ Getting Started
Download Femunity directly from our GitHub repository. After downloading the app, you can sign up for an account using your Google account or use Guest Mode to explore the app.

### Prerequisites
Before you start, make sure you have installed the following on your system:
- JDK 17

### Installation
##### ML & Server
- Clone the Pathpal repository from GitHub
   - ML : https://github.com/GDSC-PathPal/PathPal-ML
   - Server : https://github.com/GDSC-PathPal/PathPal-Server
- Start ML
  - pip install -r requirements.txt
  - python inference_yolov8.py
- Start Server
  - java -jar PathPal-0.1.0.jar
  - **You must turn on the server after the ML server is turned on**
 
iOS ML & Server
- Clone the Pathpal-iOS repository from GitHub
   - https://github.com/GDSC-PathPal/PathPal-iOS
  - **You must get the required API-Keys and config files before running**
  - **You must turn on the server after the ML server is turned on**

# ‣ License
PathPal-Server is licensed under the terms of the MIT license. See [License.txt](https://github.com/GDSC-PathPal/.github/blob/main/LICENSE) for more information
